from .models import News
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ['created_at', 'headline', 'body', 'pic_src_link']
