from django.db import migrations, models


COMPONENT_LABELS = {
    "homework": "Homework",
    "quiz": "Quiz",
    "lab": "Lab",
    "midterm": "Midterm",
    "final": "Final",
    "participation": "Participation",
    "project": "Project",
    "other": "Other",
}


def convert_choice_values_to_labels(apps, schema_editor):
    GradeComponent = apps.get_model("academics", "GradeComponent")

    for component in GradeComponent.objects.all():
        component.name = COMPONENT_LABELS.get(component.name, component.name)
        component.save(update_fields=["name"])


def restore_choice_values(apps, schema_editor):
    labels_to_values = {label: value for value, label in COMPONENT_LABELS.items()}
    GradeComponent = apps.get_model("academics", "GradeComponent")

    for component in GradeComponent.objects.all():
        component.name = labels_to_values.get(component.name, "other")
        component.save(update_fields=["name"])


class Migration(migrations.Migration):
    dependencies = [
        ("academics", "0005_rename_academicterm_term"),
    ]

    operations = [
        migrations.RunPython(
            convert_choice_values_to_labels,
            restore_choice_values,
        ),
        migrations.AlterField(
            model_name="gradecomponent",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
