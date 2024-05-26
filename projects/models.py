from django.db import models
from uuid import uuid4


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    total_votes = models.IntegerField(default=0, blank=True, null=True)
    votes_ratio = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_types = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    # owner =
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, choices=review_types)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name
