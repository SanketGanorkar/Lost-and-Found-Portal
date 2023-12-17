from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Item, Claim
from student.forms import StudentRegistrationForm, StudentLoginForm, ItemForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def gettingStarted(request):
    return render(request, 'gettingStarted.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def forgotPassword(request):
    return render(request, 'forgotpassword.html')

def registerpage(request):
    return render(request, 'registerpage.html')

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            
            student = Student.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                branch=form.cleaned_data['branch'],
                contact_number=form.cleaned_data['contact_number'],
                prn=form.cleaned_data['prn']
            )
            
            login(request, user)
            
            return redirect('login-page')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = StudentRegistrationForm()
        
    return render(request, 'loginpage.html', {'form': form})

def studentLogin(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(item_list)
                else:
                    return render(request, 'loginpage.html')
        else:
            return render(request, 'loginpage.html')
    else:
        messages.error(request, 'Form submission failed. Please check the form.')
        print("Form errors:", form.errors)
    return render(request, 'loginpage.html')

def addItempage(request):
    return render(request, 'additem.html')


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                item = Item(
                    item_category=form.cleaned_data['item_category'],
                    item_description=form.cleaned_data['item_description'],
                    location=form.cleaned_data['location'],
                    description=form.cleaned_data['description'],
                    verification_question=form.cleaned_data['verification_question'],
                    choice1=form.cleaned_data['choice1'],
                    choice2=form.cleaned_data['choice2'],
                    choice3=form.cleaned_data['choice3'],
                    choice4=form.cleaned_data['choice4'],
                    item_image=form.cleaned_data['item_image'],
                    student=request.user.student
                )
                item.save()

                messages.success(request, 'Item added successfully.')
                return redirect('item_list')
            else:
                messages.error(request, 'Authentication failed. Please log in.')
        else:
            messages.error(request, 'Form submission failed. Please check the form.')
    else:
        form = ItemForm()

    return render(request, 'additem.html', {'form': form})

def claim_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        verification_answer = request.POST.get('verification_answer')
        print(verification_answer)

        if verification_answer == str(item.verification.correct_choice):
            claim_status = 'Approved'
            item.claim = Claim.objects.get(claim=claim_status)
            item.save()

            messages.success(request, 'Claim submitted successfully.')
        else:
            messages.error(request, 'Claim submission failed. Incorrect verification answer.')

        return redirect('item_list')

    return render(request, 'homepage.html', {'item': item})


def item_list(request):
    items = Item.objects.all()
    return render(request, 'homepage.html', {'items': items})
