from django import forms

from app.models import *





class Topicform(forms.Form):
    topic_name=forms.CharField(max_length=100)


TQS=Topic.objects.all()
d={'TQS':TQS}
class Webpageform(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=TQS)
    name=forms.CharField(max_length=100)
    email=forms.EmailField()


