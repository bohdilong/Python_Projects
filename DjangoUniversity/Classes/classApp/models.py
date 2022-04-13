from django.db import models

# creating a class to create objects with the same layout
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, blank=True)
    courseNum = models.IntegerField(max_length=60, blank=True, default="", null=False)
    instructorName = models.CharField(max_length=60, blank=True, default="", null=False)
    duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)

    objects = models.Manager()
    # this will present each object in the database using the title of the course
    def __str__(self):
        return self.title
