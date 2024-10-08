from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "coquetteness"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)

    def clean_coquetteness(self):
        coquetteness = self.cleaned_data.get('coquetteness')
        return strip_tags(coquetteness)