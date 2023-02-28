from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField

# from pytils.translit import slugify


# Create your models here.
class Discussion(models.Model):
    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'

    title = models.CharField(max_length=200,
                             help_text='no more than 200 characters',
                             db_index=True)
    content = RichTextField(blank=True,
                            null=True, help_text='no more than 5000 characters',
                            max_length=5000)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    likes_discussion = models.ManyToManyField(User, related_name='discussion_like',
                                              blank=True, verbose_name='Likes')
    saves_discussions = models.ManyToManyField(User, related_name='blog_discussion_save',
                                               blank=True, verbose_name="User's saved posts")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussion(self):
        return self.likes.count()

    def total_saves_discussions(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
