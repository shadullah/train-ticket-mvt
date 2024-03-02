from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        new_user = super().save(commit=False)
        if commit == True:
            new_user.save()

            UserAccount.objects.create(
                user=new_user,
                account_no=1000+new_user.id
            )
        return new_user
    
class UserUpdateForm(forms.ModelForm):
    # password = None
    class Meta:
        model = User 
        fields = ['username', 'email']

