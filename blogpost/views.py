from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import posts

# Create your views here.
def index(request):
    post = posts.objects.all()
    username = request.user.username
    return render(request, 'index.html',{'post':post,'username':username})

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
                return redirect('register')  

            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')   

        else:
            messages.info(request, 'Password not Same')
            return redirect('register')  

    else:             
        return render(request,'register.html')    


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are Invalid')
            return redirect('login')  

    else:          
        return render(request, 'login.html')
def ad(request):
    return render(request, 'ad.html')

def save(request):
    if request.method=='POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = 0
        created = request.POST.get('created')

        # username = request.user.username
        # if author==username:
        sv = posts(author,title=title,body=body,created=created)
        sv.save()
        return HttpResponse("Submitted")

        # else:
        #     messages.info(request, 'Author is not valid')
        #     return redirect('ad')

def search(request):
    query = request.GET['search']
    if len(query)>70:
        post = []

    else:
        post = posts.objects.filter( title__icontains=query)
        context = {'post':post}
        return render(request, "search.html", context)

class UpdatePostView(UpdateView):
    model = posts
    template_name = 'update.html'
    fields = ['title','body']

class DeletePostView(DeleteView):
    model = posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
 
class UpdateProfileView(UpdateView):
    model = User
    template_name = 'update_profile.html'
    fields = ['username','email']
    success_url = reverse_lazy('index')

def LikeView(request, pk):
    p = get_object_or_404(posts, id=request.POST.get('post_id'))
    
    liked = False
    if p.likes.filter(id=request.user.id).exists():
        p.likes.remove(request.user)
        liked = False
    else:
        p.likes.add(request.user)
        liked =True
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    post = posts.objects.get(id=pk)
    stuff = get_object_or_404(posts, id= pk)
    likes_count = stuff.total_likes()

    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'post.html',{'post':post,'likes_count':likes_count,'liked':liked})