from django import forms
from django.forms import ModelForm
from .models import *


class places_import_form(forms.Form):
    file_path = forms.FileField()

# class places_new_form(forms.Form):
#     place_name = forms.CharField(max_length=100)
#     place_id = forms.CharField(max_length=4)
#     place_awesome = forms.BooleanField(required=False)
#     place_email = forms.EmailField()
#     place_desc = forms.CharField(widget=forms.Textarea)


class place_model_form(ModelForm):
    class Meta:
        model = Place
        fields = ['name','number','address_line1','address_line2','city','state','zip']
            # fields = '__all__'
            # exclude = ['title']


class group_model_form(ModelForm):
    class Meta:
        model = Group
        fields = ['name']
            # fields = '__all__'
            # exclude = ['title']


class link_model_form(ModelForm):
    class Meta:
        model = Link
        fields = ['name','description','urly']
            # fields = '__all__'
            # exclude = ['title']


class note_model_form(ModelForm):
    class Meta:
        model = Note
        fields = ['name','note_text']
            # fields = '__all__'
            # exclude = ['title']


class kb_model_form(ModelForm):
    class Meta:
        model = KbArticle
        fields = ['name','description','Kb_text']
            # fields = '__all__'
            # exclude = ['title']name = models.CharField(max_length=200)


class thing_model_form(ModelForm):
    class Meta:
        model = Thing
        fields = ['name','model_num']
            # fields = '__all__'
            # exclude = ['title']


class company_model_form(ModelForm):
    class Meta:
        model = Company
        fields = ['name']
            # fields = '__all__'
            # exclude = ['title']


class department_model_form(ModelForm):
    class Meta:
        model = Department
        fields = ['name','place']
            # fields = '__all__'
            # exclude = ['title']
