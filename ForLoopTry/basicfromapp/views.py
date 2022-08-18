import json
from django.shortcuts import render
from . import forms
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
arr=['Buy Groceries','Buy Stationary',]
value=0      

import datetime

Time = datetime.datetime.now()


def ForLoopTest(request):
    print("in")
    if request.is_ajax():
       print("out")
       global value
       data = {'message':f'{value}'}
       return HttpResponse(json.dumps(data),content_type='application/json')
    pass

def ForLoopTestPage(request):
    return render(request,'webpages/ForLoopTest.html') 
 
def get_todo(request):
    if request.is_ajax():
       global arr
       data = json.dumps(arr)
       return HttpResponse(data,content_type='application/json')
    
    else:
          raise Http404
def add_todo(request):
    if request.is_ajax() and request.POST:
       global arr
       request.POST.get('item','it')
       arr.append(request.POST.get('item'))
       
       data = {'message':'Added Sucesfully'}
       return HttpResponse(json.dumps(data),content_type='application/json')
    
    else:
          raise Http404          

def update(request):
    if request.is_ajax() and request.POST:
       
       global value
       value=request.POST.get('item')
       
       data = {'message':f'{value}'}
       return HttpResponse(json.dumps(data),content_type='application/json')
    
    else:
          raise Http404          
          
def updatepage(request):
    return render(request,'webpages/update.html')

@csrf_exempt
def index(request):
    global Time
    Time = str(datetime.datetime.now()) + datetime.datetime.now().strftime("%S") 
    print(Time)
    return render(request,'webpages/index.html', {"time":Time})
@csrf_exempt
def indexChange(request):
    global Time
    Time = str(datetime.datetime.now()) + datetime.datetime.now().strftime("%S") 
    return render(request,'webpages/index.html', {"time":Time})

def form_name_view(request):
    form=forms.FormName
    FormDictionary={'form':form}
    if request.method=='POST':
        form=forms.FormName(request.POST)
        
        if form.is_valid():
            print("NAME: "+ form.cleaned_data['name'])
            print("Email: "+ form.cleaned_data['email'])
            print("TextFeild: "+ form.cleaned_data['text'])
            FormDictionary['ConfirmLabel']="reqest taken"
    
    return render(request,'webpages/form_page.html',FormDictionary)