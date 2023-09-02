from django.shortcuts import render , redirect
from django.contrib import messages 
from.models import *
from User .models import *
import json
import razorpay



# Create your views here.
def home(request):
    try :
        product = Product.objects.filter(productName = 	"Mens-Pants")[:4]
        print(product)
        product2 = Product.objects.filter(productName ="laptop")[:6]
    except Exception as e :
        print (e)
    if product.exists():
        return render(request, "Home.html",{"product":product , "product2":product2})

def shopping(request):
    try :
        query = request.GET.get("query")
        if query is not None :
            print(query)
            product_detail = Product.objects.filter(title__icontains = query)
            product_brand = Product.objects.filter(productName__icontains = query)
            product = product_detail.union(product_brand)
            print("product_detail",product_detail)
            return render(request, "Shopping.html",{"product":product})
        else :
            product = Product.objects.all()
            return render(request ,"Shopping.html",{"product":product} )
    except Exception as e :
        print(e)





def viewproduct(request , id):
    try:
        product = Product.objects.get(id=id)
        produ =  product.about
        # print(type(produ), produ)
        # data = json.loads(produ)
        # print("daaa", data)

        cart_status = AddtoCart.objects.filter(product__id = id)
        status = False
        if cart_status.exists():
            status =  True
    except Exception as e:
        print(e)
    return render(request, "Singleproduct.html" , {"product" : product , "cart":status})

# When the user want to cart the item that time the this function is work 
def cartpage(request):
    try :
        if  'id' in request.session:
            discount_price = 0
            delivery_charges = 60
            subtotal_price = 0
            total_item = 0
            total_price = 0
            cart_product = AddtoCart.objects.filter(username__id = request.session["id"])
            print(cart_product)
            viewproduct = True 
            if len(cart_product) <= 0 :
                viewproduct = False
                return render(request ,"Add-to-cart.html", {"cartproduct":cart_product, "viewproduct":viewproduct})
            else:
                for i in cart_product :
                    total_item = total_item + i.quantity
                    print("sss", i.product.actual_price * i.quantity)
                    subtotal_price = subtotal_price + (i.product.actual_price * i.quantity)
                    discount_price = discount_price + (i.product.discount_price * i.quantity) 
                    print("ddd",i.product.discount_price)
                dis = subtotal_price - discount_price
                total_price = subtotal_price - dis + delivery_charges  
            return render(request, "Add-to-Cart.html",{"cartproduct":cart_product,
                                                        "viewproduct":viewproduct , "total_price":subtotal_price ,
                                                        "discount_price":dis , "delivery_charges":delivery_charges , "total":total_price , "total_item":total_item})         
        else :
            messages.error(request, "Please Login first ....")
            return  redirect("login")
    except Exception as e :
        print(e)



def add_to_cart(request):
    try :
        if request.method == "POST":
            print("passs")
            product_id = request.POST["product"]
            quantity = request.POST["quantity"]
            print(type(product_id))
            fil_product = Product.objects.get(id = product_id)
            fil_add_tocart_produt = AddtoCart.objects.filter(product__id = product_id)
            if fil_add_tocart_produt.exists():
                print("achii",fil_add_tocart_produt)
            else :
                user = Useraccount.objects.get(id = request.session["id"])
                AddtoCart(
                    username = user,
                    product = fil_product , 
                    quantity = int(quantity),
                    total_price = fil_product.discount_price * int(quantity)
                ).save()
            messages.success(request, "Cart Successfully")
            return redirect("cartpage")
    except Exception as e :
        print(e)





def increate_item(request):
    try :
        if request.method == "POST":
            item_id  = request.POST["item_id"]
            cart_id = request.POST["cart_id"]
            increase = request.POST["plus"]
            user = AddtoCart.objects.filter(username__id=request.session["id"],id = cart_id)
            if user.exists():
                cart_item = AddtoCart.objects.get(id = cart_id)
                increas = cart_item.quantity + int(increase)
                product = Product.objects.get(id=int(item_id))
                user.update(
                    quantity = int(increas),
                    total_price =  product.discount_price * increas
                )
        return redirect("cartpage")
    except Exception as e :
        print(e)




