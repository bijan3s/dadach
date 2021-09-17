from django.db import models

# Create your models here.

class part_model(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "parts"
        verbose_name="parts"

    def __str__(self):
        return (self.name.capitalize())

class exercises_model(models.Model):
    name = models.CharField(max_length=200)
    part=models.ForeignKey(part_model,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='exercises/')
    description = models.TextField()

    class Meta:
        verbose_name_plural = "exercises"
        verbose_name="exercises"

    def __str__(self):
        return self.name

parts=['abs','chest','shoulders','back','arms','legs','cardio']





    
