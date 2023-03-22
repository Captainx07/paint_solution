from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'


class Area(models.Model):
    pin_code = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=50)
    city = models.ForeignKey('City', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'area'


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    def __str__(self):
        return self.brand_name

    class Meta:
        managed = False
        db_table = 'brand'

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    product_d = models.ForeignKey('ProductDetails', models.DO_NOTHING)
    qty = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    state = models.ForeignKey('State', models.DO_NOTHING)
    def __str__(self):
        return self.city_name

    class Meta:
        managed = False
        db_table = 'city'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=15)
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    pin_code = models.ForeignKey(Area, models.DO_NOTHING, db_column='pin_code')
    image = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.customer_name

    class Meta:
        managed = False
        db_table = 'customer'


class Finish(models.Model):
    finish_id = models.AutoField(primary_key=True)
    finish_name = models.CharField(max_length=30)
    def __str__(self):
        return self.finish_name
    

    class Meta:
        managed = False
        db_table = 'finish'


class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=30)
    def __str__(self):
        return self.form_name

    class Meta:
        managed = False
        db_table = 'form'


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    invoice_date = models.DateField()
    service_od = models.ForeignKey('ServiceOrderDetails', models.DO_NOTHING, blank=True, null=True)
    rent_od = models.ForeignKey('RentOrderDetails', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceRent(models.Model):
    invoice_r_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    m = models.ForeignKey('Machinery', models.DO_NOTHING)
    days = models.IntegerField()
    rent_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_rent'


class InvoiceService(models.Model):
    invoice_s_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    service = models.ForeignKey('Service', models.DO_NOTHING)
    dimension = models.IntegerField()
    service_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_service'


class JobWorker(models.Model):
    job_worker_id = models.AutoField(primary_key=True)
    worker_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    work = models.ForeignKey('Work', models.DO_NOTHING)
    def __str__(self):
        return self.worker_name
    

    class Meta:
        managed = False
        db_table = 'job_worker'


class Machinery(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    rent_charge = models.IntegerField()
    machinery_work = models.CharField(max_length=400)
    image = models.CharField(max_length=400, blank=True, null=True)
    def __str__(self):
        return self.m_name

    class Meta:
        managed = False
        db_table = 'machinery'


class Machinerycart(models.Model):
    machcart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    m = models.ForeignKey(Machinery, models.DO_NOTHING)
    description = models.CharField(max_length=500)
    qty = models.IntegerField()
    price = models.IntegerField()
    requirement_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'machinerycart'


class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_code = models.CharField(max_length=30)
    min_amount = models.IntegerField(blank=True, null=True)
    discount = models.CharField(max_length=30)
    max_discount = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.DateField(blank=True, null=True)
    no_of_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'


class PCategory(models.Model):
    p_category_id = models.AutoField(primary_key=True)
    p_category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.p_category_name

    class Meta:
        managed = False
        db_table = 'p_category'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    p_date = models.DateField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    p_category = models.ForeignKey(PCategory, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('Ptype', models.DO_NOTHING, blank=True, null=True)
    form = models.ForeignKey(Form, models.DO_NOTHING, blank=True, null=True)
    finish = models.ForeignKey(Finish, models.DO_NOTHING, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    covering_capacity = models.CharField(max_length=40,blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.product_name

    class Meta:
        managed = False
        db_table = 'product'


class ProductDetails(models.Model):
    product_d_id = models.AutoField(primary_key=True)
    shade = models.ForeignKey('Shade', models.DO_NOTHING, blank=True, null=True)
    size = models.ForeignKey('Size', models.DO_NOTHING)
    price = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_details'


class ProductOrder(models.Model):
    product_o_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    date = models.DateField()
    offer = models.ForeignKey(Offer, models.DO_NOTHING, blank=True, null=True)
    total = models.IntegerField()
    shipping_handling = models.IntegerField()
    track_url = models.CharField(max_length=40, blank=True, null=True)
    track_no = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_order'


class ProductOrderDetails(models.Model):
    product_od_id = models.AutoField(primary_key=True)
    product_o = models.ForeignKey(ProductOrder, models.DO_NOTHING)
    product_d = models.ForeignKey(ProductDetails, models.DO_NOTHING)
    price = models.IntegerField()
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_order_details'


class Ptype(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=30)
    def __str__(self):
        return self.type_name

    class Meta:
        managed = False
        db_table = 'ptype'


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    order_date = models.DateField()
    total = models.IntegerField()
    shipping_handling = models.IntegerField()
    purchase_o_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderDetails(models.Model):
    purchase_od_id = models.AutoField(primary_key=True)
    purchase_o = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
    product_d = models.ForeignKey(ProductDetails, models.DO_NOTHING)
    description = models.CharField(max_length=400)
    qty = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase_order_details'


class RentOrder(models.Model):
    rent_o_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    order_date = models.DateField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rent_order'


class RentOrderDetails(models.Model):
    rent_od_id = models.AutoField(primary_key=True)
    rent_o = models.ForeignKey(RentOrder, models.DO_NOTHING)
    rent_m = models.ForeignKey(Machinery, models.DO_NOTHING)
    description = models.CharField(max_length=300)
    qty = models.IntegerField()
    requirement_days = models.IntegerField()
    return_date = models.DateField(blank=True, null=True)
    rent_m_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rent_order_details'


class Scheduling(models.Model):
    scheduling_id = models.AutoField(primary_key=True)
    scheduling_date = models.DateField()
    job_worker = models.ForeignKey(JobWorker, models.DO_NOTHING)
    service_o = models.ForeignKey('ServiceOrder', models.DO_NOTHING)
    instruction = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'scheduling'


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    service_charge = models.IntegerField()
    s_category = models.ForeignKey('ServiceCategory', models.DO_NOTHING)
    image = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceCategory(models.Model):
    s_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'service_category'


class ServiceOrder(models.Model):
    service_o_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    order_date = models.DateField()
    estimated_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_order'


class ServiceOrderDetails(models.Model):
    service_od_id = models.AutoField(primary_key=True)
    service_o = models.ForeignKey(ServiceOrder, models.DO_NOTHING)
    service = models.ForeignKey(Service, models.DO_NOTHING)
    description = models.CharField(max_length=500)
    estimated_dimension = models.IntegerField()
    service_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_order_details'

class Servicecart(models.Model):
    scart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    service = models.ForeignKey(Service, models.DO_NOTHING)
    estimation = models.IntegerField()
    charges = models.IntegerField()
    description = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'servicecart'

class Shade(models.Model):
    shade_id = models.AutoField(primary_key=True)
    shade_name = models.CharField(max_length=30)
    def __str__(self):
        return self.shade_name
    

    class Meta:
        managed = False
        db_table = 'shade'


class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size = models.IntegerField()
    unit = models.ForeignKey('Unit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'size'


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30)
    def __str__(self):
        return self.state_name
    class Meta:
        managed = False
        db_table = 'state'


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    qty = models.IntegerField()
    total_date = models.DateField()
    total_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'stock'


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=40)
    supplier_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15)
    email_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'supplier'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=30)
    
    class Meta:
        managed = False
        db_table = 'unit'


class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    work_name = models.CharField(max_length=30)
    def __str__(self):
        return self.work_name

    class Meta:
        managed = False
        db_table = 'work'
