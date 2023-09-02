from django.shortcuts import render , redirect
from django.contrib import messages 
from cryptography.fernet import Fernet
from.models import *
import requests

# Create your views here.
# When th user want to signup that time this function call 

def signup(request):
    try : 
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            contact = request.POST["contact"]
            password = request.POST["password"] 
            repassword = request.POST["repassword"]
            fil_email = Useraccount.objects.filter(email = email)
            fil_contact = Useraccount.objects.filter(contact = contact)
            if fil_email.exists():
                messages.error(request, "Email already Exists....!")
            elif name  == "" :
                messages.error(request , "name is required...")
            elif  email == "" :
                messages.error(request,"Email id is Required....!")
            elif contact == "" :
                messages.error(request ,"Contact number Is Requiered...!! ")
            elif  fil_contact.exists():
                messages.error(request, "Contact already Exists ")
            elif len(password) >=8 and password == repassword :  
                print("pass")
                passwordkey = Fernet.generate_key()
                fernet =  Fernet(passwordkey)
                encpassword = fernet.encrypt(password.encode()) 
                Useraccount(name = name, 
                            email = email,
                            contact=contact,
                            password=encpassword.decode('utf-8'),
                            password_key = passwordkey.decode('utf-8')).save()
                print("pass2")
                messages.success(request,'Registration Successfully .. !!')
                return redirect("login")
            else: 
                messages.error(request,'Password Does not match..!')
        return render(request , "Signup.html")
    except Exception as e  :
        messages.error(e)




def loginwithemail(request):
    try :
        if request.method == "POST" :
            email = request.POST["email"]
            password = request.POST["password"]
            if email == "" :
                messages.error(request , "Enter Email....!")
            elif password == "":
                messages.error(request , "Enter Password...!")
            user_data  = Useraccount.objects.get(email=email)
            if email != "" and password != "" :
                if user_data:
                    fernet = Fernet(user_data.password_key)
                    decpassword = fernet.decrypt(user_data.password).decode()
                    if password == decpassword :
                        session_id = request.session["username"] = user_data.name
                        session_id = request.session["id"] = user_data.id
                        print("session_id",session_id)
                        messages.success(request,"Login Successfully !!")
                        return redirect("home") 
                    else:
                        messages.error(request,"Incorrect password !!") 
                        return redirect('login') 
                else:
                    messages.error(request," Please enetr valid Email.. !!")
                    return redirect('login')    
        return render(request,'Login.html')
    except Exception as e :
        print(e)
        return redirect("login")
      
       
   

# def loginwithcontact(request):
#      return render(request, "Login.html",{"contact" : "contact"})

# When the user want to Logout here account then  this function work 
def userlogout(request):
    try :
        del request.session["id"]
        messages.error(request, "Logout Successfully...!")
    except Exception as e :
        print(e)
    return redirect("login")



# If the user want to forget here  password then thid function is work 

def forgetpassword(request):
    return render(request, "ForgetPassword.html")




# If the user want to change the password then this function is work 
def changepassword(request):
    try : 
        if 'id' in  request.session:
            if request.method == "POST":
                oldpassword = request.POST["oldpassword"]
                newpassword  = request.POST["newpassword"]
                filter_user = Useraccount.objects.filter(id = request.session["id"])
                if filter_user.exists():
                    old_passs = filter_user.values("password_key", "password")[0]
                    print(old_passs)
                    fernet = Fernet(old_passs["password_key"])
                    print("fernate::-",fernet)
                    decpassword = fernet.decrypt(old_passs["password"]).decode()
                    print("decordpassword:--",decpassword)
                    if oldpassword == decpassword:
                        get_pass_key = Fernet.generate_key()
                        new_fernet = Fernet(get_pass_key)
                        encpassword = new_fernet.encrypt(newpassword.encode())
                        filter_user.update(
                            password_key = get_pass_key.decode('utf-8'),
                            password = encpassword.decode('utf-8'))
                        return redirect("login")
                    return render(request, "Changepassword.html")
            else:
                return render(request, "ChangePassword.html")
        else :
            messages.error(request, "Please Login First....")
            return redirect("login")
    except Exception as e :
        print(e)
   




# If the user want to show her profile then this function is work 
def profile(request):
        try :
            if "id" in request.session:
                user = Useraccount.objects.get(id = request.session["id"])
                add = Address.objects.filter(username = request.session["id"])
                print("add" , add)
                return render(request, "Profile.html",{"detail" :user, "edit" : False , "address":add})
            else:
                messages.error(request , "Please login first...! ")
                return redirect("login")
        except Exception as e :
            print(e)
 





def edit_profile(request):
    try:
       
        if request.method == "POST" :
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['contact']
            print("pass")
            fil_user = Useraccount.objects.filter(id = request.session["id"])
            print(fil_user)
            if fil_user.exists:
                print("esxid")
                fil_user.update(
                    name =  name,email = email,contact=contact)
            return redirect("profile")
        else :
            user = Useraccount.objects.get(id = request.session["id"])
        return render( request ,"profile.html" , {"detail": user , "edit":True})
    except Exception as e:    
        print(e)




def viewstate(request):
    url = "https://api.countrystatecity.in/v1/countries"
    headers = {
  'X-CSCAPI-KEY': 'API_KEY'
}
    response = requests.get(url , headers=headers)
    data = response.json()
    print("json", data)

    

def addaddress(request):
    # viewstate(request)
    try :
        if request.method == "POST" :
            print("pass")
            username = Useraccount.objects.get(id= request.session["id"])
            city = request.POST["city"]
            area = request.POST["area"]
            state = request.POST["state"]
            pincode = request.POST["pincode"]
            contact = request.POST["contact"]
            Address(
                username = username ,
                city = city , 
                area = area , 
                state = state , 
                pincode = pincode , 
                contact =contact
            ).save()
            print("hello")
            messages.success(request , "Address added Successfully..! ")
            return redirect("profile")
        return render(request,"Add-Address.html")
    except Exception as e :
        print(e)


def del_address(request , id):
    try :
        fil_address = Address.objects.filter(id = id,username__id = request.session["id"])
        if fil_address .exists():
            fil_address.delete()
            messages.success(request , "Deleted successfully")
            return redirect("profile")
        else:
            messages .error(request , "address not available ")
    except Exception as e  :
        print(e)
    

