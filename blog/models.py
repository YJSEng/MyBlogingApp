from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                     .filter(status=Post.Status.PUBLISHED)
    
# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'

    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique_for_date='publish')
    body=models.TextField()
    author = models.CharField(max_length=80)
    email = models.EmailField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
   # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    image = models.ImageField(upload_to='products/')

    objects = models.Manager() # The default manager.
    published = PublishedManager()
    def save(self, *args, **kwargs):
        # Auto-generate slug from title if it's not already set
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            # Ensure slug uniqueness by appending a number if needed
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]


    def __str__(self) :
        return self.title.title()
    def get_absolute_url(self):
        return reverse("blog:post_detail",args=[self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug])
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    