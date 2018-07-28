from django.db import models

# Create your models here.
class NewClientOrder(models.Model):
    CliOID = models.CharField(max_length=5)
    Side = models.CharField(max_length=10)
    Symbol = models.CharField(max_length=10)
    Qty = models.CharField(max_length=100)
    Dest = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)
    Tif = models.CharField(max_length=10)
    Otyp = models.CharField(max_length=10)
    FixTags = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return "CliOID = " + str(self.CliOID)


class CreateMergeOrder(models.Model):
    MergeOID = models.CharField(max_length=5)
    CliOIDs = models.CharField(max_length=100)

    def __str__(self):
        return "MergeOID  = " + str(self.MergeOID)

class NewStreetOrder(models.Model):
    CliOrder = models.ForeignKey(NewClientOrder, on_delete=models.CASCADE, blank=True, null=True)
    MergeOrder = models.ForeignKey(CreateMergeOrder, on_delete=models.CASCADE, blank=True, null=True)
    CLiOID =  models.CharField(max_length=5)
    StrOID = models.CharField(max_length=5)
    Side = models.CharField(max_length=10)
    Symbol = models.CharField(max_length=10)
    Qty = models.CharField(max_length=100)
    Dest = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)
    Tif = models.CharField(max_length=10)
    Otyp = models.CharField(max_length=10)
    FixTags = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return "New Street Order ID = " + str(self.StrOID)

class StreetExecutionReport(models.Model):
    StrOrder = models.ForeignKey(NewStreetOrder, on_delete=models.CASCADE)
    StrOID = models.CharField(max_length=5)
    ExecType = models.CharField(max_length=10)
    Qty = models.CharField(max_length=10000, blank=True, null=True)
    Price = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Street Exec Report" + str(self.ExecType)

class RplStreetOrder(models.Model):
    StrOrder = models.ForeignKey(NewStreetOrder, on_delete=models.CASCADE)
    StrOID =  models.CharField(max_length=5)
    Qty = models.CharField(max_length=10000)
    Price = models.CharField(max_length=100)

    def __str__(self):
        return "replace StrOID : " + str(self.StrOID)





