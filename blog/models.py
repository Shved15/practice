from datetime import timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField


# model of post
class Post(models.Model):
    # meta options

    class Meta:
        verbose_name = 'Create post'
        verbose_name_plural = 'Create posts'

    title = models.CharField(max_length=200,
                             db_index=True,
                             help_text="no more than 200 characters",
                             verbose_name='Write a title')
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text="no more than 5000 characters")
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="no more than 5000 characters")
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    likes_post = models.ManyToManyField(User, related_name='post_likes', blank=True, verbose_name='Likes')
    saves_posts = models.ManyToManyField(User, related_name='blog_posts_save', blank=True, verbose_name="User's saved posts")
    # reply = models.ForeignKey('self', null=True,  related_name='reply_ok', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes_post.count()

    def total_saved_posts(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

# @receiver(pre_save, sender=Post)
# def prepopulated_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.title)
