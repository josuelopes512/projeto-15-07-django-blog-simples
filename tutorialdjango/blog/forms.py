from blog.models import Post
from django.forms import ModelForm

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'slug', 'author','body']
        prepopulated_fields = {"slug": ("title",)}