def decrease_item(request):
    try :
        if request.method == "POST":
            item_id  = request.POST["item_id"]
            cart_id = request.POST["cart_id"]
            decrease = request.POST["minus"]
            user = AddtoCart.objects.filter(username__id=request.session["id"],id = cart_id)
            if user.exists():
                cart_item = AddtoCart.objects.get(id = cart_id)
                product = Product.objects.get(id=int(item_id))
                if cart_item.quantity > 1 :
                    increas = cart_item.quantity - int(decrease)
                    user.update(
                    quantity = int(increas),
                    total_price =  product.discount_price * increas)        
                    return redirect("cartpage")
            else:
                return redirect("cartpage")
    except Exception as e :
        print(e)




# Remove the cart Item 

def remove_cart_item(request):
    try : 
        if request.method == "POST":
            id = request.POST['remove_cart_item']
            AddtoCart.objects.filter(id=int(id)).delete()
            return redirect("cartpage")
    except Exception as e:
        print(e)


def buy_now(request):
    try :
        if  'id' in request.session:
            if request.method == "POST":
                product = request.POST["product"]
                produt_id = Product.objects.get(id=int(product)) 
                user = Useraccount.objects.get(id=request.session["id"])
                order_id = OrderDetail(
                    user = user,
                    product = produt_id, 
                    buynow_status = True 
                )
                order_id.save()
                print("sdsd", order_id.id)
                request.session["order_id"] = order_id.id
        else :
            return redirect("login")
    except Exception as e:
        print(e)
    return redirect("select-address")

   


# here When the user want  to buy any product  if he want to change the address or selecet any address that time this function worhk

def select_address(request):
    try :
        login_user_address = Address.objects.filter(username_id=request.session["id"])
        order_detail = OrderDetail.objects.get(id=request.session["order_id"])
        total_price = order_detail.product.actual_price - order_detail.product.discount_price + 60
        print( order_detail.product.actual_price,order_detail.product.discount_price)
        print(order_detail)
    except Exception as e :
        print(e)
    return render(request,"SelectAddress.html", {"address":login_user_address ,"order":order_detail,"total":total_price})



def add_order_address(request):
    try :
        if request.method == "POST":
            address = request.POST["address"]
            print(address)
            view_address = Address.objects.get(id=int(address))
            order = OrderDetail.objects.filter(id=request.session["order_id"])
            if order.exists():
                order.update(
                    address = view_address, 
                    address_status = True)
                return redirect("select-address")
    except Exception as e :
        print(e)





def change_address(request):
    order_detail = OrderDetail.objects.filter(id=request.session["order_id"])
    if order_detail.exists():
        order_detail.update(
            address_status = False
        )
        messages.success(request,"Addres Updated....!")
    return redirect("select-address")

def cash_on_delivery(reqeust):
    return render(reqeust, "Payment-Section.html")


def razor_pay(request):
    try :
        if request.method == "POST" :
            payment = request.POST["payment"]
            print(payment)
            client = razorpay.Client(auth=('rzp_test_sT94LT9dyhA0BF', 'ZhsELWxsKwEteIen79LRcWY1'))
            DATA = {
            "amount": int(payment) * 100 ,
            "currency": "INR",
            }
            response = client.order.create(data=DATA)
            print(response)
        order = OrderDetail.objects.filter(id=request.session["order_id"])
        if order.exists():
            order.update(
                order_id = response["id"],
                total_price = payment ,
                payment_method = "ROZERPAY",
                payment_status = True
            )
        return redirect("select-address")
    except Exception as e :
        print(e)


def payment_success(request):
    try :
        response = request.POST
        print(response)
    except Exception as e :
        print(e)    
    return render(request , 'Successfull.html')






def customerservice(request):
    return render(request,"Customer.html")

