from django.db import models

# Create your models here.
class Project(models.Model):
    project_name= models.CharField(max_length=25)

    class Meta:
        db_table = 'Project'

    def __str__(self):
        return self.project_name


class process_file_repo(models.Model):
    # project_name=models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    project_name = models.CharField(max_length=25)
    process_name=models.CharField(max_length=25,unique=True)
    from_date=models.DateField()
    to_date=models.DateField()
    to_time=models.TimeField(auto_now=False, auto_now_add=False)
    project_file=models.TextField()

    class Meta:
        db_table = 'process_file_repo'

    def __str__(self):
        return self.project_name