from django.db import models
from django.utils.text import slugify


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Member, related_name='teams')
    leader = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='leader_teams')
    image = models.ImageField(upload_to='teams/')
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)


def load_members():
    with open('members.csv') as f:
        for line in f:
            id, first_name, last_name = line.strip().split(',')
            Member.objects.create(first_name=first_name, last_name=last_name)
            print(f"Created member {first_name} {last_name}")
        print("""
            ########################################################
            ###         Members loaded successfully!             ###
            ########################################################
        """)