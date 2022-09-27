# -*- coding: utf-8 -*-
from django import forms

from core.models import ReviewCategory,ModelYear


# -----------------------------------------------------------------------------
# ReviewCategory
# -----------------------------------------------------------------------------
class ReviewCategoryCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    slug = forms.CharField(required=False)
    meta_title = forms.CharField(required=True, label='Meta Title', widget=forms.TextInput(attrs={'placeholder': '| ElectricBikeReview.com', 'readonly': True}))

    class Meta:
        model = ReviewCategory
        fields = ['name', 'slug', 'meta_title', 'description', 'short_description', 'parent_category', 'category_image_full', 'icon_image', 'status', 'featured_review']
        labels = {
            "parent_category": "Parent Category",
            "featured_review": "Featured Review",
            "category_image_full": "Category Image",
            "description": "Long Description",
            "short_description": "Short Description(Meta Tags)",
            "icon_image": "Icon Image",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['category_image_full', 'icon_image']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean(self):
        cleaned_data = super(ReviewCategoryCreationForm, self).clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        category_image_full = cleaned_data.get("category_image_full")

        if not name:
            raise forms.ValidationError("Please enter name.")

        if not description:
            raise forms.ValidationError("Please enter description.")

        if category_image_full:
            if category_image_full.size > 15097152:
                raise forms.ValidationError("Please select image below 15 mb!")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance


class ReviewCategoryChangeForm(forms.ModelForm):
    """Custom form to change ReviewCategory"""
    meta_title = forms.CharField(required=True, label='Meta Title', widget=forms.TextInput(attrs={'placeholder': '| ElectricBikeReview.com', 'readonly': True}))

    class Meta:
        model = ReviewCategory
        fields = ['name', 'slug', 'meta_title', 'description', 'short_description', 'parent_category', 'category_image_full', 'icon_image', 'status', 'featured_review']
        labels = {
            "parent_category": "Parent Category",
            "featured_review": "Featured Review",
            "category_image_full": "Category Image",
            "description": "Long Description",
            "short_description": "Short Description(Meta Tags)",
            "icon_image": "Icon Image",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['category_image_full', 'icon_image']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean(self):
        cleaned_data = super(ReviewCategoryChangeForm, self).clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        category_image_full = cleaned_data.get("category_image_full")

        if not name:
            raise forms.ValidationError("Please enter name.")

        if not description:
            raise forms.ValidationError("Please enter description.")

        if category_image_full:
            if category_image_full.size > 15097152:
                raise forms.ValidationError("Please select image below 15 mb!")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance



 # change forms

class YearCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    year = forms.IntegerField()

    class Meta:
        model = ModelYear
        fields = ['year']
        labels = {
            "year": "year"
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         # if field not in ['category_image_full', 'icon_image']:
    #         #     self.fields[field].widget.attrs.update({'class': 'form-control'})
    #         self.fields['year'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean(self):
        cleaned_data = super(YearCreationForm, self).clean()
        year = cleaned_data.get("year")
        # description = cleaned_data.get("description")
        # category_image_full = cleaned_data.get("category_image_full")

        if not year:
            raise forms.ValidationError("Please enter year.")

        # if not description:
        #     raise forms.ValidationError("Please enter description.")

        if len(year) != 4:
                raise forms.ValidationError("Please enter valid year")
        # if len(year) != 4:
        #         raise forms.ValidationError("Please enter valid year")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance
