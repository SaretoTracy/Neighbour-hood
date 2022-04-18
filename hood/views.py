from django.shortcuts import render, redirect
from .models import Profile,NeighbourHood,Business,Authority,Health,Post
from django.contrib.auth.models import User
from .forms import ProfileForm,HoodForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    profiles = Profile.objects.filter(id = current_user.id).all()
    hoods = NeighbourHood.objects.all().order_by('-post_date')    
    return render(request, 'index.html',{"profiles": profiles, "hoods":hoods})
      
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'profile-update.html', {'form': form})

def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})
 
def createhood(request):
    current_user = request.user
    form = HoodForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request,'create-hood.html',{'form':form})


 
def neighbourhood(request,id):
    user = request.user
    profiles = Profile.objects.filter(user = user).all()
    businesses = Business.objects.all().filter(neighbourhood_id=id)
    posts = Post.objects.all().order_by('-posted_at').filter(neighbourhood_id=id)
    hood = NeighbourHood.objects.get(id=id)
    police = Authority.objects.all().filter(neighbourhood_id=id) 
    health = Health.objects.all().filter(neighbourhood_id=id) 
    
    
    return render(request,'hood.html',{'hood':hood,'police':police,'health': health,'posts':posts,'businesses': businesses,'profiles':profiles})
  

 