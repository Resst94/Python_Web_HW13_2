from django import forms
from .models import Quote, Author, Tag


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}))
    author = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by("fullname"),
        empty_label="Select author",
        to_field_name='fullname',
        widget=forms.Select(attrs={"class": "form-select"}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by("name"),
        widget=forms.SelectMultiple(attrs={"size": "7"}),
        required=False)
    new_tags = forms.CharField(required=False, max_length=30)

    class Meta:
        model = Quote
        fields = ["quote", "author", "tags", "new_tags"]


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    born_date = forms.CharField(max_length=64, help_text="Please follow the format: December 25, 2000.",
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    born_location = forms.CharField(max_length=256, help_text="Please follow the format: in Florida, USA.",
                                    widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.Textarea(attrs={"class": "form-control"})

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
