from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label="", required=False, max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'type': 'search',
            'placeholder': '名前や都道府県名など',
            'aria-label': 'Search',
        })
    )

class UploadForm(forms.Form): # アップロードフォーム
    file = forms.FileField(required=True, label='',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'customFile',
        })
    )