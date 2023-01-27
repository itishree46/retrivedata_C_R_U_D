from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    qst=Topic.objects.all()
    T={'topics':qst}
    return render(request,'display_topic.html',T)

def display_webpage(request):
    
    qsw=Webpage.objects.all()
    #qsw=Webpage.objects.filter(topic_name='cricket')
    #qsw=Webpage.objects.exclude(topic_name='cricket')
    #qsw=Webpage.objects.all()
    #qsw=Webpage.objects.order_by('name') #asc
    #qsw=Webpage.objects.order_by('-name') #desc
    #qsw=Webpage.objects.order_by(Length('name')) #asc
    #qsw=Webpage.objects.order_by(Length('name').desc()) #desc
    #qsw=Webpage.objects.filter(name__startswith='d')#it give the data which start with d od D
    #qsw=Webpage.objects.filter(name__endswith='r')#it give the data which end with r
    #qsw=Webpage.objects.filter(name__contains='r')#it give the data which have r letter
    #qsw=Webpage.objects.filter(name__regex='\w{8}')# it gives data which have length>=8
    #qsw=Webpage.objects.filter(topic_name__in=['cricket','hockey'])#it give the data which contain the given value
    #qsw=Webpage.objects.filter(Q(topic_name='football')|Q(name='Vivek')) # use of or(|) operator
    #qsw=Webpage.objects.filter(Q(topic_name='boxing') &Q(name='vijender')) #use of and(&) operator
    W={'webpage':qsw}
    return render(request,'display_webpage.html',W)

def display_access(request):
    qsa=AccessRecord.objects.all()
    #qsa=AccessRecord.objects.filter(date__year='2023')
    #qsa=AccessRecord.objects.filter(date__month='6')
    #qsa=AccessRecord.objects.filter(date__day='26')
    #qsa=AccessRecord.objects.filter(date__year='2023')
    #qsa=AccessRecord.objects.filter(date__gt='2022-10-3')
    #qsa=AccessRecord.objects.filter(date__lt='2022-10-3')
    #qsa=AccessRecord.objects.filter(date__year__gt='2022')
    A={'access':qsa}
    return render(request,'display_access.html',A)

def update_webpage(request):
    #Webpage.objects.filter(name='dhoni').update(url='https://dhoni.in') it will change 1 row 
    #Webpage.objects.filter(topic_name='cricket').update(name='Virat',url='https://Virat.in') change many row
    #Webpage.objects.filter(name='viju').update(name='siju') it will not change 
    #Webpage.objects.update_or_create(name='nick',defaults={'url':'https://nick.in'})
    #Webpage.objects.update_or_create(topic_name='kabadi',defaults={'name':'yuvraj','url':'https://yuvraj.in'}) we cn't give value for foreign key we have to give instance
    t='Kabadi'
    T=Topic.objects.get_or_create(topic_name=t)[0]
    T.save()
    Webpage.objects.update_or_create(topic_name=T,defaults={'name':'yuvraj','url':'https://yuvraj.in'})

    qsw=Webpage.objects.all()
    U={'webpage':qsw}
    return render(request,'display_webpage.html',U)

def delete_webpage(request):
    #Topic.objects.filter(topic_name='cricket').delete()   delete all cricket row
    #Webpage.objects.all().delete()  it will delete all the row from table permanently
    qsw=Webpage.objects.all()
    D={'webpage':qsw}
    return render(request,'display_webpage.html',D)