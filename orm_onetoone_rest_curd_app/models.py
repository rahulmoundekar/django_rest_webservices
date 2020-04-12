from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=45)
    mobile = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "person"


class License(models.Model):
    license_number = models.CharField(max_length=45)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    person = models.OneToOneField(Person, unique=True, on_delete=models.CASCADE, primary_key=True, )

    def __unicode__(self):
        return self.licenseNumber

    class Meta:
        db_table = "license"
