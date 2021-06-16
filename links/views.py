from django.shortcuts import render,redirect
from .models import Link
# Create your views here.

def home(request):
    # if request.method=="GET":
    #     obj=Link.objects.all()
    #     for item in obj:
    #         item.save()
    if request.method=="POST":
        obj=Link.objects.create(url=request.POST['url'])
        obj.save()
        return redirect('home')
    list_items=Link.objects.all()
    context={'items':list_items}
    return render(request,'links/home.html',context)

def update(request):
    if request.method=="GET":
        obj=Link.objects.all()
        for item in obj:
            item.save()
        return redirect('home')

def delete(request,pk):
    if request.method=="POST":
        obj=Link.objects.get(id=pk)
        obj.delete()
        return redirect('home')

def search(request):
    query=request.GET['query']
    all_items=Link.objects.filter(name__icontains=query)
    context={'items':all_items}
    return render(request,'links/search.html',context)
    
