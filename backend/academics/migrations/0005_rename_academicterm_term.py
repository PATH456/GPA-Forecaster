from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academics", "0004_alter_gradeitem_options_remove_gradeitem_due_date"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AcademicTerm",
            new_name="Term",
        ),
        migrations.RemoveConstraint(
            model_name="term",
            name="unique_academic_term_season_year",
        ),
        migrations.AddConstraint(
            model_name="term",
            constraint=models.UniqueConstraint(
                fields=("season", "year"),
                name="unique_term_season_year",
            ),
        ),
    ]
