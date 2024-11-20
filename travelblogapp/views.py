from django.shortcuts import render
import razorpay
from.models import *

# Create your views here.

def welcomepage(request):
    return render (request,'welcome.html')

def loginpage1(request):
    return render(request,'login.html')

def registerpage1(request):
    return render (request,'register.html')

def loginpage2(request):
    return render(request,'login.html')

def homepage1(request):
    return render(request,'home.html')


def reg(request):
    if request.method=='POST':
        name1=request.POST['username']
        email1=request.POST['email']
        password1=request.POST['password']
        x=blog(Username=name1,Password=password1)
        x.save()
        user.objects.create(LOGIN=x,Email=email1,Username=name1)
        return render(request,'login.html')
    else:
        return render(request,'register.html')


def login1(request):
    if request.method=='POST':
        name1=request.POST['user']
        password1=request.POST['pass']
        res=blog.objects.filter(Username=name1,Password=password1)
        if res.exists():
            return render(request,'home.html')
    return render (request,'login.html')

def kozhikodepage(request):
    return render (request,'kozhikodepage1.html')

def wayanadpage(request):
    return render(request,'wayanadpage1.html')

def munnarpage(request):
    return render(request,'munnarpage1.html')

def kozhikodebeachpage(request):
    return render(request, 'beach.html')

def sarovaramparkpage(request):
    return render(request,'sarovarampark.html')

def smstreetpage(request):
    return render(request,'smstreet.html')

def chembrapeakpage(request):
    return render(request,'chembrapeak.html')

def meenmuttypage(request):
    return render(request,'meenmutty.html')
def forestpage(request):
    return render(request,'forest.html')

def anaimudipage(request):
    return render(request,'anaimudipage.html')

def aboutpage(request):
    return render(request,'aboutpage.html')

def contactpage(request):
    return render(request,'contact.html')

def familypackagepage(request):
    return render(request,'familypackage.html')

def bachelorpackagepage(request):
    return render(request,'bachelorpage.html')

def bachelor_package(request):
    if request.method == 'POST':
        fullname = request.POST['fullname2']
        email = request.POST['email2']
        phone_number = request.POST['phonenumber2']
        check_in = request.POST['checkin2']
        check_out = request.POST['checkout2']
        room_type = request.POST['room2']
        guests = request.POST['guests2']
        special_request = request.POST['specialrequest2']

        # Create a new BachelorPackage entry
        v= BachelorPackage.objects.create(
            Fullname=fullname,
            Email=email,
            Phonenumber=phone_number,
            Checkin=check_in,
            Checkout=check_out,
            Roomtype=room_type,
            Numberofguest=guests,
            Specialrequest=special_request
        )
        v.save()
        # Add success message
        context = {'key': 'Booking Successfully'}
        return render(request, 'bachelorpage.html', context)


# Example of form handling
def add_view(request):
    if request.method == 'POST':
        # Handle the POST request (e.g., form data processing)
        return render(request, 'add_page.html', {'message': 'Form Submitted'})
    else:
        # Handle the GET request (e.g., display the form)
        return render(request, 'add_page.html')
    

def bookcalicutpage(request):
    return render (request,'bookcalicut.html')


def calicut_book(request):
    cfullname = request.POST['cname']
    cemail = request.POST['cemail']
    cphone = request.POST['cphone']
    ctrip_date = request.POST['ctrip-date']
    cnum_travelers = request.POST['cnum-travelers']
    cspecial_request = request.POST['cspecial']


    calicut_book_data = calicutbook.objects.create(
        cFullname = cfullname,
        cEmail = cemail,
        cPhonenumber = cphone,
        cTripdate = ctrip_date,
        cTravelers = cnum_travelers,
        cSpecialrequest = cspecial_request,

    )
    calicut_book_data.save()
    context = {'key': 'Booking Successfully'}
    return render(request, 'bookcalicut.html', context)


def bookwayandpage(request):
    return render(request,'bookwayanad.html')


def bookmunnarpage(request):
    return render (request,'bookmunnar.html')

def paymentpage(request):
    return render (request,'payment.html')

def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount=500

        client = razorpay.Client(
            auth=("rzp_test_JAeLcxoJpwFjEq", "Pvj0eaEQA5b2gH4XHxEGEhMB")
        )
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture':'1'})
        return render(request,'payment.html')