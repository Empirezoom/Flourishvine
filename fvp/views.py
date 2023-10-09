
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q # for search 
from userprofile.models import *

from django.db.models import Count
from datetime import date
from django.contrib.auth.decorators import login_required





# Create your views here.
def homepage(request):

    feat = Features.objects.get(pk=1)
    about = About.objects.get(pk=1)
    tperson= Testimonies.objects.all()
    gright = Gallery.objects.filter(land_right2=True)
    gleft = Gallery.objects.filter(land_left2=True)
    gport = Gallery.objects.filter(portrait_center1=True)

    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,'Your message has been sent successfully!')
            return redirect('message_center')
    
    context = {
        'feat':feat,
        'feat':feat,
        'about':about,
        'tperson':tperson,
        'gright':gright,
        'gleft':gleft,
        'gport':gport,
        'contact':contact,
    }
    return render(request,'index.html',context)
def give(request):
   
    giver = Give.objects.get(pk=1)
    
    context = {
        
        'giver':giver,
    }
    return render(request,'give.html',context)

def register(request):
    member = MemberForm()
    if request.method == 'POST':
        dob = request.POST['dob']
        phone = request.POST['phone']
        address = request.POST['address']
        pix = request.POST['pix']
        member = MemberForm(request.POST)
        if member.is_valid():
            user = member. save()
            newuser = Member()
            newuser.user = user
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.dob = dob
            newuser.phone = phone
            newuser.address = address
            newuser.pix = pix
            newuser.save()
            messages.success(request, f'Dear {user} account has been created successfully')
            return redirect('message_center')
        else:
            messages.error(request, member.errors)
            return redirect('message_center')

    return render(request,'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('message_center')
        else:
            messages.info(request, 'username/password incorrect')
            return redirect('message_center')
        
    return render(request, 'register.html')

def signout(request):
    logout(request)
    messages.success(request, 'you are now signed out')
    return redirect('message_center')


@login_required(login_url='signin')
def profile(request):
    userprof = Member.objects.get(user__username=request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        new = request.user.username.title()
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Dear {new}  password changed!')
            return redirect('message_center')
        else:
            messages.error(request, f'{new} password did not change, {form.errors}')
            return redirect('message_center')

    context = {
        'userprof':userprof,
        'form':form,
    }

    return render(request, 'profile.html',context)


@login_required(login_url='signin')
def profile_update(request):
    userprof = Member.objects.get(user__username = request.user.username)
    form = ProfileForm(instance=request.user.member)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.member)
        if form.is_valid():
            user = form.save()
            new = user.first_name.title()
            messages.success(request, f'Dear {new} your profile update is successful, go back to profile to check ')
            return redirect('message_center')
        else:
            new = user.first_name.title()
            messages.error(request, f'Dear {new}, errors: {form.errors}')
            return redirect('message_center')
          
    context = {
        'userprof':userprof
    }    
    return render(request, 'profile.html',context)




def message_center(request):


    return render(request,'messages.html')




def welcome(request):
   
 
    return render(request,'welcoming.html')


def event(request):
    giver = Give.objects.get(pk=1)
    activities = Activity.objects.all()

    birthdays = Member.objects.all()
    button_count = birthdays.count()

    today = date.today()
    celebrants = Member.objects.filter(dob__day = today.day,dob__month =today.month)
    counter = celebrants.count()

    # to count total comments in all posts
    # total_comments = Comment.objects.order_by('-id').count()
   
    





    context = {
        
        'giver':giver,
        'activities':activities,
        'birthdays':birthdays,
        'button_count':button_count,
        'celebrants':celebrants,
        'counter':counter,
       
       
      
    }
    return render(request,'event.html',context)


def detail(request,theslug):
    giver = Give.objects.get(pk=1)
    activities = Activity.objects.all()

    postdet = Activity.objects.get(slug = theslug)
    comments = Comment.objects.order_by('-id').filter(post=postdet)
    com_count = comments.count()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
    if form.is_valid():
        thecom = form.save(commit=False)
        thecom.post = postdet
        thecom.commenter = request.user
        thecom.save()
        return redirect('detail',theslug = postdet.slug)


    context = {
    'giver':giver,
    'activities':activities,

    'postdet':postdet,
    'comments':comments,
    'form':form,
    'com_count':com_count,
    }

    return render(request,'details.html',context)


@login_required(login_url='signin')
def post_like(request):
  post_url = request.META.get('HTTP_REFERER')
  user = request.user
  if request.method =='POST':
    post_id = request.POST.get('post_id')
    post_obj = Activity.objects.get(id=post_id)

    if user in post_obj.liked.all():
      post_obj.liked.remove(user)
    else:
      post_obj.liked.add(user)
    like,created = Like.objects.get_or_create(user=user,post_id=post_id)

    if not created:
      if like.value == 'like':
        like.value = 'unlike'
      else:
        like.value = 'like'
      like.save()
  return redirect(post_url)



@login_required(login_url='signin')
def fvp_media_admin(request):
    activities = Activity.objects.all()
    person = Member.objects.all()
    cont = Contact.objects.all()
    talk = Comment.objects.all()
    heart = Like.objects.all()
    testifying = Testimonies.objects.all()
    infor = AdminInfo.objects.all()
    
    if request.method == 'POST':
        theme = CompanyProfileForm(request.POST,request.FILES)
        if theme.is_valid():
            instance = CompanyProfile.objects.first()
            instance.montheme = theme.cleaned_data['montheme']
            instance.save()
            return redirect('fvp_media_admin')
        else:
            theme = CompanyProfileForm()

    if request.method == 'POST':
        activ = ActivityForm(request.POST,request.FILES)
        if activ.is_valid():
            activ.save()
            messages.success(request,'one item added to activity/post')
            return redirect('fvp_media_admin')
        else:
            activ = ActivityForm()

    if request.method == 'POST':
        testimoni = TestimoniesForm(request.POST,request.FILES)
        if testimoni.is_valid():
            testimoni.save()
            messages.success(request,'one item added to testimonies')
            return redirect('fvp_media_admin')
        else:
            testimoni = TestimoniesForm()

    if request.method == 'POST':
        infos = AdminInfoForm(request.POST)
        if infos.is_valid():
            infos.save()
            messages.success(request,'an information has been passed on notification page')
            return redirect('message_center')
        else:
            infos = AdminInfoForm()





    context = {
        'activities':activities,
        'person':person,
        'cont':cont,
        'talk':talk,
        'heart':heart,
        'testifying':testifying,
        'infor':infor,
   
    
       
    }
    return render(request,'admin.html',context)

def delete(request):
    if request.method == 'POST':
        del_item = request.POST['del_id']
        Activity.objects.filter(pk=del_item).delete()
        messages.success(request, 'one item deleted')
        return redirect('fvp_media_admin')
    
def del_test(request):
    if request.method == 'POST':
        del_item = request.POST['del_id']
        Testimonies.objects.filter(pk=del_item).delete()
        messages.success(request, 'one item deleted')
        return redirect('fvp_media_admin')
    
def del_notification(request):
    if request.method == 'POST':
        del_item = request.POST['del_id']
        AdminInfo.objects.filter(pk=del_item).delete()
        messages.success(request, 'one item deleted in notification page')
        return redirect('fvp_media_admin')
    
def search(request):
  if request.method == 'POST':
    items = request.POST['search']
    searched = Q(Q(title__icontains=items)|Q(content__icontains=items)|Q(active__icontains=items))
    searched_item = Activity.objects.filter(searched)

    context = {
      'items':items,
      'searched_item':searched_item,
    }

    return render(request,'search.html',context)
  else:
    return render(request,'search.html')
  


@login_required(login_url='signin')
def notification(request):

      
    
    return render(request,'notification.html')
