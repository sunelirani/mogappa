from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
from .forms import PostForm

def login_user(request):
    print 'hello', request.method
    if request.method == 'POST':
        print 'rani'
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print 'binit' , username, password
        if user is not None:
            print 'vikrant'
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/home/")
            else:
                print "Your account is not active, please contact the site admin"
        else:
            print "Your username and/or password were incorrect."

    return render_to_response('login.html', context_instance=RequestContext(request))

def home(request):
    print 'neha'
    return render_to_response('index.html', {'username': request.user.username})

def logout_user(request):
    print 'rr'
    logout(request)
    return HttpResponseRedirect('/login/')

def signup_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print username, password, email, confirm_password
        if password == confirm_password:
            user =User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            print user
            return HttpResponseRedirect("/home/")
        else:
                
            return render(request, '/signup_user.html')
        
    return render(request, 'signup_user.html')

def post_list(request):
    print 'puja'
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})			

def post_new(request):
    print 'suneli'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print 'su'
	    post=form.save(commit=False)
	    post.author=request.user
	    post.published_date = timezone.now()
	    post.save()
	    return redirect(request, 'login.views.post_detail.html', pk=post.pk)
    else:
	form = PostForm()
        return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    print 'anu'
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
	    post = form.save(commit=False)
	    post.author = request.user
	    post.published_date = timezone.now()
	    post.save()
	    return redirect(request, 'login.views.post_detail.html', pk=post.pk)
    else:
	form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})



