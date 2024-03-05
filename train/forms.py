from django import forms
from .models import Train_list

class AddTrainForm(forms.ModelForm):
    class Meta:
        model = Train_list
        fields = ['name', 'time', 'station', 'destination','seat_number']

class TrainInfoUpdateForm(forms.ModelForm):
    class Meta:
        model= Train_list
        fields = ['name', 'time', 'destination']
