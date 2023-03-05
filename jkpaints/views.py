from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

from .models import *

#---------------------------------------------------------------------------------------------------
# ===================================== User Views =================================================
#---------------------------------------------------------------------------------------------------

def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get("txtname")
        pwd = request.POST.get("txtpass")
        customer = Customer.objects.filter(email_id=uname,password=pwd)
        i = 0
        for us in customer:
            i = i+1
            request.session['customer'] = us.email_id
            request.session['cid'] = us.customer_id
            
            return redirect("/user")
    return render(request, "user/clogin.html")



def productlist(request):
    obj = Product.objects.all()
    return render(request, 'user/productgrid.html', {"Product": obj})

def productdetailslist(request,id):
    obj = ProductDetails.objects.filter(product_id=id)
    return render(request, 'user/productdetailslist.html', {"productdetails":obj})

def productdetails1(request,id):
    pdetails=ProductDetails.objects.get(product_d_id=id)
    return render(request, 'user/proddetails.html', {"i":pdetails})

def addtocart(request,id):
    if request.session.has_key('cid'):
        pass
    else:
        return redirect('/userlogin/')
    cid=request.session['cid']
    cust=Customer.objects.get(customer_id=cid)
    proddetails=ProductDetails.objects.get(product_d_id=id)
    rate=proddetails.price
    cds=Cart.objects.filter(product_d=proddetails,customer=cust,price=rate)
    cnt=0
    for cd in cds:
        cnt=cnt+1
        cd.qty=cd.qty+1
        cd.save()
    if cnt==0:
        cart=Cart(customer=cust,product_d=proddetails,qty=1)
        cart.save()
    return redirect('/cart/')

def viewcart(request):
    cid=request.session['cid']
    cust=Customer.objects.get(customer_id=cid)
    cds=Cart.objects.filter(customer=cust)
    return render(request,'user/cart.html',{'proddetails':cds})

def machinerylist(request):
    obj = Machinery.objects.all()
    return render(request, 'user/machinerylist.html', {"machinery": obj})

#def machinerydetailslist(request,id):
 #   obj = machinerydetailslist.objects.filter(machinery_id=id)
 #   return render(request, 'user/machinerydetailslist.html', {"machinerydetails":obj})

def machineryaddtocart(request,id):
    if request.session.has_key('cid'):
        pass
    else:
        return redirect('/userlogin/')
    cid=request.session['cid']
    cust=Customer.objects.get(customer_id=cid)
    machinery=machinery.objects.get(machinery_id=id)
    rate=machinery.rent_price
    cds=Cart.objects.filter(machinery=machinery,customer=cust,rent_price=rate)
    cnt=0
    for cd in cds:
        cnt=cnt+1
        cd.qty=cd.qty+1
        cd.save()
    if cnt==0:
        cart=Cart(customer=cust,machinery=machinery,qty=1)
        cart.save()
    return redirect('/machinerycart/')

def machinerycart(request):
    cid=request.session['cid']
    cust=Customer.objects.get(customer_id=cid)
    cds=Cart.objects.filter(customer=cust)
    return render(request,'user/machinerycart.html',{'machinery':cds})



    
def userpage(request):
    return render(request, 'user/userindex.html')



#---------------------------------------------------------------------------------------------------
# ===================================== Admin Views =================================================
#---------------------------------------------------------------------------------------------------

def login(request):
    if request.method == "POST":
        uname = request.POST.get("txtname")
        pwd = request.POST.get("txtpass")
        admins = Admin.objects.filter(admin_name=uname, password=pwd)
        i = 0
        for ad in admins:
            i = i+1
            request.session['admin'] = ad.admin_name
            return redirect("/")
    return render(request, "login.html")

