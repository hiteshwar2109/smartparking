
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login successful!")  # Debugging line
                return redirect('home')  # Ensure this matches the name in your urls.py
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')


def index(request):
     return render(request, 'index.html')




# View for rendering the parking lot reservation page
def reservation_view(request):
    return render(request, 'reservation.html')

# View to handle reservation requests
@csrf_exempt
def reserve_slot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            slot_id = data.get('slot_id')
            # Here you can implement the logic to save the reservation
            # For demonstration purposes, we'll just return success
            response = {
                'status': 'success',
                'message': f'Slot {slot_id} has been reserved.'
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': 'error',
                'message': str(e)
            }
            return JsonResponse(response)
    else:
        response = {
            'status': 'error',
            'message': 'Invalid request method.'
        }
        return JsonResponse(response)
def user(request):
     return render(request, 'user.html')
def details(request):
     return render(request, 'details.html')
def downtown(request):
     return render(request, 'downtown.html')
def airport(request):
     return render(request, 'airport.html')
def mall(request):
     return render(request, 'mall.html')
def stadium(request):
     return render(request, 'stadium.html')
def office(request):
     return render(request, 'office.html')