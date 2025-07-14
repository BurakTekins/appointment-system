from django.forms import ModelForm
from .models import User
from django import forms
<<<<<<< HEAD
from django.core.exceptions import ValidationError
import re
=======
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

class UserSignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Şifre")

    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'password', 'student_id']
        labels = {
            'name': 'Ad',
            'surname': 'Soyad',
            'email': 'E-posta',
            'password': 'Şifre',
            'student_id': 'Öğrenci Numarası',
        }
<<<<<<< HEAD
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        valid_domains = ['@live.acibadem.edu.tr', '@acibadem.edu.tr']
        if email and not any(email.endswith(domain) for domain in valid_domains):
            raise ValidationError(
                'Lütfen Acıbadem uzantılı e-posta adresinizi kullanınız.'
            )
        return email
    
    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        # Check if student_id is exactly 9 digits
        if not re.match(r'^\d{9}$', student_id):
            raise ValidationError(
                'Öğrenci numaranız 9 rakamdan oluşmalıdır.'
            )
        return student_id
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        # Check password length
        if len(password) < 8 or len(password) > 25:
            raise ValidationError(
                'Şifreniz 8-25 karakter uzunluğunda olmalıdır.'
            )
        
        # Check for at least one uppercase letter
        if not any(char.isupper() for char in password):
            raise ValidationError(
                'Şifreniz en az bir büyük harf içermelidir.'
            )
        
        # Check for at least one digit
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Şifreniz en az bir rakam içermelidir.'
            )
        
        return password
=======
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

class UserSignInForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['email', 'password']
=======
        fields = ['email', 'password']

    
        
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
