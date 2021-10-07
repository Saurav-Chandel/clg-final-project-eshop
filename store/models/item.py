from django.db import models

# Create your models here.
class Item(models.Model):  #inherit models in class product.
    product_id = models.AutoField  #An IntegerField that automatically increments according to available IDs.
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/shop/images",default="")
    price = models.IntegerField(default=0)

    description = models.CharField(max_length=200, default='', null=True, blank=True)



    def __str__(self):
        return self.product_name