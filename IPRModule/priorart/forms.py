from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
import re

class IPR_prior_art_form(forms.ModelForm):
    IPR_prior_art_invention_title = forms.CharField(label="Invention Title",max_length=500,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_Invention_description = forms.CharField(label="Invention Description",max_length=8500,widget=forms.Textarea(attrs={'class':'form-control'}))
    IPR_prior_art_applicant_name = forms.CharField(label="Applicant Name",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_applicant_name_others = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_inventor_name = forms.CharField(label="Inventor Title",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_inventor_name_others = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_keywords = forms.CharField(label="Keywords",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    IPR_prior_art_uploaded_doc_name = forms.FileField(label="Upload Document",max_length=500,widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = PriorArtSearch
        fields = ['IPR_prior_art_invention_title',
                  'IPR_prior_art_Invention_description', 
                  'IPR_prior_art_applicant_name',
                  'IPR_prior_art_applicant_name_others',
                  'IPR_prior_art_inventor_name',
                  'IPR_prior_art_inventor_name_others',
                  'IPR_prior_art_keywords',
                  'IPR_prior_art_uploaded_doc_name',
        ]
       

    def clean_IPR_prior_art_invention_title(self):
        super(IPR_prior_art_form, self).clean()
        IPR_prior_art_invention_title = self.cleaned_data.get('IPR_prior_art_invention_title')

        if IPR_prior_art_invention_title is None or len(IPR_prior_art_invention_title) < 4:
            print("inside Clean Method validation")
            raise forms.ValidationError("Error in IPR_prior_art_invention_title",code="IPR_prior_art_invention_title")

        elif(True):
            Name_regex = "^[a-zA-Z!-,.()]+([\s][a-zA-Z!-,.()]+)*$"
            pattern = re.compile(Name_regex)
            valid_Name = re.search(pattern, IPR_prior_art_invention_title)
            if valid_Name is None:
                raise forms.ValidationError("Title is not valid ",code="IPR_prior_art_invention_title")
        
        return IPR_prior_art_invention_title

        
    def clean_IPR_prior_art_Invention_description(self):
        super(IPR_prior_art_form, self).clean()
        IPR_prior_art_Invention_description = self.cleaned_data.get('IPR_prior_art_Invention_description')

        if IPR_prior_art_Invention_description is None or len(IPR_prior_art_Invention_description) < 4:
            print("inside Clean Method validation")
            raise forms.ValidationError("Error in IPR_prior_art_invention_title",code="IPR_prior_art_Invention_description")
        
        elif(True):
            Description_regex = "^[0-9]*[a-zA-Z]+[a-zA-Z0-9! \r\n &()+@%\-=\[\] {} ;': \\ |,.<>/?]*$"
            pattern = re.compile(Description_regex)
            valid_Name = re.search(pattern, IPR_prior_art_Invention_description)
            if valid_Name is None:
                raise forms.ValidationError("Enter a valid Description",code="IPR_prior_art_Invention_description")
        return IPR_prior_art_Invention_description

        

    def clean_IPR_prior_art_applicant_name(self):
        IPR_prior_art_applicant_name = self.cleaned_data['IPR_prior_art_applicant_name']
        #Name_regex = re.compile('/^[A-Za-z][A-Za-z\'\-]+([\ A-Za-z][A-Za-z\'\-]+)*/')
        if IPR_prior_art_applicant_name is None or len(IPR_prior_art_applicant_name) < 2:
            raise forms.ValidationError("Name should have 2 or more characters.")
        elif(True):
            Name_regex = "^[a-zA-Z]+([\s][a-zA-Z]+)*$"
            pattern = re.compile(Name_regex)
            valid_Name = re.search(pattern, IPR_prior_art_applicant_name)
            if valid_Name is None:
                raise forms.ValidationError("Name is not valid ",code="IPR_prior_art_applicant_name")
        
        return IPR_prior_art_applicant_name 

    def clean_IPR_prior_art_applicant_name_others(self):

        IPR_prior_art_applicant_name_others = self.cleaned_data['IPR_prior_art_applicant_name_others']
        print(IPR_prior_art_applicant_name_others)

        #Keyword_REGEX = re.compile('/^(([a-zA-Z0-9 ](,)?)*)+$/')
        
        if IPR_prior_art_applicant_name_others is None :
            raise forms.ValidationError("There must be atleast 1 keyword")
        
        elif(True):
            Keyword_REGEX = "^(([a-zA-Z0-9 ](,)?)*)+$"
            key_pattern = re.compile(Keyword_REGEX)
            valid_Keywords = re.search(key_pattern,IPR_prior_art_applicant_name_others)
            print(valid_Keywords)
            if valid_Keywords is None:
                raise forms.ValidationError("Multiple applicant names should be entered in comma seprated way.",code="IPR_prior_art_applicant_name_others")

        return IPR_prior_art_applicant_name_others


    def clean_IPR_prior_art_inventor_name(self):
        IPR_prior_art_inventor_name = self.cleaned_data['IPR_prior_art_inventor_name']
        #Name_regex = re.compile('/^[A-Za-z][A-Za-z\'\-]+([\ A-Za-z][A-Za-z\'\-]+)*/')
        if IPR_prior_art_inventor_name is None or len(IPR_prior_art_inventor_name) < 2:
            raise forms.ValidationError("Name should have 2 or more characters.")
        elif(True):
            Name_regex = "^[a-zA-Z]+([\s][a-zA-Z]+)*$"
            pattern = re.compile(Name_regex)
            valid_Name = re.search(pattern, IPR_prior_art_inventor_name)
            if valid_Name is None:
                raise forms.ValidationError("Name is not valid ",code="IPR_prior_art_inventor_name")
        
        return IPR_prior_art_inventor_name 
    
    def clean_IPR_prior_art_inventor_name_others(self):

        IPR_prior_art_inventor_name_others = self.cleaned_data['IPR_prior_art_inventor_name_others']
        print(IPR_prior_art_inventor_name_others)

        #Keyword_REGEX = re.compile('/^(([a-zA-Z0-9 ](,)?)*)+$/')
        
        if IPR_prior_art_inventor_name_others is None :
            raise forms.ValidationError("There must be atleast 1 keyword")
        
        elif(True):
            Keyword_REGEX = "^(([a-zA-Z0-9 ](,)?)*)+$"
            key_pattern = re.compile(Keyword_REGEX)
            valid_Keywords = re.search(key_pattern,IPR_prior_art_inventor_name_others)
            print(valid_Keywords)
            if valid_Keywords is None:
                raise forms.ValidationError("Multiple Inventor names should be entered in comma seprated way.",code="IPR_prior_art_inventor_name_others")

        return IPR_prior_art_inventor_name_others

    def clean_IPR_prior_art_uploaded_doc_name(self):
        MAX_UPLOAD_SIZE = 2621440 #2.5 mb
        IPR_prior_art_uploaded_doc_name = self.cleaned_data['IPR_prior_art_uploaded_doc_name']
        print(IPR_prior_art_uploaded_doc_name.size)
        if IPR_prior_art_uploaded_doc_name.size > MAX_UPLOAD_SIZE:
            print("Size Exceeded")
            raise forms.ValidationError("File Size Not Satisfied. Must be less than 2 Mb",code="IPR_prior_art_uploaded_doc_name")
        print(IPR_prior_art_uploaded_doc_name)

        return IPR_prior_art_uploaded_doc_name

    def clean_IPR_prior_art_keywords(self):

        IPR_prior_art_keywords = self.cleaned_data['IPR_prior_art_keywords']
        print(IPR_prior_art_keywords)

        #Keyword_REGEX = re.compile('/^(([a-zA-Z0-9 ](,)?)*)+$/')
        
        if IPR_prior_art_keywords is None :
            raise forms.ValidationError("There must be atleast 1 keyword")
        
        elif(True):
            Keyword_REGEX = "^(([a-zA-Z0-9 ](,)?)*)+$"
            key_pattern = re.compile(Keyword_REGEX)
            valid_Keywords = re.search(key_pattern,IPR_prior_art_keywords)
            print(valid_Keywords)
            if valid_Keywords is None:
                raise forms.ValidationError("Keywords should be entered in comma seprated way.",code="IPR_prior_art_keywords")

        return IPR_prior_art_keywords
                                        


    # def clean_IPR_prior_art_invention_title(self, *args, **kwargs):
    #     invention_title = self.cleaned_data.get("IPR_prior_art_invention_title")
    #     if len(invention_title) < 4:
    #         print("no")
    #         raise forms.ValidationError( "Title Length is Too Small", code='invalid')
    #     return invention_title
           