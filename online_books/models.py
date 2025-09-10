from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# دسته‌بندی کتاب
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # دسته‌بندی‌ها یکتا باشند

    def __str__(self):
        return self.name


# کتاب
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")

    def __str__(self):
        return f"{self.title} - {self.author}"


# پروفایل کاربر و علاقه‌مندی‌ها
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book, blank=True, related_name='fans')

    def __str__(self):
        return self.user.username


# سیگنال برای ساخت پروفایل کاربر به محض ثبت‌نام
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