def adminpage(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    return render(request, 'm1.html')


def adminshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Admin.objects.all()
    return render(request, 'admin.html', {"Admin": obj})


def adminadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        aname = request.POST.get("txtaname")
        passw = request.POST.get("txtpassw")
        obj = Admin(admin_name=aname, password=passw)
        obj.save()
        return redirect("/admin")
    return render(request, 'adminadd.html')


def admindelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    aid = Admin.objects.get(admin_id=id)
    aid.delete()
    return redirect("/admin")


def adminedit(request, id):
    admin = Admin.objects.get(admin_id=id)
    return render(request, 'adminedit.html', {"admin": admin})


def adminupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    admin = Admin.objects.get(admin_id=id)
    admin.admin_name = request.POST.get('txtaname')
    admin.password = request.POST.get("txtpassw")
    admin.save()
    return redirect("/admin")


def areashow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Area.objects.all()
    return render(request, 'area.html', {"Area": obj})


def areaadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        pincode = request.POST.get("txtpincode")
        areaname = request.POST.get("txtareaname")
        cityid = request.POST["city_id"]
        obj = Area(pin_code=pincode, area_name=areaname, city_id=cityid)
        obj.save()
        return redirect("/area")
    city = City.objects.all()
    return render(request, 'areaadd.html', {'city': city})


def areadelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    areaid = Area.objects.get(pin_code=id)
    areaid.delete()
    return redirect("/area")


def areaedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    area = Area.objects.get(pin_code=id)
    cities = City.objects.all()
    return render(request, 'areaedit.html', {"area": area, "cities": cities})


def areaupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    area = Area.objects.get(pin_code=id)
    area.pin_code = request.POST.get('txtpincode')
    area.area_name = request.POST.get('txtareaname')
    area.city_id = request.POST["city_id"]
    area.save()
    return redirect("/area")
    city = City.objects.all()
    return render(request, 'areaadd.html', {'city': city})


def brandshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Brand.objects.all()
    return render(request, 'brand.html', {"Brand": obj})


def brandadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        bname = request.POST.get("txtbname")
        obj = Brand(brand_name=bname)
        obj.save()
        return redirect("/brand")
    return render(request, 'brandadd.html')


def branddelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    bid = Brand.objects.get(brand_id=id)
    bid.delete()
    return redirect("/brand")


def brandedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    brand = Brand.objects.get(brand_id=id)
    return render(request, 'brandedit.html', {"brand": brand})


def brandupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    brand = Brand.objects.get(brand_id=id)
    brand.brand_name = request.POST.get('txtbname')
    brand.save()
    return redirect("/brand")


def cityshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = City.objects.all()
    return render(request, 'city.html', {"City": obj})


def cityadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        cityname = request.POST.get("txtcityname")
        stateid = request.POST["state_id"]
        obj = City(city_name=cityname, state_id=stateid)
        obj.save()
        return redirect("/city")
    state = State.objects.all()
    return render(request, 'cityadd.html', {'state': state})


def citydelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cityid = City.objects.get(city_id=id)
    cityid.delete()
    return redirect("/city")


def cityedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    city = City.objects.get(city_id=id)
    state = State.objects.all()
    return render(request, 'cityedit.html', {"city": city, "state": state})


def cityupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    city = City.objects.get(city_id=id)
    city.city_name = request.POST.get('txtcname')
    city.state_id = request.POST["state_id"]
    city.save()
    return redirect("/city")
    state = State.objects.all()
    return render(request, 'stateadd.html', {'state': state})


def customershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Customer.objects.all()
    return render(request, 'customer.html', {"Customer": obj, })


def customeradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        cusname = request.POST.get("txtcusname")
        cusadd = request.POST.get("txtcusadd")
        cuscon = request.POST.get("txtcuscon")
        cusemail = request.POST.get("txtcusemail")
        cuspass = request.POST.get("txtcuspass")
        pincode = request.POST["pin_code"]
        pin = Area.objects.get(pin_code=pincode)
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        obj = Customer(customer_name=cusname, address=cusadd, contact_number=cuscon,
                       email_id=cusemail, password=cuspass, pin_code=pin, image=file_url)
        obj.save()
        return redirect("/customer")
    area = Area.objects.all()
    return render(request, 'customeradd.html', {'area': area})


def customerdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    cusid = Customer.objects.get(customer_id=id)
    cusid.delete()
    return redirect("/customer")


def customeredit(request, id):
    
    customer = Customer.objects.get(customer_id=id)
    area = Area.objects.all()
    return render(request, 'customeredit.html', {"customer": customer, "area": area})


def customerupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    customer = Customer.objects.get(customer_id=id)
    customer.customer_name = request.POST.get("txtcusname")
    customer.address = request.POST.get("txtcusadd")
    customer.contact_number = request.POST.get("txtcuscon")
    customer.email_id = request.POST.get("txtcusemail")
    customer.password = request.POST.get("txtcuspass")
    pin_code = request.POST["pin_code"]
    pin = Area.objects.get(pin_code=pin_code)
    customer.pin_code = pin
    image=request.FILES['image']
    fss=FileSystemStorage()
    file=fss.save(image.name,image)
    fp=fss.url(file)
    customer.image=fp
    customer.save()
    return redirect("/customer")
    area = Area.objects.all()
    return render(request, 'customeradd.html', {'area': area})


def finishshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Finish.objects.all()
    return render(request, 'finish.html', {"Finish": obj})


def finishadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        fname = request.POST.get("txtfname")
        obj = Finish(finish_name=fname)
        obj.save()
        return redirect("/finish")
    return render(request, 'finishadd.html')


def finishdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    fid = Finish.objects.get(finish_id=id)
    fid.delete()
    return redirect("/finish")


def finishedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    finish = Finish.objects.get(finish_id=id)
    return render(request, 'finishedit.html', {"finish": finish})


def finishupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    finish = Finish.objects.get(finish_id=id)
    finish.finish_name = request.POST.get('txtfname')
    finish.save()
    return redirect("/finish")


def formshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Form.objects.all()
    return render(request, 'form.html', {"Form": obj})


def formadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        fname = request.POST.get("txtfname")
        obj = Form(form_name=fname)
        obj.save()
        return redirect("/form")
    return render(request, 'formadd.html')


def formdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    fid = Form.objects.get(form_id=id)
    fid.delete()
    return redirect("/form")


def formedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    form = Form.objects.get(form_id=id)
    return render(request, 'formedit.html', {"form": form})


def formupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    form = Form.objects.get(form_id=id)
    form.form_name = request.POST.get('txtfname')
    form.save()
    return redirect("/form")


def invoiceshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Invoice.objects.all()
    return render(request, 'invoice.html', {"Invoice": obj})


def invoiceadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        customer = request.POST["customer_id"]
        date = request.POST.get("txtdate")
        servicedorder = request.POST["service_od_id"]
        rentdorder = request.POST["rent_od_id"]
        if servicedorder == "0":
            servicedorder = None
        if rentdorder == "0":
            rentdorder = None
        obj = Invoice(customer_id=customer, invoice_date=date,
                      service_od_id=servicedorder, rent_od_id=rentdorder)
        obj.save()
        return redirect("/invoice")
    customer = Customer.objects.all()
    serviceod = ServiceOrderDetails.objects.all()
    rentod = RentOrderDetails.objects.all()
    return render(request, 'invoiceadd.html', {'customer': customer, 'serviceod': serviceod, 'rentod': rentod})


def invoicedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    iid = Invoice.objects.get(invoice_id=id)
    iid.delete()
    return redirect("/invoice")


def invoiceedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoice = Invoice.objects.get(invoice_id=id)
    customer = Customer.objects.all()
    serviceod = ServiceOrderDetails.objects.all()
    rentod = RentOrderDetails.objects.all()
    return render(request, 'invoiceedit.html', {"invoice": invoice, "customer": customer, "serviceod": serviceod, "rentod": rentod})


def invoiceupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoice = Invoice.objects.get(invoice_id=id)
    invoice.customer_id = request.POST["customer_id"]
    invoice.invoice_date = request.POST.get("txtdate")
    serviceod = request.POST["service_od_id"]
    if serviceod == "0":
        serviceod = None
    invoice.service_od_id = serviceod
    rentod = request.POST["rent_od_id"]
    if rentod == "0":
        rentod = None
    invoice.rent_od_id = rentod
    invoice.save()
    return redirect("/invoice")
    customer = Customer.objects.all()
    serviceod = ServiceOrderDetails.objects.all()
    rentod = RentOrderDetails.objects.all()
    return render(request, 'invoiceadd.html', {'customer': customer, 'serviceod': serviceod, 'rentod': rentod})


def invoicerentshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = InvoiceRent.objects.all()
    return render(request, 'invoicerent.html', {"InvoiceRent": obj})


def invoicerentadd(request):
    if request.method == "POST":
        if request.session.has_key('admin'):
            pass
    else:
        return redirect('/login/')
        invoice = request.POST["invoice_id"]
        machinery = request.POST["m_id"]
        day = request.POST.get("txtday")
        charge = request.POST.get("txtchare")
        obj = InvoiceRent(invoice_id=invoice, m_id=machinery,
                          days=day, rent_charge=charge)
        obj.save()
        return redirect("/invoicerent")
    invoice = Invoice.objects.all()
    machinery = Machinery.objects.all()
    return render(request, 'invoicerentadd.html', {'invoice': invoice, 'machinery': machinery})


def invoicerentdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = InvoiceRent.objects.get(invoice_r_id=id)
    ird.delete()
    return redirect("/invoicerent")


def invoicerentedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoicerent = InvoiceRent.objects.get(invoice_r_id=id)
    invoice = Invoice.objects.all()
    machinery = Machinery.objects.all()
    return render(request, 'invoicerentedit.html', {"invoicerent": invoicerent, "invoice": invoice, "machinery": machinery})


def invoicerentupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoicerent = InvoiceRent.objects.get(invoice_r_id=id)
    invoicerent.invoice_id = request.POST["invoice_id"]
    invoicerent.machinery = request.POST["m_id"]
    invoicerent.days = request.POST.get("txtday")
    invoicerent.rent_charge = request.POST.get("txtchare")
    invoicerent.save()
    return redirect("/invoicerent")
    invoice = Invoice.objects.all()
    machinery = Machinery.objects.all()
    return render(request, 'invoicerentadd.html', {'invoice': invoice, 'machinery': machinery})


def invoiceserviceshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = InvoiceService.objects.all()
    return render(request, 'invoiceservice.html', {"InvoiceService": obj})


def invoiceserviceadd(request):
    if request.method == "POST":
        if request.session.has_key('admin'):
            pass
    else:
        return redirect('/login/')
        invoice = request.POST["invoice_id"]
        service = request.POST["service_id"]
        dimension = request.POST.get("txtdime")
        charge = request.POST.get("txtchare")
        obj = InvoiceService(invoice_id=invoice, service_id=service,
                             dimension=dimension, service_charge=charge)
        obj.save()
        return redirect("/invoiceservice")
    invoice = Invoice.objects.all()
    service = Service.objects.all()
    return render(request, 'invoiceserviceadd.html', {'invoice': invoice, 'service': service})


def invoiceservicedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    iid = InvoiceService.objects.get(invoice_s_id=id)
    iid.delete()
    return redirect("/invoiceservice")


def invoiceserviceedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoiceservice = InvoiceService.objects.get(invoice_s_id=id)
    invoice = Invoice.objects.all()
    service = Service.objects.all()
    return render(request, 'invoiceserviceedit.html', {"invoiceservice": invoiceservice, "invoice": invoice, "service": service})


def invoiceserviceupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    invoiceservice = InvoiceService.objects.get(invoice_s_id=id)
    invoiceservice.invoice_id = request.POST["invoice_id"]
    invoiceservice.service_id = request.POST["service_id"]
    invoiceservice.dimension = request.POST.get("txtdime")
    invoiceservice.service_charge = request.POST.get("txtchare")
    invoiceservice.save()
    return redirect("/invoiceservice")
    invoice = Invoice.objects.all()
    service = Service.objects.all()
    return render(request, 'invoiceserviceadd.html', {'invoice': invoice, 'service': service})


def jobworkershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = JobWorker.objects.all()
    return render(request, 'jobworker.html', {"JobWorker": obj})


def jobworkeradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        wname = request.POST.get("txtwname")
        address = request.POST.get("txtaddress")
        email = request.POST.get("txtemail")
        password = request.POST.get("txtpassword")
        cnumber = request.POST.get("txtcnumber")
        work = request.POST["work_id"]
        obj = JobWorker(worker_name=wname, address=address, email_id=email,
                        password=password, contact_no=cnumber, work_id=work)
        obj.save()
        return redirect("/jobworker")
    work = Work.objects.all()
    return render(request, 'jobworkeradd.html', {'work': work})


def jobworkerdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    jwid = JobWorker.objects.get(job_worker_id=id)
    jwid.delete()
    return redirect("/jobworker")


def jobworkeredit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    jobworker = JobWorker.objects.get(job_worker_id=id)
    work = Work.objects.all()
    return render(request, 'jobworkeredit.html', {"jobworker": jobworker, "work": work})


def jobworkerupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    jobworker = JobWorker.objects.get(job_worker_id=id)
    jobworker.worker_name = request.POST.get("txtwname")
    jobworker.address = request.POST.get("txtaddress")
    jobworker.email_id = request.POST.get("txtemail")
    jobworker.password = request.POST.get("txtpassword")
    jobworker.contact_no = request.POST.get("txtcnumber")
    jobworker.work_id = request.POST["work_id"]
    jobworker.save()
    return redirect("/jobworker")
    work = Work.objects.all()
    return render(request, 'jobworkeradd.html', {'work': work})


def machineryshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Machinery.objects.all()
    return render(request, 'machinery.html', {"Machinery": obj})


def machineryadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        mname = request.POST.get("txtmname")
        descri = request.POST.get("txtdescri")
        rcharge = request.POST.get("txtrcharge")
        mwork = request.POST.get("txtmwork")
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        obj = Machinery(m_name=mname, description=descri,
                        rent_charge=rcharge, machinery_work=mwork,image=file_url)
        obj.save()
        return redirect("/machinery")
    return render(request, 'machineryadd.html')


def machinerydelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    mid = Machinery.objects.get(m_id=id)
    mid.delete()
    return redirect("/machinery")


def machineryedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    machinery = Machinery.objects.get(m_id=id)
    return render(request, 'machineryedit.html', {"machinery": machinery})


def machineryupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    machinery = Machinery.objects.get(m_id=id)
    machinery.m_name = request.POST.get('txtmname')
    machinery.description = request.POST.get("txtdescri")
    machinery.rent_charge = request.POST.get("txtrcharge")
    machinery.machinery_work = request.POST.get("txtmwork")

    image = request.POST.get("txtimage")
   
    upload = request.FILES['image']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    machinery.image=file_url
    machinery.save()
    return redirect("/machinery")


def offershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Offer.objects.all()
    return render(request, 'offer.html', {"Offer": obj})


def offeradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        offer_code = request.POST.get("txtocode")
        min_amount = request.POST.get("txtmin")
        discount = request.POST.get("txtdis")
        max_discount = request.POST.get("txtmax")
        start_date = request.POST.get("txtstrtdate")
        end_date = request.POST.get("txtenddate")
        is_active = request.POST.get("txtisact")
        no_of_time = request.POST.get("txtnof")
        if min_amount == "0":
            min_amount = None
        if max_discount == "0":
            max_discount = None
        if start_date == "0":
            start_date = None
        if end_date == "0":
            end_date = None
        if is_active == "0":
            is_active = None
        if no_of_time == "0":
            no_of_time = None
        obj = Offer(offer_code=offer_code, min_amount=min_amount, discount=discount,
                    max_discount=max_discount, start_date=start_date, end_date=end_date, is_active=is_active,
                    no_of_time=no_of_time)
        obj.save()
        return redirect("/offer")
    return render(request, 'offeradd.html')


def offerdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    oid = Offer.objects.get(offer_id=id)
    oid.delete()
    return redirect("/offer")


def offeredit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    offer = Offer.objects.get(offer_id=id)
    return render(request, 'offeredit.html', {"offer": offer})


def offerupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    offer = Offer.objects.get(offer_id=id)
    offer.offer_code = request.POST.get('txtcode')
    offer.min_amount = request.POST.get("txtmin")
    offer.discount = request.POST.get("txtdis")
    offer.max_discount = request.POST.get("txtmax")
    offer.start_date = request.POST.get("txtstrtdate")
    offer.end_date = request.POST.get("txtenddate")
    offer.is_active = request.POST.get("txtisact")
    offer.no_of_time = request.POST.get("txtnof")
    offer.save()
    return redirect("/offer")


def pcategoryshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = PCategory.objects.all()
    return render(request, 'pcategory.html', {"PCategory": obj})


def pcategoryadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        pcname = request.POST.get("txtpcname")
        obj = PCategory(p_category_name=pcname)
        obj.save()
        return redirect("/pcategory")
    return render(request, 'pcategoryadd.html')


def pcategorydelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pcid = PCategory.objects.get(p_category_id=id)
    pcid.delete()
    return redirect("/pcategory")


def pcategoryedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pcategory = PCategory.objects.get(p_category_id=id)
    return render(request, 'pcategoryedit.html', {"pcategory": pcategory})


def pcategoryupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    pcategory = PCategory.objects.get(p_category_id=id)
    pcategory.p_category_name = request.POST.get('txtpcname')
    pcategory.save()
    return redirect("/pcategory")


def paymentshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Payment.objects.all()
    return render(request, 'payment.html', {"Payment": obj})


def paymentadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        invoice = request.POST["invoice_id"]
        pdate = request.POST.get("txtpdate")
        amount = request.POST.get("txtamount")
        obj = Payment(invoice_id=invoice, p_date=pdate, amount=amount)
        obj.save()
        return redirect("/payment")
    invoice = Invoice.objects.all()
    return render(request, 'paymentadd.html', {'invoice': invoice})


def paymentdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    payment = Payment.objects.get(payment_id=id)
    payment.delete()
    return redirect("/payment")


def paymentedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    payment = Payment.objects.get(payment_id=id)
    invoice = Invoice.objects.all()
    return render(request, 'paymentedit.html', {"payment": payment, "invoice": invoice})


def paymentupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    payment = Payment.objects.get(payment_id=id)
    payment.invoice_id = request.POST["invoice_id"]
    payment.p_date = request.POST.get("txtpdate")
    payment.amount = request.POST.get("txtamount")
    payment.save()
    return redirect("/payment")
    invoice = Invoice.objects.all()
    return render(request, 'paymentadd.html', {'invoice': invoice})


def productshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Product.objects.all()
    return render(request, 'product.html', {"Product": obj})


def productadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        pname = request.POST.get("txtpname")
        descri = request.POST.get("txtdescri")
        brand = request.POST["brand_id"]
        pcat = request.POST["p_category_id"]
        ptype = request.POST["type_id"]
        pform = request.POST["form_id"]
        pfinish = request.POST["finish_id"]
        mate = request.POST.get("txtmate")
        cc = request.POST.get("txtcc")
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        if brand == "0":
            brand = None
        if pcat == "0":
            pcat = None
        if ptype == "0":
            ptype = None
        if pform == "0":
            pform = None
        if pfinish == "0":
            pfinish = None
        if mate == "0":
            mate = None
        if cc == "0":
            cc = None
        obj = Product(product_name=pname, description=descri, brand_id=brand, p_category_id=pcat, type_id=ptype,
                      form_id=pform, finish_id=pfinish, material=mate, covering_capacity=cc, image=file_url)

        obj.save()
        return redirect("/product")
    brand = Brand.objects.all()
    pcategory = PCategory.objects.all()
    ptype = Ptype.objects.all()
    pform = Form.objects.all()
    pfinish = Finish.objects.all()
    return render(request, 'productadd.html', {'brand': brand, 'pcategory': pcategory, 'ptype': ptype, 'pform': pform, 'pfinish': pfinish})


def productdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productid = Product.objects.get(product_id=id)
    productid.delete()
    return redirect("/product")


def productedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    product = Product.objects.get(product_id=id)
    brand = Brand.objects.all()
    pcategory = PCategory.objects.all()
    ptype = Ptype.objects.all()
    pform = Form.objects.all()
    pfinish = Finish.objects.all()
    return render(request, 'productedit.html', {'product': product, 'brand': brand, 'pcategory': pcategory, 'ptype': ptype,
                                                'pform': pform, 'pfinish': pfinish})


def productupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    product = Product.objects.get(product_id=id)
    product.product_name = request.POST.get("txtpname")
    product.description = request.POST.get("txtdescri")
    brand = request.POST["brand_id"]
    if brand == "0":
        brand = None
    product.brand_id = brand
    pcat = request.POST["p_category_id"]
    if pcat == "0":
        pcat = None
    product.p_category_id = pcat
    ptype = request.POST["type_id"]
    if ptype == "0":
        ptype = None
    product.type_id = ptype
    pform = request.POST["form_id"]
    if pform == "0":
        pform = None
    product.form_id = pform
    pfinish = request.POST["finish_id"]
    if pfinish == "0":
        pfinish = None
    product.finish_id = pfinish
    mate = request.POST.get("txtmate")
    if mate == "0":
        mate = None
    product.material = mate
    cc = request.POST.get("txtcc")
    if cc == "0":
        cc = None
    product.covering_capacity = cc
    image = request.POST.get("txtimage")
    if image == "0":
        image = None
    if len(request.FILES) != 0:
        if(len(product.image)) >0:
            os.remove(product.image)
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        product.image=file_url
    product.save()

    return redirect("/product")
    brand = Brand.objects.all()
    pcategory = PCategory.objects.all()
    ptype = Ptype.objects.all()
    pform = Form.objects.all()
    pfinish = Finish.objects.all()
    return render(request, 'productadd.html',
                  {'brand': brand, 'pcategory': pcategory, 'ptype': ptype, 'pform': pform, 'pfinish': pfinish})


def productdetailsshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ProductDetails.objects.all()
    return render(request, 'productdetails.html', {"ProductDetails": obj})


def productdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        price = request.POST.get("txtprice")
        size = request.POST["size_id"]
        shade = request.POST["shade_id"]
        product = request.POST["product_id"]
        obj = ProductDetails(price=price, size_id=size,
                             shade_id=shade, product_id=product)
        obj.save()
        return redirect("/productdetails")
    size = Size.objects.all()
    shade = Shade.objects.all()
    product = Product.objects.all()
    return render(request, 'productdetailsadd.html', {'size': size, 'shade': shade, 'product': product})


def productdetailsdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productdid = ProductDetails.objects.get(product_d_id=id)
    productdid.delete()
    return redirect("/productdetails")


def productdetailsedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productdetails = ProductDetails.objects.get(product_d_id=id)
    size = Size.objects.all()
    shade = Shade.objects.all()
    product = Product.objects.all()
    return render(request, 'productdetailsedit.html', {'productdetails': productdetails,
                                                       'size': size, 'shade': shade, 'product': product})


def productdetailsupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productdetails = ProductDetails.objects.get(product_d_id=id)
    productdetails.price = request.POST.get("txtprice")
    productdetails.shade_id = request.POST["shade_id"]
    productdetails.size_id = request.POST["size_id"]
    productdetails.product_id = request.POST["product_id"]
    productdetails.save()
    return redirect("/productdetails")
    product = Product.objects.all()
    size = Size.objects.all()
    shade = Shade.objects.all()
    return render(request, 'productdetailsadd.html',
                  {'size': size, 'shade': shade, 'product': product})


def productordershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ProductOrder.objects.all()
    return render(request, 'productorder.html', {"ProductOrder": obj})


def productorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        customer = request.POST["customer_id"]
        date = request.POST.get("txtdate")
        offer = request.POST["offer_id"]
        total = request.POST.get("txttotal")
        sheeping = request.POST.get("txtsheeping")
        track_url = request.POST.get("txturl")
        track_no = request.POST.get("txtno")
        if offer == "0":
            offer = None
        if track_url == "0":
            track_url = None
        if track_no == "0":
            track_no = None
        obj = ProductOrder(customer_id=customer, date=date, offer_id=offer, total=total, shipping_handling=sheeping,
                           track_url=track_url, track_no=track_no)
        obj.save()
        return redirect("/productorder")
    customer = Customer.objects.all()
    offer = Offer.objects.all()
    return render(request, 'productorderadd.html', {'customer': customer, 'offer': offer})


def productorderdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = ProductOrder.objects.get(product_o_id=id)
    ird.delete()
    return redirect("/productorder")


def productorderedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productorder = ProductOrder.objects.get(product_o_id=id)
    customer = Customer.objects.all()
    offer = Offer.objects.all()
    return render(request, 'productorderedit.html', {"productorder": productorder, "customer": customer, "offer": offer})


def productorderupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productorder = ProductOrder.objects.get(product_o_id=id)
    productorder.customer_id = request.POST["customer_id"]
    productorder.date = request.POST.get("txtdate")
    offer = request.POST["offer_id"]
    if offer == "0":
        offer = None
    productorder.offer_id = offer
    productorder.total = request.POST.get("txttotal")
    productorder.shipping_handling = request.POST.get("txtsheeping")
    track_url = request.POST.get("txturl")
    if track_url == "0":
        track_url = None
    productorder.track_url=track_url 
    track_no = request.POST.get("txtno")
    if track_no=="0":
        track_no= None
    productorder.track_no=track_no
    productorder.save()
    return redirect("/productorder")
    customer = Customer.objects.all()
    offer = Offer.objects.all()
    return render(request, 'productorderadd.html', {'customer': customer, 'offer': offer})


def productorderdetailsshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ProductOrderDetails.objects.all()
    return render(request, 'productorderdetails.html', {"ProductOrderDetails": obj})


def productorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        productorder = request.POST["product_o_id"]
        productdetails = request.POST["product_d_id"]
        price = request.POST.get("txtprice")
        qty = request.POST.get("txtqty")
        discription = request.POST.get("txtdis")
        obj = ProductOrderDetails(
            product_o_id=productorder, product_d_id=productdetails, price=price, qty=qty, description=discription)
        obj.save()
        return redirect("/productorderdetails")
    product = ProductOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'productorderdetailsadd.html', {'product': product, 'productdetails': productdetails})


def productorderdetailsdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = ProductOrderDetails.objects.get(product_od_id=id)
    ird.delete()
    return redirect("/productorderdetails")


def productorderdetailsedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productorderdetails = ProductOrderDetails.objects.get(product_od_id=id)
    product = ProductOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'productorderdetailsedit.html', {"productorderdetails": productorderdetails, "product": product,
                                                    "productdetails": productdetails})


def productorderdetailsupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    productorderdetails = ProductOrderDetails.objects.get(product_od_id=id)
    productorderdetails.productorder_id = request.POST["product_o_id"]
    productorderdetails.productdetails_id = request.POST["product_d_id"]
    productorderdetails.price = request.POST.get("txtprice")
    productorderdetails.qty = request.POST.get("txtqty")
    productorderdetails.description = request.POST.get("txtdis")
    productorderdetails.save()
    return redirect("/productorderdetails")
    product = ProductOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'productorderdetails.add', {'product': product, 'productdetails': productdetails})


def ptypeshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Ptype.objects.all()
    return render(request, 'ptype.html', {"Ptype": obj})


def ptypeadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        ptname = request.POST.get("txtptname")
        obj = Ptype(type_name=ptname)
        obj.save()
        return redirect("/ptype")
    return render(request, 'ptypeadd.html')


def ptypedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ptid = Ptype.objects.get(type_id=id)
    ptid.delete()
    return redirect("/ptype")


def ptypeedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ptype = Ptype.objects.get(type_id=id)
    return render(request, 'ptypeedit.html', {"ptype": ptype})


def ptypeupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ptype = Ptype.objects.get(type_id=id)
    ptype.type_name = request.POST.get('txtptname')
    ptype.save()
    return redirect("/ptype")


def purchaseordershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = PurchaseOrder.objects.all()
    return render(request, 'purchaseorder.html', {"PurchaseOrder": obj})


def purchaseorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        supplier = request.POST["supplier_id"]
        date = request.POST.get("txtdate")
        total = request.POST.get("txttotal")
        shipping = request.POST.get("txtshipping")
        obj = PurchaseOrder(supplier_id=supplier, order_date=date,
                            total=total, shipping_handling=shipping)
        obj.save()
        return redirect("/purchaseorder")
    supplier = Supplier.objects.all()
    return render(request, 'purchaseorderadd.html', {'supplier': supplier})


def purchaseorderdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = PurchaseOrder.objects.get(purchase_o_id=id)
    ird.delete()
    return redirect("/purchaseorder")


def purchaseorderedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    purchaseorder = PurchaseOrder.objects.get(purchase_o_id=id)
    supplier = Supplier.objects.all()
    return render(request, 'purchaseorderedit.html', {"purchaseorder": purchaseorder, "supplier": supplier})


def purchaseorderupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    purchaseorder = PurchaseOrder.objects.get(purchase_o_id=id)
    purchaseorder.supplier_id = request.POST["supplier_id"]
    purchaseorder.order_date = request.POST.get("txtdate")
    purchaseorder.total = request.POST.get("txttotal")
    purchaseorder.shipping_handling = request.POST.get("txtshipping")
    purchaseorder.save()
    return redirect("/purchaseorder")
    supplier = Supplier.objects.all()
    return render(request, 'purchaseorderadd.html', {'supplier': supplier})


def purchaseorderdetailsshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = PurchaseOrderDetails.objects.all()
    return render(request, 'purchaseorderdetails.html', {"PurchaseOrderDetails": obj})


def purchaseorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        puo = request.POST["purchase_o_id"]
        productdetails = request.POST["product_d_id"]
        price = request.POST.get("txtprice")
        qty = request.POST.get("txtqty")
        description = request.POST.get("txtdis")
        obj = PurchaseOrderDetails(
            purchase_o_id=puo, product_d_id=productdetails, price=price, qty=qty, description=description)
        obj.save()
        return redirect("/purchaseorderdetails")
    puo = PurchaseOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'purchaseorderdetailsadd.html', {'puo': puo, 'productdetails': productdetails})


def purchaseorderdetailsdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = PurchaseOrderDetails.objects.get(purchase_od_id=id)
    ird.delete()
    return redirect("/purchaseorderdetails")


def purchaseorderdetailsedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    purchaseorderdetails = PurchaseOrderDetails.objects.get(purchase_od_id=id)
    puo = PurchaseOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'purchaseorderdetailsedit.html', {"purchaseorderdetails": purchaseorderdetails, "puo": puo,
                                                             "productdetails": productdetails})


def purchaseorderdetailsupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    purchaseorderdetails = PurchaseOrderDetails.objects.get(purchase_od_id=id)
    purchaseorderdetails.purchase_o_id = request.POST["purchase_o_id"]
    purchaseorderdetails.product_d_id = request.POST["product_d_id"]
    purchaseorderdetails.price = request.POST.get("txtprice")
    purchaseorderdetails.qty = request.POST.get("txtqty")
    purchaseorderdetails.description = request.POST.get("txtdis")
    purchaseorderdetails.save()
    return redirect("/productorderdetails")
    puo = PurchaseOrder.objects.all()
    productdetails = ProductDetails.objects.all()
    return render(request, 'purchaseorderdetailsadd.html', {'puo': puo, 'productdetails': productdetails})


def rentordershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = RentOrder.objects.all()
    return render(request, 'rentorder.html', {"RentOrder": obj})


def rentorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        customer = request.POST["customer_id"]
        date = request.POST.get("txtdate")
        total = request.POST.get("txttotal")
        obj = RentOrder(customer_id=customer, order_date=date, total=total)
        obj.save()
        return redirect("/rentorder")
    customer = Customer.objects.all()
    return render(request, 'rentorderadd.html', {'customer': customer})


def rentorderdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = RentOrder.objects.get(rent_o_id=id)
    ird.delete()
    return redirect("/rentorder")


def rentorderedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    rentorder = RentOrder.objects.get(rent_o_id=id)
    customer = Customer.objects.all()
    return render(request, 'rentorderedit.html', {"rentorder": rentorder, "customer": customer})


def rentorderupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    rentorder = RentOrder.objects.get(rent_o_id=id)
    rentorder.customer_id = request.POST["customer_id"]
    rentorder.order_date = request.POST.get("txtdate")
    rentorder.total = request.POST.get("txttotal")
    rentorder.save()
    return redirect("/rentorder")
    customer = Customer.objects.all()
    return render(request, 'rentorderadd.html', {'customer': customer})


def rentorderdetailsshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = RentOrderDetails.objects.all()
    return render(request, 'rentorderdetails.html', {"RentOrderDetails": obj})


def rentorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        rentorder = request.POST["rent_o_id"]
        machinery = request.POST["m_id"]
        discription = request.POST.get("txtdis")
        requirement_days = request.POST.get("txtreqday")
        return_date = request.POST.get("txtretdate")
        price = request.POST.get("txtprice")
        obj = RentOrderDetails(rent_o_id=rentorder, rent_m_id=machinery, description=discription,
                               requirement_days=requirement_days, return_date=return_date, rent_m_charge=price)
        obj.save()
        return redirect("/rentorderdetails")
    rentorder = RentOrder.objects.all()
    machinery = Machinery.objects.all()
    return render(request, 'rentorderdetailsadd.html', {'rentorder': rentorder, 'machinery': machinery})


def rentorderdetailsdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = RentOrderDetails.objects.get(rent_od_id=id)
    ird.delete()
    return redirect("/rentorderdetails")


def rentorderdetailsedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    rentorderdetails = RentOrderDetails.objects.get(rent_od_id=id)
    rentorder = RentOrder.objects.all()
    machorder = Machinery.objects.all()
    return render(request, 'rentorderdetailsedit.html', {"rentorderdetails": rentorderdetails, "rentorder": rentorder,
                     "machorder": machorder})


def rentorderdetailsupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    rentorderdetails = RentOrderDetails.objects.get(rent_od_id=id)
    rentorderdetails.rent_o_id = request.POST["rent_o_id"]
    rentorderdetails.rent_m_id = request.POST["m_id"]
    rentorderdetails.description = request.POST.get("txtdis")
    rentorderdetails.requirement_days = request.POST.get("txtreqday")
    rentorderdetails.return_date = request.POST.get("txtretdate")
    rentorderdetails.rent_m_charge = request.POST.get("txtprice")
    rentorderdetails.save()
    return redirect("/rentorderdetails")
    rentoder = RentOrder.objects.all()
    machorder = Machinery.objects.all()
    return render(request, 'rentorderdetailsadd.html', {'rentoder': rentoder, 'machorder': machorder})


def schedulingshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Scheduling.objects.all()
    return render(request, 'scheduling.html', {"Scheduling": obj})


def schedulingadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        scheduling_date = request.POST.get("txtsd")
        jobworker = request.POST["job_worker_id"]
        service = request.POST["service_o_id"]
        instruction = request.POST.get("txtins")
        status = request.POST.get("txtstatus")
        obj = Scheduling(scheduling_date=scheduling_date, job_worker_id=jobworker,
                               service_o_id=service, instruction=instruction, status=status)
        obj.save()
        return redirect("/scheduling")
    jobworker = JobWorker.objects.all()
    serviceorder = ServiceOrder.objects.all()
    return render(request, 'schedulingadd.html', {'jobworker': jobworker, 'serviceorder': serviceorder})


def schedulingdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = Scheduling.objects.get(scheduling_id=id)
    ird.delete()
    return redirect("/scheduling")


def schedulingedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    scheduling = Scheduling.objects.get(scheduling_id=id)
    jobworker = JobWorker.objects.all()
    serviceorder = ServiceOrder.objects.all()
    return render(request, 'schedulingedit.html', {"scheduling": scheduling, "jobworker": jobworker,
                                                   "serviceorder": serviceorder})


def schedulingupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    scheduling = Scheduling.objects.get(scheduling_id=id)
    scheduling.scheduling_date = request.POST.get("txtsd")
    scheduling.job_worker_id = request.POST["job_worker_id"]
    scheduling.service_o_id = request.POST["service_o_id"]
    scheduling.instruction = request.POST.get("txtins")
    scheduling.status = request.POST.get("txtstatus")
    return redirect("/scheduling")
    jobworker = JobWorker.objects.all()
    serviceorder = ServiceOrder.objects.all()
    return render(request, 'schedulingadd.html', {"scheduling": scheduling, "jobworker": jobworker,
                                                  "serviceorder": serviceorder})


def serviceshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Service.objects.all()
    return render(request, 'service.html', {"Service": obj})


def serviceadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        sname = request.POST.get("txtsname")
        descri = request.POST.get("txtdescri")
        scharge = request.POST.get("txtscharge")
        ssub = request.POST["s_sub_id"]
        obj = Service(service_name=sname, description=descri,
                      service_charge=scharge, s_sub_id=ssub)
        obj.save()
        return redirect("/service")
    sscategory = ServiceCategory.objects.all()
    return render(request, 'serviceadd.html', {'sscategory': sscategory})


def servicedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sid = Service.objects.get(service_id=id)
    sid.delete()
    return redirect("/service")


def serviceedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    service = Service.objects.get(service_id=id)
    sscategory = ServiceCategory.objects.all()
    return render(request, 'serviceedit.html', {"service": service, "sscategory": sscategory})


def serviceupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    service = Service.objects.get(service_id=id)
    service.service_name = request.POST.get("txtsname")
    service.description = request.POST.get("txtdescri")
    service.service_charge = request.POST.get("txtscharge")
    service.s_sub_id = request.POST["s_sub_id"]
    service.save()
    return redirect("/service")
    sscategory = ServiceSubCategory.objects.all()
    return render(request, 'serviceadd.html', {'sscategory': sscategory})


def servicecategoryshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ServiceCategory.objects.all()
    return render(request, 'servicecategory.html', {"ServiceCategory": obj})


def servicecategoryadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        scname = request.POST.get("txtscname")
        descri = request.POST.get("txtdescri")
        obj = ServiceCategory(service_name=scname, description=descri)
        obj.save()
        return redirect("/servicecategory")
    return render(request, 'servicecategoryadd.html')


def servicecategorydelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    scid = ServiceCategory.objects.get(s_category_id=id)
    scid.delete()
    return redirect("/servicecategory")


def servicecategoryedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    servicecategory = ServiceCategory.objects.get(s_category_id=id)
    return render(request, 'servicecategoryedit.html', {"servicecategory": servicecategory})


def servicecategoryupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    servicecategory = ServiceCategory.objects.get(s_category_id=id)
    servicecategory.service_name = request.POST.get('txtscname')
    servicecategory.description = request.POST.get("txtdescri")
    servicecategory.save()
    return redirect("/servicecategory")


def serviceordershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ServiceOrder.objects.all()
    return render(request, 'serviceorder.html', {"ServiceOrder": obj})


def serviceorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        customer = request.POST["customer_id"]
        date = request.POST.get("txtdate")
        total = request.POST.get("txttotal")
        obj = ServiceOrder(customer_id=customer,
                           order_date=date, estimated_total=total)
        obj.save()
        return redirect("/serviceorder")
    customer = Customer.objects.all()
    return render(request, 'serviceorderadd.html', {'customer': customer})


def serviceorderdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = ServiceOrder.objects.get(service_o_id=id)
    ird.delete()
    return redirect("/serviceorder")


def serviceorderedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    serviceorder = ServiceOrder.objects.get(service_o_id=id)
    customer = Customer.objects.all()
    return render(request, 'serviceorderedit.html', {"serviceorder": serviceorder, "customer": customer})


def serviceorderupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    serviceorder = ServiceOrder.objects.get(service_o_id=id)
    serviceorder.customer_id = request.POST["customer_id"]
    serviceorder.order_date = request.POST.get("txtdate")
    serviceorder.estimated_total = request.POST.get("txttotal")
    serviceorder.save()
    return redirect("/serviceorder")
    customer = Customer.objects.all()
    return render(request, 'serviceorderadd.html', {'customer': customer})


def serviceorderdetailsshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = ServiceOrderDetails.objects.all()
    return render(request, 'serviceorderdetails.html', {"ServiceOrderDetails": obj})


def serviceorderdetailsadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        serviceorder = request.POST["service_o_id"]
        service = request.POST["service_id"]
        discription = request.POST.get("txtdis")
        estimated_dimension = request.POST.get("txted")
        price = request.POST.get("txtprice")
        obj = ServiceOrderDetails(service_o_id=serviceorder, service_id=service, description=discription, estimated_dimension=estimated_dimension,
                                  service_charge=price)
        obj.save()
        return redirect("/serviceorderdetails")
    serviceorder = ServiceOrder.objects.all()
    service = Service.objects.all()
    return render(request, 'serviceorderdetailsadd.html', {'serviceorder': serviceorder, 'service': service})


def serviceorderdetailsdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = ServiceOrderDetails.objects.get(service_od_id=id)
    ird.delete()
    return redirect("/serviceorderdetails")


def serviceorderdetailsedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sod = ServiceOrderDetails.objects.get(service_od_id=id)
    serviceorder = ServiceOrder.objects.all()
    service = Service.objects.all()
    return render(request, 'serviceorderdetailsedit.html', {"sod": sod, "serviceorder": serviceorder,
                                                            "service": service})


def serviceorderdetailsupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    serviceorderdetails = ServiceOrderDetails.objects.get(service_od_id=id)
    serviceorderdetails.service_o_id = request.POST["service_o_id"]
    serviceorderdetails.service_id = request.POST["service_id"]
    serviceorderdetails.discription = request.POST.get("txtdis")
    serviceorderdetails.estimated_dimension = request.POST.get("txted")
    serviceorderdetails.service_charge = request.POST.get("txtprice")
    serviceorderdetails.save()
    return redirect("/serviceorderdetails")
    serviceorder = ServiceOrder.objects.all()
    service = Service.objects.all()
    return render(request, 'serviceorderdetailsadd.html', {'serviceorder': serviceorder, 'service': service})

def shadeshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Shade.objects.all()
    return render(request, 'shade.html', {"Shade": obj})


def shadeadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        sname = request.POST.get("txtsname")
        obj = Shade(shade_name=sname)
        obj.save()
        return redirect("/shade")
    return render(request, 'shadeadd.html')


def shadedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sid = Shade.objects.get(shade_id=id)
    sid.delete()
    return redirect("/shade")


def shadeedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    shade = Shade.objects.get(shade_id=id)
    return render(request, 'shadeedit.html', {"shade": shade})


def shadeupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    shade = Shade.objects.get(shade_id=id)
    shade.shade_name = request.POST.get('txtsname')
    shade.save()
    return redirect("/shade")


def sizeshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Size.objects.all()
    return render(request, 'size.html', {"Size": obj})


def sizeadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        size = request.POST.get("txtsize")
        unitid = request.POST["unit_id"]
        obj = Size(size=size, unit_id=unitid)
        obj.save()
        return redirect("/size")
    unit = Unit.objects.all()
    return render(request, 'sizeadd.html', {'unit': unit})


def sizedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sizeid = Size.objects.get(size_id=id)
    sizeid.delete()
    return redirect("/size")


def sizeedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    size = Size.objects.get(size_id=id)
    unit = Unit.objects.all()
    return render(request, 'sizeedit.html', {"size": size, "unit": unit})


def sizeupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    size = Size.objects.get(size_id=id)
    size.size = request.POST.get("txtsize")
    size.unit_id = request.POST["unit_id"]
    size.save()
    return redirect("/size")
    unit = Unit.objects.all()
    return render(request, 'sizeadd.html', {'unit': unit})


def stateshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = State.objects.all()
    return render(request, 'state.html', {"State": obj})


def stateadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        sname = request.POST.get("txtsname")
        obj = State(state_name=sname)
        obj.save()
        return redirect("/state")
    return render(request, 'stateadd.html')


def statedelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sid = State.objects.get(state_id=id)
    sid.delete()
    return redirect("/state")


def stateedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    state = State.objects.get(state_id=id)
    return render(request, 'stateedit.html', {"state": state})


def stateupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    state = State.objects.get(state_id=id)
    state.state_name = request.POST.get('txtsname')
    state.save()
    return redirect("/state")


def stockshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Stock.objects.all()
    return render(request, 'stock.html', {"Stock": obj})


def stockadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        product = request.POST["product_id"]
        qty = request.POST.get("txtqty")
        totaldate = request.POST.get("txttd")
        totaltype = request.POST.get("txtdt")
        obj = Stock(product_id=product, qty=qty,
                    total_date=totaldate, total_type=totaltype)
        obj.save()
        return redirect("/stock")
    product = Product.objects.all()
    return render(request, 'stockadd.html', {'product': product})


def stockdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    ird = Stock.objects.get(stock_id=id)
    ird.delete()
    return redirect("/stock")


def stockedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    stock = Stock.objects.get(stock_id=id)
    product = Product.objects.all()
    return render(request, 'stockedit.html', {"stock": stock, "product": product})


def stockupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    stock = Stock.objects.get(stock_id=id)
    stock.product_id = request.POST["product_id"]
    stock.qty = request.POST.get("txtqty")
    stock.total_date = request.POST.get("txttd")
    stock.total_type = request.POST.get("txtdt")
    stock.save()
    return redirect("/stock")
    product = Product.objects.all()
    return render(request, 'stockadd.html', {'product': product})


def suppliershow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Supplier.objects.all()
    return render(request, 'supplier.html', {"Supplier": obj})


def supplieradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        supplier_name = request.POST.get("txtsname")
        company_name = request.POST.get("txtcname")
        address = request.POST.get("txtadd")
        contact_no = request.POST.get("txtcont")
        email_id = request.POST.get("txtemail")
        obj = Supplier(company_name=company_name, supplier_name=supplier_name, address=address,
                       contact_no=contact_no, email_id=email_id)
        obj.save()
        return redirect("/supplier")
    return render(request, 'supplieradd.html')


def supplierdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    sid = Supplier.objects.get(supplier_id=id)
    sid.delete()
    return redirect("/supplier")


def supplieredit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    supplier = Supplier.objects.get(supplier_id=id)
    return render(request, 'supplieredit.html', {"supplier": supplier})


def supplierupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    supplier = Supplier.objects.get(supplier_id=id)
    supplier.supplier_name = request.POST.get('txtsname')
    supplier.company_name = request.POST.get("txtcname")
    supplier.address = request.POST.get("txtadd")
    supplier.contact_no = request.POST.get("txtcont")
    supplier.email_id = request.POST.get("txtemail")
    supplier.save()
    return redirect("/supplier")


def unitshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Unit.objects.all()
    return render(request, 'unit.html', {"Unit": obj})


def unitadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        uname = request.POST.get("txtuname")
        obj = Unit(unit_name=uname)
        obj.save()
        return redirect("/unit")
    return render(request, 'unitadd.html')


def unitdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    uid = Unit.objects.get(unit_id=id)
    uid.delete()
    return redirect("/unit")


def unitedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    unit = Unit.objects.get(unit_id=id)
    return render(request, 'unitedit.html', {"unit": unit})


def unitupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    unit = Unit.objects.get(unit_id=id)
    unit.unit_name = request.POST.get('txtuname')
    unit.save()
    return redirect("/unit")


def workshow(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    obj = Work.objects.all()
    return render(request, 'work.html', {"Work": obj})


def workadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    if request.method == "POST":
        wname = request.POST.get("txtwname")
        obj = Work(work_name=wname)
        obj.save()
        return redirect("/work")
    return render(request, 'workadd.html')


def workdelete(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    wid = Work.objects.get(work_id=id)
    wid.delete()
    return redirect("/work")


def workedit(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    work = Work.objects.get(work_id=id)
    return render(request, 'workedit.html', {"work": work})


def workupdate(request, id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect('/login/')
    work = Work.objects.get(work_id=id)
    work.work_name = request.POST.get('txtwname')
    work.save()
    return redirect("/work")
