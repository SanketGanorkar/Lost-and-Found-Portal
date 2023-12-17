from django import forms
from home.models import Item

class StudentRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    prn = forms.CharField(max_length=8, required=True)
    branch = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    contact_number = forms.CharField(max_length=11, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class StudentLoginForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)

class ItemForm(forms.ModelForm):
    item_description = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=100, required=True)
    verification_question = forms.CharField(max_length=200, required=True)
    choice1 = forms.CharField(max_length=100, required=True)
    choice2 = forms.CharField(max_length=100, required=True)
    choice3 = forms.CharField(max_length=100, required=True)
    choice4 = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Item
        fields = ['item_category', 'item_description', 'location', 'description', 'item_image', 'verification_question', 'choice1', 'choice2', 'choice3', 'choice4']