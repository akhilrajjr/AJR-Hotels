
from django.shortcuts import redirect, render
from .models import models, rooms
from django.contrib.auth.models import auth, User
from .models import comment, contactus, printpage
import random
from datetime import date, datetime 
# Create your views here.


def index(request):
    sec=rooms.objects.all()
    return render (request,'index.html',{'ksec':sec})    

def about (request):
    return render (request,'about.html')

def blog (request):
    return render (request,'blog.html')

def contact (request):
    return render (request,'contact.html')

def gallery (request):
    return render (request,'gallery.html')

def room1 (request):
    sec=rooms.objects.all()
    return render (request,'room1.html',{'ksec':sec})

#service
def room (request):
    req=request.GET['s']
    obj=rooms.objects.get(id=req)
    return render(request,'room.html',{"obj": obj})

#booking
def book (request):
    req=request.GET['s']
    obj=rooms.objects.get(id=req)
    return render(request,'booking.html',{"obj": obj})
    

#login and logout page
def login1 (request):
    return render (request,'login1.html')

def login2 (request):
    usr =request.POST['uname']
    psd = request.POST['pswd']
    user = auth.authenticate(username = usr,password = psd)
    if user is not None:
        auth.login(request,user)
    else:
        msg = 'Invalid Username !!!'
        return render (request,'login1.html',{'msg':msg})
    return redirect('/')

def logout (request):
    auth.logout(request)
    return render (request,'index.html')


#registration page

def register (request):
    if request.method=='POST':
        unam = request.POST['uname']
        fnam = request.POST['fname']
        lnam = request.POST['lname']
        mail = request.POST['email']
        psd = request.POST['pswd']
        rpsd = request.POST['rpswd']
        if unam != '' and mail != '' and psd != '' and psd == rpsd:
            user = User.objects.create_user(username=unam,first_name=fnam,last_name=lnam,email=mail,password=psd)
            user.save();
            auth.login(request,user)                
            return redirect('/')
        else:
            return render(request,'register.html')
    else:
        return render (request,'register.html')


# BOOKING PROCESS

def booking (request):
    if request.method=='POST':
        username=request.POST['user']
        checkin = request.POST['ckin']
        chectout = request.POST['ckot']
        days = request.POST['days']
        adults = request.POST['adults']
        des= request.POST['des']
        amt= request.POST['amt']
        rom= request.POST['rom']
        pl = request.POST['pl']
        
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        
        ad1='QWERTYUIOPASDFGHJKLZXCVBNM'
        ad2='qwertyuioplkjhgfdsazxcvbnm'
        ad3='0123456789'
        all=ad1+ad2+ad3
        inv=ad1+ad3
        ln=8
        ln1=4
        bookno="".join(random.sample(all,ln))
        invno="".join(random.sample(inv,ln1))
        print('haiiiiiiiiiii',bookno)

        add=int(days)*int(adults)*float(amt)
        gst = add*18/100
        total= add+gst
        print('hiiiiiiiiiiiii',total,add,gst)
        
        booked = printpage.objects.create(booking=bookno,inv=invno,urname=username,checkin=checkin,checkot=chectout,amount=total)
        booked.save();

        return render(request,'confirm.html',{'nam':username,'cin':checkin,'cot':chectout,'days':days,
        'adults':adults,'price':amt,'add':add,'gst':gst,'total':total,'bkno':bookno,
        'rom':rom,'dt':dt,'invno':invno,'des':des,'pl':pl})

    else:
            return render(request,'confirm.html')



#comment functions
def comments(request):
    details=request.POST['body']
    username=request.POST['user']
    serviceid=request.POST['service']
    cmt = comment.objects.create(body=details,name=username,service_id=serviceid)
    cmt.save();
    obj = rooms.objects.get(id=serviceid)
    return render(request,'room.html',{'obj': obj})
    


#contact functions
def contactuspg(request):
    name=request.POST['name']
    mail=request.POST['mail']
    phone=request.POST['phone']
    msg=request.POST['msgs']
    contus = contactus.objects.create(name=name,mail=mail,phone=phone,msg=msg)
    contus.save();
    note= 'We will contact you soon...'
    return render(request,'contact.html',{'note':note})




# BOOKING PROCESS

def printpg (request):
    return render(request,'print.html')