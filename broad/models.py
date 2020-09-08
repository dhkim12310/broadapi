from django.db                  import models
from django.contrib.auth.models import User

class Broad(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    description = models.TextField()
    hits = models.PositiveIntegerField(default = 0)
    image = models.ImageField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        def __str__(self):
            return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    broad = models.ForeignKey(Broad, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        def __str__(self):
            return self.comment


