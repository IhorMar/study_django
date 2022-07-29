from .models import *
from django import forms
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category'

    class Meta:
        model = Women
        fields = ['title',
                  'slug',
                  'content',
                  'photo',
                  'is_published',
                  'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Len to mach')
        return title
