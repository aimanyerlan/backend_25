from django.db import models

# Create your models here.
class Thread(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    # class Meta:
    #     verbose_name_plural = 'Threads'
    #     verbose_name = 'Thread'

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    picture = models.FileField(upload_to='media/')
    description = models.TextField()
    author = models.CharField(max_length=250)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name_plural = 'Posts'
    #     verbose_name = 'Post'
        
    def __str__(self):
        return self.title