from .models import CompanyProfile,AdminInfo,Activity,Comment
from userprofile.models import Member
from django.db.models import Count
from datetime import date


def flourish(request):
    fvp = CompanyProfile.objects.get(pk=1)


    


    context = {
     'fvp': fvp,
    }

    return context

def notification(request):
    today = date.today()
    celebrants = Member.objects.filter(dob__day = today.day,dob__month =today.month)
    counter = celebrants.count()

    adinfo = AdminInfo.objects.all()
    timer = adinfo.count()

    bar = counter+timer
    


    context = {
     'celebrants':celebrants,
     'counter':counter,
     'bar':bar,
     'adinfo':adinfo,
     'timer':timer,
      
   
    }

    return context

