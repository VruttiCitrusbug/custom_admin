# -*- coding: utf-8 -*-
from django import forms

from core.models import ReviewCategory,ModelYear,BikeClass,FrameType,BreakType,WheelSize,BikeClass
import re

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
    # year = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'id':'aaa'}))
    
    class Meta:
        model = ModelYear
        fields = ['year']
        labels = {
            "year": "year"
        }

    def clean(self):
        cleaned_data = super(YearCreationForm, self).clean()
        year = cleaned_data.get("year")

        if not year:
            raise forms.ValidationError("Please enter valid year.")

        count = 0
        num=year
        while num != 0:
            num //= 10
            count += 1
        if count != 4:
                raise forms.ValidationError("Please enter valid year")
    # def __init__(self, *args, **kwargs):
    #     super(YearCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['year'].widget.attrs['id'] = 'aaa'
    def __init__(self, *args, **kwargs):
        super(YearCreationForm, self).__init__(*args, **kwargs)
        self.fields['year'].required = False
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'iiiiiiiiiiii'
            
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         if not field:
    #             self.fields[field].widget.attrs.update({'class': 'form-control'})
    #         self.fields['year'].widget.attrs.update({'autofocus': 'autofocus'})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:

            # if not field:
            #     self.fields[field].widget.attrs.update({'class': 'form-control'})
            #     print("***************************************************************************************************************{}".format(self.fields[field].widget.attrs.update({'class': 'form-control'})))
            # self.fields['year'].widget.attrs.update({'autofocus': 'autofocus'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance

class BikeClassCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    bike_class = forms.CharField()

    class Meta:
        model = BikeClass
        fields = ['bike_class']
        labels = {
            "bike_class": "bike_class"
        }

    def clean(self):
        cleaned_data = super(BikeClassCreationForm, self).clean()
        bike_class = cleaned_data.get("bike_class")

        if not bike_class:
            raise forms.ValidationError("This Field is Require.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance

class FrameTypeCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    frame_type = forms.CharField()

    class Meta:
        model = FrameType
        fields = ['frame_type']
        labels = {
            "bike_class": "bike_class"
        }

    def clean(self):
        cleaned_data = super(FrameTypeCreationForm, self).clean()
        frame_type = cleaned_data.get("frame_type")

        if not frame_type:
            raise forms.ValidationError("This Field is Require.")
        if re.match(r'^[0-9]+$',frame_type):
                raise forms.ValidationError("only alphabelts are allowed")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance
class BreakTypeCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    break_type = forms.CharField()

    class Meta:
        model = BreakType
        fields = ['break_type']
        labels = {
            "break_type": "break_type"
        }

    def clean(self):
        cleaned_data = super(BreakTypeCreationForm, self).clean()
        break_type = cleaned_data.get("break_type")

        if not break_type:
            raise forms.ValidationError("This Field is Require.")
        if not re.match(r'^[A-za-z]+$',break_type):
                raise forms.ValidationError("only alphabelts are allowed")
    def __init__(self, *args, **kwargs):
        super(BreakTypeCreationForm, self).__init__(*args, **kwargs)
        self.fields['break_type'].required = False

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance

class WheelSizeCreationForm(forms.ModelForm):
    """Custom ReviewCategory"""
    break_type = forms.CharField()

    class Meta:
        model = WheelSize
        fields = ['wheel_size']
        labels = {
            "wheel_size": "wheel_size"
        }

    def clean(self):
        cleaned_data = super(WheelSizeCreationForm, self).clean()
        wheel_size = cleaned_data.get("wheel_size")

        if not wheel_size:
            raise forms.ValidationError("This Field is Require.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance

# class YearCreationForm(forms.ModelForm):
#   
#     year = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'aaa'}))
    
#     class Meta:
#         model = ModelYear
#         fields = ['year']
#         labels = {
#             "year": "year"
#         }

#     def clean(self):
#         cleaned_data = super(YearCreationForm, self).clean()
#         year = cleaned_data.get("year")

#         if not year:
#             raise forms.ValidationError("Please enter valid year.")

#         count = 0
#         num=year
#         while num != 0:
#             num //= 10
#             count += 1
#         if count != 4:
#                 raise forms.ValidationError("Please enter valid year")

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if commit:
#             instance.save()

#         return instance

class YearChangeForm(forms.ModelForm):
    
    class Meta:
        model = ModelYear
        fields = ['year']
        labels = {
            "Year": "year"
        }
    def clean(self):
        cleaned_data = super(YearChangeForm, self).clean()
        year = cleaned_data.get("year")
        if not year:
            raise forms.ValidationError("Please enter year.")
        count = 0
        num=year
        while num != 0:
            num //= 10
            count += 1
        if count != 4:
                raise forms.ValidationError("Please enter valid year")
        if num <1853 :
            raise forms.ValidationError("enter value greater equal to 1853")
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class BreakTypeChangeForm(forms.ModelForm):
    """Custom form to change ReviewCategory"""
    # meta_title = forms.CharField(required=True, label='Meta Title', widget=forms.TextInput(attrs={'placeholder': '| ElectricBikeReview.com', 'readonly': True}))

    class Meta:
        model = BreakType
        fields = ['break_type']
        labels = {
            "break_type": "break_type"
        }
    def clean(self):
        cleaned_data = super(BreakTypeChangeForm, self).clean()
        break_type = cleaned_data.get("break_type")

        if not break_type:
            raise forms.ValidationError("This Field is Require.")

        if not re.match(r'^[A-Za-z]+$',break_type):
                raise forms.ValidationError("only alphabelts are allowed")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class FrameTypeChangeForm(forms.ModelForm):

    class Meta:
        model = FrameType
        fields = ['frame_type']
        labels = {
            "frame_type": "frame_type"
        }
    def clean(self):
        cleaned_data = super(FrameTypeChangeForm, self).clean()
        frame_type = cleaned_data.get("frame_type")

        if not frame_type:
            raise forms.ValidationError("This Field is Require.")
        if re.match(r'^[0-9]+$',frame_type):
                raise forms.ValidationError("only alphabelts are allowed")
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class WheelSizeChangeForm(forms.ModelForm):

    class Meta:
        model = WheelSize
        fields = ['wheel_size']
        labels = {
            "wheel_size": "wheel_size"
        }
    def clean(self):
        cleaned_data = super(WheelSizeChangeForm, self).clean()
        wheel_size = cleaned_data.get("wheel_size")

        if not wheel_size:
            raise forms.ValidationError("This Field is Require.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class BikeClassChangeForm(forms.ModelForm):

    class Meta:
        model = BikeClass
        fields = ['bike_class']
        labels = {
            "bike_class": "bike_class"
        }
    def clean(self):
        cleaned_data = super(BikeClassChangeForm, self).clean()
        bike_class = cleaned_data.get("bike_class")

        if not bike_class:
            raise forms.ValidationError("This Field is Require.")
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance