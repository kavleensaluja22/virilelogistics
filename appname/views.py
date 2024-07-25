from django.shortcuts import render
from .models import Reach
# Create your views here.
from .forms import ReachModelForm
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse , HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ReachModelForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            #form_instance = form.save()

            # Send an email to the owner
            subject = 'New Contact Form Submission'
            message = f'Name: {name}\nEmail: {email}\nComment: {comment}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['virilelogistics@gmail.com']  # Replace with the owner's email address

            _email = send_mail(subject, message, from_email, recipient_list)
            print(_email)

        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = ReachModelForm()
    return render(request, 'contact.html', {'form': form})



def base(request):
    return render(request,'base.html')
def helpmore(request):
    return render(request,'helpmore.html')
def service(request):
    return render(request,'service.html')
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactFormModelForm
from .forms import ContactFormModelForm

@csrf_exempt
def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send email to owner
            subject = 'New Contact Form Submission'
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            MC Number: {form.cleaned_data['mc_number']}
            Query: {form.cleaned_data['query']}
            Preferred Contact Method: {form.cleaned_data['contact_method']}
            """
            
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['virilelogistics@gmail.com']
            
            _email = send_mail(subject, message, from_email, recipient_list)
            print(_email)
            
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})










