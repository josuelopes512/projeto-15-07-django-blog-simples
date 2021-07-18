from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ("-created",)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        # instance.slug = unique_slug_generator(instance)

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     slug = slugify(instance.title)
#     exists = Post.objects.filter(slug=slug).exists()
#     if exists:
#         slug = "%s-%s" %(slug, instance.id)
#     instance.slug = slug
#     # if not instance.slug:
#     #     # instance.slug = create_slug(instance)
#     #     instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)