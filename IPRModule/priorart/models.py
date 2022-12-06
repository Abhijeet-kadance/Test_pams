from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from dateutil import parser
from datetime import datetime
from django.core.exceptions import ValidationError
# Create your models here.
class Document(models.Model):
    description = models.TextField(max_length=255,blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    uploaded_at =  models.DateTimeField(auto_now_add=True)

def validate_prior_art_date( self):
    print( parser. parse( self.strftime( "%Y-%m- %d ")). date())
    date_db= parser. parse( self.strftime( "%Y-%m- %d ")). date()
    print(( datetime. now()). date())
    nowdate= datetime. now(). date()
    print( date_db - nowdate )
    if date_db < nowdate:
        print( "date cant")
        raise ValidationError( "Date cannot be in the past")

class PriorArtSearch(models.Model):
    IPR_prior_art_invention_title = models.CharField(max_length=500,null=False,blank=False)
    IPR_prior_art_applicant_name = models.CharField(max_length=200,null=False, blank=False)
    IPR_prior_art_applicant_name_others = models.CharField(max_length=200,null=True, blank=True)
    IPR_prior_art_inventor_name = models.CharField(max_length=250,null=False, blank=False)
    IPR_prior_art_inventor_name_others = models.CharField(max_length=250,null=True, blank=True)
    IPR_prior_art_Invention_description = models.TextField(max_length=8500,null=False, blank=False)
    IPR_prior_art_keywords = models.CharField(max_length=200,null=False, blank=False)
    IPR_prior_art_from_user_email = models.CharField(max_length=150)
    IPR_prior_art_date_received = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    IPR_prior_art_date_replied = models. DateTimeField(
            auto_now= False, auto_now_add= False, null= True, blank= True,
    validators=[ validate_prior_art_date ])
    IPR_prior_art_choices = (
        ( 'Inprocess', 'Inprocess'), ( 'Completed', 'Completed')
        )
    IPR_prior_art_status = models. CharField(
        max_length= 30, choices = IPR_prior_art_choices, default= "Inprocess")
    IPR_prior_art_replied_comments = models.TextField(max_length=8500)
    IPR_prior_art_reply_doc_name =  models.FileField(upload_to='documents/reply/', null=True, blank=True)
    IPR_prior_art_uploaded_doc_name =  models.FileField(upload_to='documents/upload/', null=False, blank=False, validators=[FileExtensionValidator(['pdf','docx']) ])






  