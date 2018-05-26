from django.shortcuts import render_to_response,redirect,render
from django.utils import timezone
from .models import Post,User,Comment,Like,Dislike
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .forms import RegForm,LogForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404


@csrf_exempt
def reg(request):
    if request.method == 'POST':
      form = RegForm(request.POST)
      if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                reg = form.save()
                reg.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect(main)
    form = RegForm()
    return render_to_response( 'app/reg.html',{'form':form}, RequestContext(request))
@csrf_exempt
def main(request):
    view = ''
    username = request.user.username
    view = User.objects.filter(username=request.user.username).values('image')
    print(view)
    return render_to_response('app/main.html', {'request': request,'user': request.user,'view': view}, RequestContext(request))

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def validate_password(request):
    password = request.GET.get('password', None)
    if (User.objects.filter(password=password).exists()):
        data = {
        'is_taken' : 'True'
        }
    else:
        data = {
        'is_taken' : 'False'
        }
    return JsonResponse(data)
