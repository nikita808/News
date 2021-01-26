from django.forms import ModelForm

from .models import News


class PostForm(ModelForm):
    class Meta:
        model = News
        fields = ['created_at', 'headline', 'body', 'pic_src_link']
