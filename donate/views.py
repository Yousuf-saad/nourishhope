from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request,'index.html')

def user_home(request):
    return render(request,'user_home.html')

def ngo_home(request):
    return render(request,'ngo_home.html')

def admin_home(request):
    return render(request,'admin_home.html')

def user_reg(request):
    if request.method=='POST':
        usr=reg_form(request.POST)
        passwrd=log_form(request.POST)
        if usr.is_valid() and passwrd.is_valid():
            login_data=passwrd.save(commit=False)
            login_data.user_type='donor'
            login_data.save()
            reg_data=usr.save(commit=False)
            reg_data.login_id=login_data
            reg_data.save()
            return redirect('login')
    else:
        usr=reg_form()
        passwrd=log_form()
        return render(request,'register.html',{'users':usr,'passwrd':passwrd})

def logins(request):
    if request.method=='POST':
        form=login_verify(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=login.objects.get(email=email)
                if user.password == password:
                    if user.user_type == 'donor':
                        request.session['donor_id'] = user.id
                        return redirect('users_home')
                    elif user.user_type =='NGO':
                        request.session['ngo_id'] =user.id
                        return redirect('ngos_home')
                    elif user.user_type=='admin':
                        request.session['admin_id']=user.id
                        return redirect('admins')
                else:
                    messages.error(request,'Invalid password')
            except login.DoesNotExist:
                messages.error(request,'User Does not Exist')
    else:
        form=login_verify()
    return render(request,'login.html',{'form':form})

def logout(request):
    request.session.flush()
    return redirect('login')

def donor_profile(request):
    donr_id=request.session.get('donor_id')
    donr_login_data=get_object_or_404(login,id=donr_id)
    donr_data=get_object_or_404(user,login_id=donr_login_data)
    if request.method=='POST':
        form=user_edit_form(request.POST,instance=donr_data)
        logform=log_edit_form(request.POST,instance=donr_login_data)
        if form.is_valid() and logform.is_valid():
            form.save()
            logform.save()
            return redirect('users_home')
    else:
        form=user_edit_form(instance=donr_data)
        logform=log_edit_form(instance=donr_login_data)
    return render(request,'user_edit.html',{'forms':form,'logform':logform})

def donate(request):
    donr_id=request.session.get('donor_id')
    donr_login_data=get_object_or_404(login,id=donr_id)
    if request.method=='POST':
        donation=donation_form(request.POST)
        if donation.is_valid():
            don_data=donation.save(commit=False)
            don_data.login_id=donr_login_data
            don_data.save()
            return redirect('users_home')
    else:
        donation=donation_form()
    return render(request,'donation_add.html',{'donation':donation})

def donation_view(request):
    donr_id=request.session.get('donor_id')
    donr_login_data=get_object_or_404(login,id=donr_id)
    all_products=donations.objects.filter(login_id=donr_login_data)
    return render(request,'donation_view.html',{'all_product':all_products})

def view_donation(request):
    all_products=donations.objects.filter(donation_status='pending')
    return render(request,'all_donations.html',{'all_product':all_products})

def request_donation(request,id):
    ngos_id=request.session.get('ngo_id')
    ngo_login_data=get_object_or_404(login,id=ngos_id)
    donation=get_object_or_404(donations,id=id)
    if requests.objects.filter(ngo=ngo_login_data,donation_id=donation,request_status='requested').exists():
        messages.success(request,'already requested')
    else:
        request_data=requests.objects.create(
            ngo=ngo_login_data,
            donation_id=donation,
            donor_id=donation.login_id
        )
        donation.donation_status='requested'
        donation.save()
    return redirect('all_donations')

def admin_users(request):
    all_users=user.objects.all()
    return render(request,'all_donor.html',{'all_user':all_users})

def admin_donations(request):
    all_dons=donations.objects.all()
    return render(request,'all_donations_view.html',{'all_don':all_dons})

def admin_requests(request):
    all_req=requests.objects.all()
    return render(request,'all_requests_view.html',{'all_reqs':all_req})