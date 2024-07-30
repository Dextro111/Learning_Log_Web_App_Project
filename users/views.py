from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def logout_view(request):
#     """Log the User Out."""
#     logout(request)
    #return redirect('users:logged_out')

def register(request):
    """Register A New User"""
    if request.method != 'POST':
        #  Display Blank Registration Form.
        form = UserCreationForm()
    else:
        # Process Completed Form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the User in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

