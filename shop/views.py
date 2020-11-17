
from math import ceil
import json
from django.shortcuts import render
from django.http import HttpResponse
from.models import Product,Contact,Order,OrderUpdate


# Create your views here.
def index(request):
   # products=Product.objects.all()
   # n=len(products)
    # nslides=n//4+ ceil((n/4)-(n//4))
  #  params={'no of slide':nslides,'range':range(1,nslides),'product':products}
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])

    # allprods=[[products,range(1,nslides),nslides],
    # [products,range(1,nslides),nslides]]
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc_help=request.POST.get('desc_help', '')
        contact=Contact(name=name,email=email,phone=phone,desc_help=desc_help)
        contact.save()
    return render(request,'shop/contact.html')   

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"sucess","updates":updates,"itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e :
            return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter right item in search"}
    return render(request, 'shop/search.html', params)


def prodView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product':product[0]})    

def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')       
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')
        phone=request.POST.get('phone','')
        items_json=request.POST.get('itemsJson','')
        order=Order(name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,phone=phone,items_json=items_json)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')