from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact
from math import ceil

# Create your views here.
def home(request):
    products= product.objects.all()
    #print(products)
    n=len(products)
    nslides=n//4 +ceil(n/4-n//4)
    #prm={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    #allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    prodcategory=product.objects.values("category","id")
    categ={item["category"] for item in prodcategory}
    for c in categ:
        prod=product.objects.filter(category=c)
        allprods.append([prod, range(1,nslides),nslides])
    prm={"allprods":allprods}
    return render(request,'index.html',prm)
def about(request):
    return render(request,'about.html')
def store(request):
    return HttpResponse('Hi you are  store part')
def bag(request):
    return HttpResponse('Hi you are in bag')
def tracker(request):
    return HttpResponse('Hi you are in tracker')
def productview(request,myid):
    print(myid)
    prdct=product.objects.filter(id=myid)
    print(prdct)
    return render(request,'ProductView.html',{'product':prdct[0]})
def search(request):
    return HttpResponse('Hi you are in search')
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('Name','')
        email=request.POST.get('mail','')
        contact_no=request.POST.get('Phone','')
        query=request.POST.get('query','')
        print(name,email,contact_no,query)
        contact_info=Contact(name=name,email=email,phone=contact_no,descrip=query)
        contact_info.save()

    return render(request,"contact.html")

