"""paint_solutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jkpaints import views
from django.conf.urls.static import static
from paint_solutions import settings
urlpatterns = [

#---------------------------------------------------------------------------------------------------
# ===================================== Users Urls =================================================
#---------------------------------------------------------------------------------------------------

    path('userlogin/',views.userlogin),
    path('user/',views.userpage),
    path('productlist/',views.productlist),
    path('productdetailslist/<int:id>/',views.productdetailslist),
    path('proddetails/<int:id>/', views.proddetails),








#---------------------------------------------------------------------------------------------------
# ===================================== Admin URls =================================================
#---------------------------------------------------------------------------------------------------

    path('home/',views.adminpage),
    path('login/',views.login),


    path('admin/', views.adminshow),
    path('adminadd/', views.adminadd),
    path('admindelete/<int:id>/', views.admindelete),
    path('adminedit/<int:id>/', views.adminedit),
    path('adminupdate/<int:id>/', views.adminupdate),

    path('area/',views.areashow),
    path('areaadd/',views.areaadd),
    path('areadelete/<int:id>/', views.areadelete),
    path('areaedit/<int:id>/', views.areaedit),
    path('areaupdate/<int:id>/', views.areaupdate),

    path('brand/',views.brandshow),
    path('brandadd/', views.brandadd),
    path('branddelete/<int:id>/', views.branddelete),
    path('brandedit/<int:id>/', views.brandedit),
    path('brandupdate/<int:id>/', views.brandupdate),

    path('city/',views.cityshow),
    path('cityadd/', views.cityadd),
    path('citydelete/<int:id>/', views.citydelete),
    path('cityedit/<int:id>/', views.cityedit),
    path('cityupdate/<int:id>/', views.cityupdate),

    path('customer/',views.customershow),
    path('customeradd/', views.customeradd),
    path('customerdelete/<int:id>/', views.customerdelete),
    path('customeredit/<int:id>/', views.customeredit),
    path('customerupdate/<int:id>/', views.customerupdate),

    path('finish/',views.finishshow),
    path('finishadd/', views.finishadd),
    path('finishdelete/<int:id>/', views.finishdelete),
    path('finishedit/<int:id>/', views.finishedit),
    path('finishupdate/<int:id>/', views.finishupdate),


    path('form/',views.formshow),
    path('formadd/',views.formadd),
    path('formdelete/<int:id>/', views.formdelete),
    path('formedit/<int:id>/', views.formedit),
    path('formupdate/<int:id>/', views.formupdate),


    path('invoice/',views.invoiceshow),
    path('invoiceadd/',views.invoiceadd),
    path('invoicedelete/<int:id>/', views.invoicedelete),
    path('invoiceedit/<int:id>/', views.invoiceedit),
    path('invoiceupdate/<int:id>/', views.invoiceupdate),

    path('invoicerent/',views.invoicerentshow),
    path('invoicerentadd/',views.invoicerentadd),
    path('invoicerentdelete/<int:id>/', views.invoicerentdelete),
    path('invoicerentedit/<int:id>/', views.invoicerentedit),
    path('invoicerentupdate/<int:id>/', views.invoicerentupdate),

    path('invoiceservice/',views.invoiceserviceshow),
    path('invoiceserviceadd/',views.invoiceserviceadd),
    path('invoiceservicedelete/<int:id>/', views.invoiceservicedelete),
    path('invoiceserviceedit/<int:id>/', views.invoiceserviceedit),
    path('invoiceserviceupdate/<int:id>/', views.invoiceserviceupdate),

    path('jobworker/',views.jobworkershow),
    path('jobworkeradd/', views.jobworkeradd),
    path('jobworkerdelete/<int:id>/', views.jobworkerdelete),
    path('jobworkeredit/<int:id>/', views.jobworkeredit),
    path('jobworkerupdate/<int:id>/', views.jobworkerupdate),

    path('machinery/',views.machineryshow),
    path('machineryadd/',views.machineryadd),
    path('machinerydelete/<int:id>/', views.machinerydelete),
    path('machineryedit/<int:id>/', views.machineryedit),
    path('machineryupdate/<int:id>/', views.machineryupdate),


    path('offer/',views.offershow),
    path('offeradd/',views.offeradd),
    path('offerdelete/<int:id>/', views.offerdelete),
    path('offeredit/<int:id>/', views.offeredit),
    path('offerupdate/<int:id>/', views.offerupdate),

    path('pcategory/',views.pcategoryshow),
    path('pcategoryadd/',views.pcategoryadd),
    path('pcategorydelete/<int:id>/', views.pcategorydelete),
    path('pcategoryedit/<int:id>/', views.pcategoryedit),
    path('pcategoryupdate/<int:id>/', views.pcategoryupdate),

    path('payment/',views.paymentshow),
    path('paymentadd/', views.paymentadd),
    path('paymentdelete/<int:id>/', views.paymentdelete),
    path('paymentedit/<int:id>/', views.paymentedit),
    path('paymentupdate/<int:id>/', views.paymentupdate),

    path('product/',views.productshow),
    path('productadd/', views.productadd),
    path('productdelete/<int:id>/', views.productdelete),
    path('productedit/<int:id>/', views.productedit),
    path('productupdate/<int:id>/', views.productupdate),
 
    path('productdetails/',views.productdetailsshow),
    path('productdetailsadd/', views.productdetailsadd),
    path('productdetailsdelete/<int:id>/', views.productdetailsdelete),
    path('productdetailsedit/<int:id>/', views.productdetailsedit),
    path('productdetailsupdate/<int:id>/', views.productdetailsupdate),

    path('productorder/',views.productordershow),
    path('productorderadd/', views.productorderadd),
    path('productorderdelete/<int:id>/', views.productorderdelete),
    path('productorderedit/<int:id>/', views.productorderedit),
    path('productorderupdate/<int:id>/', views.productorderupdate),

    path('productorderdetails/', views.productorderdetailsshow),
    path('productorderdetailsadd/', views.productorderdetailsadd),
    path('productorderdetailsdelete/<int:id>/', views.productorderdetailsdelete),
    path('productorderdetailsedit/<int:id>/', views.productorderdetailsedit),
    path('productorderdetailsupdate/<int:id>/', views.productorderdetailsupdate),

    path('ptype/',views.ptypeshow),
    path('ptypeadd/',views.ptypeadd),
    path('ptypedelete/<int:id>/', views.ptypedelete),
    path('ptypeedit/<int:id>/', views.ptypeedit),
    path('ptypeupdate/<int:id>/', views.ptypeupdate),

    path('purchaseorder/', views.purchaseordershow),
    path('purchaseorderadd/', views.purchaseorderadd),
    path('purchaseorderdelete/<int:id>/', views.purchaseorderdelete),
    path('purchaseorderedit/<int:id>/', views.purchaseorderedit),
    path('purchaseorderupdate/<int:id>/', views.purchaseorderupdate),


    path('purchaseorderdetails/', views.purchaseorderdetailsshow),
    path('purchaseorderdetailsadd/', views.purchaseorderdetailsadd),
    path('purchaseorderdetailsdelete/<int:id>/', views.purchaseorderdetailsdelete),
    path('purchaseorderdetailsedit/<int:id>/', views.purchaseorderdetailsedit),
    path('purchaseorderdetailsupdate/<int:id>/', views.purchaseorderdetailsupdate),


    path('rentorder/', views.rentordershow),
    path('rentorderadd/', views.rentorderadd),
    path('rentorderdelete/<int:id>/', views.rentorderdelete),
    path('rentorderedit/<int:id>/', views.rentorderedit),
    path('rentorderupdate/<int:id>/', views.rentorderupdate),


    path('rentorderdetails/', views.rentorderdetailsshow),
    path('rentorderdetailsadd/', views.rentorderdetailsadd),
    path('rentorderdetailsdelete/<int:id>/', views.rentorderdetailsdelete),
    path('rentorderdetailsedit/<int:id>/', views.rentorderdetailsedit),
    path('rentorderdetailsupdate/<int:id>/', views.rentorderdetailsupdate),

    path('scheduling/', views.schedulingshow),
    path('schedulingadd/', views.schedulingadd),
    path('schedulingdelete/<int:id>/', views.schedulingdelete),
    path('schedulingedit/<int:id>/', views.schedulingedit),
    path('schedulingupdate/<int:id>/', views.schedulingupdate),

    path('service/', views.serviceshow),
    path('serviceadd/', views.serviceadd),
    path('servicedelete/<int:id>/', views.servicedelete),
    path('serviceedit/<int:id>/', views.serviceedit),
    path('serviceupdate/<int:id>/', views.serviceupdate),

    path('servicecategory/',views.servicecategoryshow),
    path('servicecategoryadd/',views.servicecategoryadd),
    path('servicecategorydelete/<int:id>/', views.servicecategorydelete),
    path('servicecategoryedit/<int:id>/', views.servicecategoryedit),
    path('servicecategoryupdate/<int:id>/', views.servicecategoryupdate),

    path('serviceorder/', views.serviceordershow),
    path('serviceorderadd/', views.serviceorderadd),
    path('serviceorderdelete/<int:id>/', views.serviceorderdelete),
    path('serviceorderedit/<int:id>/', views.serviceorderedit),
    path('serviceorderupdate/<int:id>/', views.serviceorderupdate),

    path('serviceorderdetails/', views.serviceorderdetailsshow),
    path('serviceorderdetailsadd/', views.serviceorderdetailsadd),
    path('serviceorderdetailsdelete/<int:id>/', views.serviceorderdetailsdelete),
    path('serviceorderdetailsedit/<int:id>/', views.serviceorderdetailsedit),
    path('serviceorderdetailsupdate/<int:id>/', views.serviceorderdetailsupdate),

    path('servicesubcategory/',views.servicesubcategoryshow),
    path('servicesubcategoryadd/', views.servicesubcategoryadd),
    path('servicesubcategorydelete/<int:id>/', views.servicesubcategorydelete),
    path('servicesubcategoryedit/<int:id>/', views.servicesubcategoryedit),
    path('servicesubcategoryupdate/<int:id>/', views.servicesubcategoryupdate),

    path('shade/',views.shadeshow),
    path('shadeadd/',views.shadeadd),
    path('shadedelete/<int:id>/', views.shadedelete),
    path('shadeedit/<int:id>/', views.shadeedit),
    path('shadeupdate/<int:id>/', views.shadeupdate),

    path('size/', views.sizeshow),
    path('sizeadd/', views.sizeadd),
    path('sizedelete/<int:id>/', views.sizedelete),
    path('sizeedit/<int:id>/', views.sizeedit),
    path('sizeupdate/<int:id>/', views.sizeupdate),

    path('state/',views.stateshow),
    path('stateadd/',views.stateadd),
    path('statedelete/<int:id>/', views.statedelete),
    path('stateedit/<int:id>/', views.stateedit),
    path('stateupdate/<int:id>/', views.stateupdate),

    path('stock/', views.stockshow),
    path('stockadd/',views.stockadd),
    path('stockdelete/<int:id>/', views.stockdelete),
    path('stockedit/<int:id>/', views.stockedit),
    path('stockupdate/<int:id>/', views.stockupdate),


    path('supplier/', views.suppliershow),
    path('supplieradd/',views.supplieradd),
    path('supplierdelete/<int:id>/', views.supplierdelete),
    path('supplieredit/<int:id>/', views.supplieredit),
    path('supplierupdate/<int:id>/', views.supplierupdate),

    path('unit/', views.unitshow),
    path('unitadd/',views.unitadd),
    path('unitdelete/<int:id>/', views.unitdelete),
    path('unitedit/<int:id>/', views.unitedit),
    path('unitupdate/<int:id>/', views.unitupdate),

    path('work/', views.workshow),
    path('workadd/',views.workadd),
    path('workdelete/<int:id>/', views.workdelete),
    path('workedit/<int:id>/', views.workedit),
    path('workupdate/<int:id>/', views.workupdate),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

