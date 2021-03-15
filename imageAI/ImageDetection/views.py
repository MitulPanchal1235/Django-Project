from django.shortcuts import render,redirect,HttpResponse
from .forms import *
import xml.etree.ElementTree as ET
from PIL import ImageFont,ImageDraw,Image
import os
from .serializers import *
from rest_framework.renderers import JSONRenderer
import csv
def index(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            data = Data.objects.all()
            for i in data:
                imgp=i.image_file
                xmlp=i.xml_file
            imgp='media/'+str(imgp)
            xmlp='media/'+str(xmlp)
            mytree=ET.parse(xmlp)
            myroot=mytree.getroot()
            pn=myroot[1].text
            image=Image.open(imgp)
            draw=ImageDraw.Draw(image)
            ft=ImageFont.truetype('Arial.ttf',30)
            for i in myroot.findall('object'):
                tn=i.find('name').text
                a=int(i.find('bndbox')[0].text)
                b=int(i.find('bndbox')[1].text)
                c=int(i.find('bndbox')[2].text)
                d=int(i.find('bndbox')[3].text)
                idata=Image_Details.objects.create(imagename=pn,objectname=tn,xmin=a,ymin=b,xmax=c,ymax=d)
                idata.save()
                draw.text(xy=(a,b-30),text=tn,fill='red',font=ft)
                draw.rectangle((a,b,c,d),outline='red',width=3)
            image.save(imgp)
            return redirect('/')
    return render(request ,'index.html',{'form':form})

def Filerecord(request):
    for i in Data.objects.all():
        data1 = i
    serializeddata = Serializerpy(data1)
    Jdata = JSONRenderer().render(serializeddata.data)
    return HttpResponse(Jdata,content_type='application/json')

def report(request): 
    sd=request.POST.get('sdate')
    ed=request.POST.get('edate')
    response=HttpResponse(content_type="text/csv")
    d2=Image_Details.objects.filter(timestamp__gte=sd).filter(timestamp__lte=ed)
    writer=csv.writer(response)
    writer.writerow(['picture name','object name','xmin','ymin','xmax','ymax','timestamp'])
    for d in d2.values_list('imagename','objectname','xmin','ymin','xmax','ymax','timestamp'):
        writer.writerow(d)
    response['Content-Disposition']='attachment; filename = "reportextract.csv"'
    return response





















