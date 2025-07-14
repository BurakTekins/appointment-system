<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.urls import reverse
from django import forms

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Şifreyi değiştirmek için doldurun, değiştirmeyecekseniz boş bırakın."
    )
    
    class Meta:
        model = User
        fields = ['email']  
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']  
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from .forms import UserSignUpForm
from django.urls import reverse


>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
<<<<<<< HEAD
            return redirect('/')  
=======
            return redirect(reverse('user_reservation', args=[user.id])) 
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
        else:
            messages.error(request, 'Giriş başarısız. Lütfen bilgilerinizi kontrol edin.')

    return render(request, 'users/sign_in_page.html', {'hide_container': True})

<<<<<<< HEAD
=======

>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
def sign_up_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, 'Başarılı bir şekilde kayıt oldunuz.')
            return redirect('sign_in')
        else:
            messages.error(request, 'Form geçersiz.')
    else:
        form = UserSignUpForm()

    return render(request, 'users/sign_up_page.html', {'form': form})

<<<<<<< HEAD
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.user.id != user.id:
        messages.error(request, "Bu işlemi yapmaya yetkiniz yok!")
        return redirect('/')
    
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        password = request.POST.get('password')
        
        if form.is_valid():
            user = form.save(commit=False)
            if password:  
                user.set_password(password)
            user.save()
            messages.success(request, 'Bilgileriniz başarıyla güncellendi.')
            
            if password:
                user = authenticate(email=user.email, password=password)
                if user:
                    login(request, user)
                
            return redirect('user_info', user_id=user.id)
    else:
        form = UserUpdateForm(instance=user)
    
    return render(request, 'users/user_info.html', {
        'form': form,
        'user': user
    })

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.user.id != user.id and not request.user.is_staff:
        messages.error(request, "Bu işlemi yapmaya yetkiniz yok!")
        return redirect('/')
    
    if request.method == 'POST':
        user.delete()
        logout(request)
        messages.success(request, 'Hesabınız başarıyla silindi.')
        return redirect('/')
    
    return redirect('user_info', user_id=user_id)

def logout_view(request):
    logout(request)
    return redirect('/')
=======

def update_user(request,user_id):
    user = User.objects.get(id=user_id)
    form = UserSignUpForm(instance = user)

    if request.method == 'POST':
        form = UserSignUpForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_info', user_id=user.id)
    
    context = {'form':form , 'user':user}
    return render(request,"users/user_info.html",context)
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
