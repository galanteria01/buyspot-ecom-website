from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignUpForm

# Create your views here.

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('items:list')
    else:
        return render(request, 'accounts/activation_invalid.html')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = request.get_current_site
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('accounts/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:activation_sent')
    elif request.method == "GET":
        form = SignUpForm()
    return render(request,'accounts/signup_page.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('items:list')
    elif request.method == "GET":
        form  = AuthenticationForm()
    return render(request,'accounts/login_page.html',{'form':form})

def logout_view(request):
    if request.method == "GET":
        logout(request)
    return redirect('items:list')

def user_details(request):
    current_user = request.user
    
    return render(request,'user_details_page.html',{'current_user',current_user})