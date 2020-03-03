from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/listings/' + listing_id)
        contact1 = Contact(listing_id=listing_id, listing=listing, name=username, email=email, phone=phone, message=message, user_id=user_id)
        contact1.save()
        #send mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign in to the admin portal for more info',
            'sadbhavanahk@gmail.com',
            [realtor_email, 'sadbhavanahk@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your request has been submitted...The realtor will get bac to you soon')
        return redirect('/listings/'+listing_id)