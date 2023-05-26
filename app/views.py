from django.shortcuts import render
from app.models import *
from app.forms import *


# Create your views here.
def insert_topic(request):
    TFO=Topicform()
    d={'TFO':TFO}
    if request.method=='POST':
        TD=Topicform(request.POST)
        if TD.is_valid():
            topic_name=TD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topics.html',d1)
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=Webpageform()
    d={'WFO':WFO}
    if request.method=='POST':
        WD=Webpageform(request.POST)
        if WD.is_valid():
            topic_name=WD.cleaned_data['topic_name']
            name=WD.cleaned_data['name']
            email=WD.cleaned_data['email']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,email=email)[0]
            WO.save()
            WQS=Webpage.objects.all()
            d1={'WQS':WQS}
            return render(request,'display_webpage.html',d1)


    return render (request,'insert_webpage.html',d)