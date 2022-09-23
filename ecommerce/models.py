from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Address(models.Model):
    type_choice = [
        ("Home", "Home"),
        ("Institute", "Institute"),
        ("Work", "Work"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=150)
    phone_num = models.CharField(max_length=10)
    building_num_name = models.CharField(max_length=250)
    area_colony = models.CharField(max_length=250)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address_type = models.CharField(max_length=100, choices=type_choice, null=True)

    def __str__(self):
        return f"{self.user} ({self.building_num_name}, {self.city})"

    class Meta:
        verbose_name_plural = 'Address'


class Category(models.Model):
    category = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to="CategoryImages", null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name_plural = 'Contact Us'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    category = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} (Qty. {self.quantity}) ({self.product})"

    class Meta:
        verbose_name_plural = 'Cart Items'


class Carousel(models.Model):
    offer = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="CarouselImages")

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = 'Carousel Items'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    gst_id = models.CharField(max_length=15)
    aadhar_number = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = 'Seller'

    def __str__(self):
        val = f"{self.user} (GST: {self.gst_id})"
        return str(val)


class Electronic(models.Model):
    type_choice = [
        ('Audio', 'Audio'),
        ('Cameras', 'Cameras'),
        ('Laptops', 'Laptops'),
        ('Monitors', 'Monitors'),
        ('Tablets', 'Tablets'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="ElectronicImages")
    image2 = models.ImageField(upload_to="ElectronicImages")
    image3 = models.ImageField(upload_to="ElectronicImages")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(Electronic, self).save(*args, **kwargs)

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Electronics'


class Fashion(models.Model):
    type_choice = [
        ('T-Shirts', 'T-Shirts'),
        ('Shirts', 'Shirts'),
        ('Casual Shoes', 'Casual Shoes'),
        ('Formal Shoes', 'Formal Shoes'),
        ('Jeans', 'Jeans'),
        ('Trousers', 'Trousers'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="FashionImages")
    image2 = models.ImageField(upload_to="FashionImages")
    image3 = models.ImageField(upload_to="FashionImages")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(Fashion, self).save(*args, **kwargs)

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Fashion'


class HomeDecor(models.Model):
    type_choice = [
        ('Clocks', 'Clocks'),
        ('Lights', 'Lights'),
        ('Paintings & Posters', 'Paintings & Posters'),
        ('Wall Shelves', 'Wall Shelves'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="HomeDecorImages")
    image2 = models.ImageField(upload_to="HomeDecorImages")
    image3 = models.ImageField(upload_to="HomeDecorImages")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(HomeDecor, self).save(*args, **kwargs)

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Home Decor'


class Mobile(models.Model):
    type_choice = [
        ('Android', 'Android'),
        ('ios', 'ios'),
        ('Symbian', 'Symbian'),
        ('Windows', 'Windows'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="MobileImages")
    image2 = models.ImageField(upload_to="MobileImages")
    image3 = models.ImageField(upload_to="MobileImages")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(Mobile, self).save(*args, **kwargs)

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Mobiles'
