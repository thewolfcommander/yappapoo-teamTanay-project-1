from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class CommonInfo(models.Model):
    """
    Common info for models in which some fields are common
    """
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Category(CommonInfo):
    """
    This model is for containing product categories
    """
    image = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.name)

    
class Seller(models.Model):
    """
    This model is for seller profile
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    postal = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.company_name)

    
class Product(CommonInfo):
    """
    This model is for containing product itself
    """
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name="product_category")
    gross_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    shipping = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    tax = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)


    def __str__(self):
        return "{} - {}".format(str(self.id), self.name)


class ProductImage(models.Model):
    """
    Model to handle multiple images of Products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.product.name)

    
class ProductSizes(models.Model):
    """
    Model to handle multiple sizes available for the Product
    """
    SIZE = [
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('XXXXL', 'XXXXL'),
        ('XXXXXL', 'XXXXXL')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=25, choices=SIZE, default='S')
    available = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(str(self.product.id), self.size)


class ProductReview(models.Model):
    """
    Model to handle the review of the products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.product.name, str(self.rating))

    def is_positive(self):
        """
        To identify the positive and negative reviews for the products
        """
        if rating > 3.5:
            return True
        else:
            return False
