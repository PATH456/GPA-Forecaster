from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Term(models.Model):
    # A term is one school semester, like Fall 2026.
    class Season(models.TextChoices):
        SPRING = "spring", "Spring"
        SUMMER = "summer", "Summer"
        FALL = "fall", "Fall"
        WINTER = "winter", "Winter"

    season = models.CharField(max_length=20, choices=Season.choices)
    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2200),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show newest terms first.
        ordering = ["-year", "season"]
        constraints = [
            # Do not allow the same term twice.
            models.UniqueConstraint(
                fields=["season", "year"],
                name="unique_term_season_year",
            )
        ]

    def __str__(self):
        return f"{self.get_season_display()} {self.year}"


class Course(models.Model):
    # Each course belongs to one term.
    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=120)
    credits = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["term", "code", "name"]
        constraints = [
            # Do not allow the same course twice in one term.
            models.UniqueConstraint(
                fields=["term", "code"],
                name="unique_course_code_per_term",
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"


class GradeComponent(models.Model):
    # A component is one grading category for a course, such as quizzes or exams.
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="components",
    )
    name = models.CharField(max_length=100)
    weight_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    item_count = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(500),
        ]
    )
    points_per_item = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["course", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["course", "name"],
                name="unique_grade_component_name_per_course",
            )
        ]

    def __str__(self):
        return f"{self.course.code} {self.name} ({self.weight_percent}%)"


class GradeItem(models.Model):
    # A grade item is one score, such as Quiz 1 or Exam 2.
    component = models.ForeignKey(
        GradeComponent,
        on_delete=models.CASCADE,
        related_name="items",
    )
    name = models.CharField(max_length=100)
    earned_points = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )
    possible_points = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show grade items in the order they were created.
        ordering = ["component", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["component", "name"],
                name="unique_grade_item_name_per_component",
            )
        ]

    @property
    def is_graded(self):
        # No score means this item has not been graded yet.
        return self.earned_points is not None

    def __str__(self):
        return f"{self.component.name} - {self.name}"
