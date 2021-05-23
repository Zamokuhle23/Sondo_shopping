from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from store.models import Customer


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'registration/login.html')

    def post(self, request):
        userData = request.POST
        customerEmail = Customer.emailExits(userData["email"])
        if customerEmail:
            # user = authenticate(email=customerEmail, password=userData["password"])
            if userData["password"] == customerEmail.password:
                # if user is not None:
                print("Step 2 passed")
                request.session["customer"] = customerEmail
                # request.session["user"]
                # print(userData["email"])
                if Login.return_url:
                    print("Shuuuu")
                    return HttpResponseRedirect(Login.return_url)
                else:
                    print(Login.return_url)
                    Login.return_url = None
                    return redirect('/')
            else:
                print(customerEmail.customer)
                print(customerEmail.password)
                return render(request, 'registration/login.html',
                              {"userData": userData, "error": "Email or password doesn't match"})
        else:

            return render(request, 'registration/login.html',
                          {"userData": userData, "error": "Email or password doesn't match"})


def logout(request):
    request.session.clear()
    return redirect('home')
