from django import forms
from .models import BsBoard

class BoardCreateForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label='제목'
    )
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    # validation
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')