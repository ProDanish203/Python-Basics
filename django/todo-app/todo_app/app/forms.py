from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    completed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Todo
        fields = ["title", "description", "completed", "image"]
