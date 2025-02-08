
from django.shortcuts import render, redirect, get_object_or_404# type: ignore
from django.contrib.auth import login,logout,authenticate # type: ignore
from django.contrib import messages # type: ignore

from  .models import Record   # type: ignore
from .form import SignUpForm
# Create your views here.
def home (request):
    records=Record.objects.all()
    #check to see if logging in
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been Logged IN')
            return redirect('home') # type: ignore
        else:
            messages.success(request,'error failed to logging')
            return redirect('home') # type: ignore
    return render(request,'home.html',{'records':records})

# def register_user(request):
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=UserCreationForm()

#     return render(request,'register.html',{'form':form})
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print('form is valid', form.is_valid())  # Call is_valid() method with parentheses
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data.get('password1')
            print('user', username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully registered')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed')
        else:
            print(form.errors)  # Print form errors to debug

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def logout_user (request):
    logout(request)
    return render(request,'home.html',{})

def customer_record(request,pk):
    if request.user.is_authenticated:
         
        # look up record
        customer=Record.objects.get(id=pk)
         
        return render(request,'customer_record.html',{'customer':customer})
    else:
        messages.warning(request,'you must log in to view this page')
        return redirect('home')
def delete_customer_record(request,pk):
    if request.user.is_authenticated:
        record=Record.objects.get(id=pk)
        record.delete()
        return redirect('home')
    else:
        messages.success('Failed to delete to record')
        return redirect('home')

def add_record(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            country = request.POST.get('country')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')
            if(first and last and phone and email and address and country and city and state and zipcode):
                record = Record(first_name=first, last_name=last, email=email, phone=phone, address=address, country=country, city=city, state=state, zipcode=zipcode) 
                print(record)
                record.save()
            messages.success(request, 'New record added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed to post details')
            redirect('home')
    return render(request, 'addRecord.html')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record, pk=pk)

        if request.method == 'POST':
            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            country = request.POST.get('country')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')
            
            if all([first, last, phone, email, address, country, city, state, zipcode]):
                current_record.first_name = first
                current_record.last_name = last
                current_record.phone = phone
                current_record.email = email
                current_record.address = address
                current_record.country = country
                current_record.city = city
                current_record.state = state
                current_record.zipcode = zipcode
                current_record.save()
                messages.success(request, 'Record updated successfully')
                return redirect('home')
            else:
                messages.error(request, 'Failed to update record. Please fill in all fields.')

        return render(request, 'updateRecord.html', {'record': current_record})
    else:
        messages.error(request, 'You need to be logged in to update a record')
        return redirect('home')
