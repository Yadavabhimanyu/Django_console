from django.db import models

# Create your models here.
class process_file_repo(models.Model):
    project_name=models.CharField(max_length=25)
    process_name=models.CharField(max_length=25)
    from_date=models.DateField()
    to_date=models.DateField()
    to_time=models.TimeField(auto_now=False, auto_now_add=False)
    project_file=models.CharField(max_length=25)

    def __str__(self):
        return self.project_name