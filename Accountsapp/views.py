from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def Register(request):
    if request.method == 'POST':
        f_name = request.POST['First_name']
        l_name = request.POST['Last_name']
        username = request.POST['Username']
        e_mail = request.POST['Email']
        password = request.POST['Password']
        confirm_password = request.POST['Confirm Password']
        # Validation
        error_msg = None
        if not f_name:
            error_msg = "First name required"
        elif len(f_name) < 4:
            error_msg = "First name must be 4 characters long or more"
        elif not l_name:
            error_msg = "Last name required"
        elif len(l_name) < 4:
            error_msg = "Last name must be 4 characters long or more"

        elif len(username) < 8:
            error_msg = "Username must be 8 characters long"

        elif len(e_mail) < 8:
            error_msg = "Email must be 8 characters long"

        elif len(password) < 8:
            error_msg = "Password must be 8 characters long"

        elif User.objects.filter(email=e_mail).exists():
            error_msg = "Email already taken"

        elif User.objects.filter(username=username).exists():
            error_msg = "Username already exists"

        elif password != confirm_password:
            error_msg = "Password not matching"

        values = {

            'vf_name': f_name,
            'vl_name': l_name,
            'v_username': username,
            'v_password': password,
            'v_email': e_mail,
            'vc_password': confirm_password
        }
        if not error_msg:
            u = User.objects.create_user(first_name=f_name, last_name=l_name, email=e_mail, username=username,
                                         password=password)
            u.save()
            return redirect("indexes")
        else:
            data = {
                'values': values,
                'error_msgs': error_msg,
            }

            return render(request, 'Registration.html', data)

    else:
        return render(request, 'Registration.html')



def Login(request):
    if request.method == 'POST':
        l_username = request.POST['Username']
        l_password = request.POST['Password']
        userlogin = auth.authenticate(username=l_username, password=l_password)
        if userlogin is not None:
            auth.login(request, userlogin)
            return redirect('/')
        else:
            error_msg = "Invalid details"
            return render(request, 'Login.html', {'error': error_msg})
    else:
        return render(request,'Login.html')
def Logout(request):
    auth.logout(request)
    return redirect('/')