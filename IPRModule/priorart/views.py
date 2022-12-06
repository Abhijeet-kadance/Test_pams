import magic
from django.shortcuts import render
from django import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# from IPRModule.priorart.forms import DocumentForm
from .forms import IPR_prior_art_form
from django.contrib import messages

# Create your views here.
# def base(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         #print(uploaded_file_url)
#         return render(request, 'priorart/base.html' , {
#             'uploaded_file_url':uploaded_file_url
#         })
#     return render(request, 'priorart/base.html')

def model_form_upload(request):
    if request.method == "POST":
        form = IPR_prior_art_form(request.POST , request.FILES)
        # request.session['user_email'] = 'test@cdac.in'
        if form.is_valid():
            form.save()
            print("tets is valid")
            return render(request, 'priorart/model_form_upload.html',{
                'form':form
            })
        else:
            print()
            return render(request , 'priorart/model_form_upload.html',{
                'form':form
            })
    else:
        form = IPR_prior_art_form()
        return render(request, 'priorart/model_form_upload.html',{
                'form':form
            })


    # def model_form_upload(request):
    # if request.method == "POST":
    #     form = DocumentForm(request.POST , request.FILES)
          
    #     if form.is_valid():
    #         print(form.cleaned_data['document'])
    #         file = form.cleaned_data.get('IPR_prior_art_uploaded_doc_name', False)
    #         filetype = magic.from_buffer(file.read())
    #         #filetype2 = magic.from_file(file.read(),mime=True)
    #         allowedfiletypes = ['application/pdf','application/zip']
    #         print(filetype)
    #         if not 'PDF' in filetype: 
    #             print("File type not supported")
    #             raise forms.ValidationError('Invalid File Type',code='invalid')
    #         else:
    #             form.save()
    #             print("successfull Submission of form")
    #     else:
    #         form = DocumentForm()
    #         return render(request , 'priorart/model_form_upload.html',{
    #             'form':form
    #         })
    # return render(request, 'priorart/model_form_upload.html')