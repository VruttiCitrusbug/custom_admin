from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm
from customloginapp.MyAuthenticationForm import MyAuthenticationForm
from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
# Create your views here.
# raise ValidationError("you are not admin")
def login(request):
    if request.method  == 'POST':
        form = MyAuthenticationForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                if user.is_superuser:
                    auth.login(request,user)
                    return redirect('http://127.0.0.1:8000/customadmin/')
            else:
                return redirect("http://127.0.0.1:8000/customlogin/mylogin")
    return render(request,r'C:\Users\Vrutti\Desktop\py\custom_admin\ebr-randy-develop\core\templates\core\ebr\registration\login.html',{'form': MyAuthenticationForm()})
    