from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
# import simplejson as json
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
import smtplib 
import urllib.request
import webbrowser
import random


conn = MySQLdb.connect("localhost","root","","legal_advisor")
c = conn.cursor()

# def sendsms(ph,msg):

#     sendToPhoneNumber= "+91"+ph
#     userid = "2000022557"
#     passwd = "54321@lcc"
#     url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    # webbrowser.open(url)


# Create your views here.
def index(request):
    if 'login' in request.POST:
        return HttpResponseRedirect("/login")
    return render(request,"index.html")

def login(request):
    if 'login' in request.POST:
        name = request.POST.get("name")
        password = request.POST.get("password")
        st="1"
        s1 = "select * from login where username = '"+str(name)+"' and password= '"+str(password)+"' and status='"+str(st)+"'"
        print(s1)
        c.execute(s1)
        log_count = c.fetchone()
        print(log_count)

        if not bool(log_count):
            msg = "User Does Not Exists"
            return render(request,"login.html",{"msg":msg})
            
        if log_count[4] == 'admin' :

            return HttpResponseRedirect("/admin_home")
        
        if log_count[4] == 'advocate' :
            request.session["adv_id"] = log_count[1]

            return HttpResponseRedirect("/adv_home")

        elif log_count[4] == 'user' :
            request.session["uid"] = log_count[1]
            return HttpResponseRedirect("/user_home")
        
        # return render(request,"user_register.html")
    return render(request,"login.html")

def adv_register(request):
    s = "select * from category"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print("-----------------------inside advocate register-------------------------")
    if 'submit' in request.POST:
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        enr_id = request.POST.get("enr_id")
        qual = request.POST.get("qual")
        category = request.POST.get("category")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")

        s1 = "select count(*) from advocate where adv_email = '"+str(email)+"' or adv_enroll_no= '"+str(enr_id)+"' or adv_phone = '"+str(phone)+"'"
        print(s1)
        c.execute(s1)
        reg_count = c.fetchone()

        if reg_count[0] == 0 :
            s2 = "insert into advocate(`adv_img`,`adv_name`,`adv_enroll_no`,`adv_qual`,`adv_age`,`adv_gender`,`adv_email`,`adv_phone`,`adv_address`,`adv_category`) values('"+str(uploaded_file_url)+"','"+str(name)+"','"+str(enr_id)+"','"+str(qual)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(address)+"','"+str(category)+"')"
            print(s2)
            c.execute(s2)
            conn.commit()
            s3 = "insert into login(`user_id`,`username`,`password`,`type`,`status`) values((select max(adv_id) from advocate),'"+str(email)+"','"+str(password)+"','advocate','0')"
            print(s3)
            c.execute(s3)
            conn.commit()
            msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
            # sendsms(phone,msgg)
            # return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+msgg+"&mobile="+phone+"")
            msg = "Advocate Registered Successfully,Your Account will be activate soon..."
            return render(request,"adv_register.html",{"data":data,"msg":msg})
        else:
            msg = "Account Already Exists"
            return render(request,"adv_register.html",{"data":data,"msg":msg})
    return render(request,"adv_register.html",{"data":data})

def user_register(request):
    print("-----------------------inside User register-------------------------")
    if 'submit' in request.POST:
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        aadhar = request.POST.get("aadhar")
        address = request.POST.get("address")
        password = request.POST.get("password")

        s1 = "select count(*) from user where u_email = '"+str(email)+"' or u_phone= '"+str(phone)+"' or u_aadhar='"+str(aadhar)+"'"
        print(s1)
        c.execute(s1)
        reg_count = c.fetchone()

        if reg_count[0] != 0 :
            msg = "Account Already Exists"
            return render(request,"user_register.html",{"msg":msg})

        else:
            request.session["name"] = name
            request.session["uploaded_file_url"] = uploaded_file_url
            request.session["age"] = age
            request.session["gender"] = gender
            request.session["email"] = email
            request.session["phone"] = phone
            request.session["aadhar"] = aadhar
            request.session["address"] = address
            request.session["password"] = password
            return HttpResponseRedirect("/user_bank")
       
    
    return render(request,"user_register.html")

def user_bank(request):
    name = request.session["name"]
    uploaded_file_url = request.session["uploaded_file_url"] 
    age = request.session["age"]  
    gender = request.session["gender"]
    email = request.session["email"]
    phone = request.session["phone"] 
    aadhar= request.session["aadhar"]
    address = request.session["address"]
    password = request.session["password"] 
    
    if 'submit' in request.POST:
        acc = request.POST.get("acc")
        cvv = request.POST.get("cvv")
        s2 = "insert into user(`u_img`,`u_name`,`u_age`,`u_gender`,`u_email`,`u_phone`,`u_aadhar`,`u_address`,`u_account`,`u_cvv`) values('"+str(uploaded_file_url)+"','"+str(name)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(aadhar)+"','"+str(address)+"','"+str(acc)+"','"+str(cvv)+"')"
        print(s2)
        c.execute(s2)
        conn.commit()
        s3 = "insert into login(`user_id`,`username`,`password`,`type`,`status`) values((select max(u_id) from user),'"+str(email)+"','"+str(password)+"','user','0')"
        print(s3)
        c.execute(s3)
        conn.commit()
        msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
        # sendsms(phone,msgg)
        # return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+msgg+"&mobile="+phone+"")

        msg = "User Registered Successfully,Your Account will be activate soon..."
        return render(request,"user_bank.html",{"msg":msg})
    
        # return render(request,"user_bank.html") 
    return render(request,"user_bank.html")

def admin_header_footer(request):
    
    return render(request,"admin_header_footer.html")

def admin_home(request):
    
    return render(request,"admin_home.html")

def advocate_list(request):

    s1 = "select * from advocate a , login l where a.adv_id = l.user_id and l.status = '1' and l.type = 'advocate'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Advocates to show...."
    
        return render(request,"advocate_list.html",{"data":data,"msgg":msg})
    return render(request,"advocate_list.html",{"data":data})

def adv_request(request):

    s1 = "select * from advocate a , login l where a.adv_id = l.user_id and l.status = '0' and l.type = 'advocate'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)
    if not bool(data):
        msg = "No Requests to show...."
    
        return render(request,"adv_request.html",{"data":data,"msgg":msg})
    
    return render(request,"adv_request.html",{"data":data})

def action_adv(request):
    reg_id = request.GET.get("reg_id")
    st = request.GET.get("st")
    print("inside action_adv")
    if st == 'Approve' :
        print("Approve")

        s = "update login set status = '1' where user_id = '"+str(reg_id)+"' and type = 'advocate'"
        print(s)
        c.execute(s)
        conn.commit()
        s1 = "select * from advocate a , login l where  a.adv_id = '"+str(reg_id)+"' and a.adv_id = l.user_id and l.type = 'advocate'"
        print(s1)
        c.execute(s1)
        data = c.fetchone()
        msg = " Dear "+str(data[2])+"... , Welcome to LEGAL ADVISOR .You can Login using  Username  :  "+str(data[7])+"  Password  :  "+str(data[13])
        # sendsms(data[8],msg)
        # return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+msg+"&mobile="+data[8]+"")

        return HttpResponseRedirect("/adv_request")
    
    if st == 'Reject' :
        print("Reject")

        s = "delete from login  where user_id = '"+str(reg_id)+"' and type = 'advocate'"
        print(s)
        c.execute(s)
        conn.commit()
        s = "delete from advocate  where adv_id = '"+str(reg_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/adv_request")
    
    return HttpResponseRedirect("/adv_request")

def adv_remove(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside action_adv")
    
    s = "delete from login where user_id = '"+str(reg_id)+"' and type='advocate'"
    print(s)
    c.execute(s)
    conn.commit()
    s1 = "delete from advocate  where adv_id = '"+str(reg_id)+"'"
    print(s1)
    c.execute(s1)
    conn.commit()
    
    return HttpResponseRedirect("/advocate_list")

def user_request(request):

    s1 = "select * from user u , login l where u.u_id = l.user_id and l.status = '0' and l.type = 'user'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)
    if not bool(data):
        msg = "No Requests to show...."
        return render(request,"user_request.html",{"data":data,"msgg":msg})
    
    return render(request,"user_request.html",{"data":data})

def action_user(request):
    reg_id = request.GET.get("reg_id")
    st = request.GET.get("st")
    print("inside action_adv")
    if st == 'Approve' :
        print("Approve")

        s = "update login set status = '1' where user_id = '"+str(reg_id)+"' and type = 'user'"
        print(s)
        c.execute(s)
        conn.commit()
        s1 = "select * from user u , login l where  u.u_id = '"+str(reg_id)+"' and u.u_id = l.user_id and l.type = 'user'"
        print(s1)
        c.execute(s1)
        data = c.fetchone()
        msg = " Dear "+str(data[2])+"... , Welcome to LEGAL ADVISOR .You can Login using  Username  :  "+str(data[5])+"  Password  :  "+str(data[11])
        # sendsms(data[6],msg)
        # return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+msg+"&mobile="+data[6]+"")

        return HttpResponseRedirect("/user_request")
    
    if st == 'Reject' :
        print("Reject")

        s = "delete from login  where user_id = '"+str(reg_id)+"' and type = 'user'"
        print(s)
        c.execute(s)
        conn.commit()
        s = "delete from user  where u_id = '"+str(reg_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/user_request")
    
    return HttpResponseRedirect("/user_request")

def user_list(request):

    s1 = "select * from user u , login l where u.u_id = l.user_id and l.status = '1' and l.type = 'user'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Users to show...."
    
        return render(request,"user_list.html",{"data":data,"msgg":msg})
    return render(request,"user_list.html",{"data":data})

def user_remove(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside action_adv")
    
    s = "delete from login where user_id = '"+str(reg_id)+"' and type='user'"
    print(s)
    c.execute(s)
    conn.commit()
    s1 = "delete from user  where u_id = '"+str(reg_id)+"'"
    print(s1)
    c.execute(s1)
    conn.commit()
    
    return HttpResponseRedirect("/user_list")

def case_category(request):
    ss = "select * from category"
    c.execute(ss)
    data1 = c.fetchall()
    if 'cat' in request.POST:
        category = request.POST.get("category")
        cat_description = request.POST.get("cat_description")
        s = "select count(*) from category where cat_name = '"+str(category)+"'"
        c.execute(s)
        data = c.fetchone()

        if data[0] == 0 :
            s1 = "insert into category(`cat_name`,`cat_description`) values('"+str(category)+"','"+str(cat_description)+"')"
            c.execute(s1)
            conn.commit()
            msg = str(category)+" added Successfully"
            return render(request,"case_category.html",{"msg":msg,"data1":data1})
        else:
            msg = str(category)+" already exists"
            return render(request,"case_category.html",{"msg":msg,"data1":data1})
    return render(request,"case_category.html",{"data1":data1})

def cat_remove(request):
    cat_id = request.GET.get("cat_id")
    
    print("inside action_adv")
    
    s = "delete from category where cat_id = '"+str(cat_id)+"'"
    print(s)
    c.execute(s)
    conn.commit()
    
    return HttpResponseRedirect("/case_category")

def ipc_section(request):
    ss = "select * from ipc"
    c.execute(ss)
    data1 = c.fetchall()
    if 'ipc' in request.POST:
        ipc_section = request.POST.get("ipc_section")
        ipc_description = request.POST.get("ipc_description")
        s = "select count(*) from ipc where ipc_section = '"+str(ipc_section)+"'"
        c.execute(s)
        data = c.fetchone()

        if data[0] == 0 :
            s1 = "insert into ipc(`ipc_section`,`ipc_description`) values('"+str(ipc_section)+"','"+str(ipc_description)+"')"
            c.execute(s1)
            conn.commit()
            msg = str(ipc_section)+" added Successfully"
            return render(request,"ipc_section.html",{"data1":data1,"msg":msg})
        else:
            msg = str(ipc_section)+" already exists"
            return render(request,"ipc_section.html",{"msg":msg,"data1":data1})
    return render(request,"ipc_section.html",{"data1":data1})

def ipc_remove(request):
    ipc_id = request.GET.get("ipc_id")
    
    print("inside action_adv")
    
    s = "delete from ipc where ipc_id = '"+str(ipc_id)+"'"
    print(s)
    c.execute(s)
    conn.commit()
    
    return HttpResponseRedirect("/ipc_section")

def view_feedback(request):
    print("inside feedback")

    if 'submit' in request.POST:
        print("inside submit")
        user_type = request.POST.get("user_type")
        print(user_type)
        if user_type == 'user' :
            s = "select * from feedback f,user u where f.type='user' and f.u_id = u.u_id"
            print(s)
            c.execute(s)
            data_feed = c.fetchall()
            if not bool(data_feed):
                msg = "No Users to show...."

                return render(request,"view_feedback.html",{"msgg":msg})
            else:
                return render(request,"view_feedback.html",{"data_feed":data_feed,"user":user_type})

        if user_type == 'advocate' :
            s = "select * from feedback f,advocate a where f.type='advocate' and f.u_id = a.adv_id"
            print(s)
            c.execute(s)
            data_feed = c.fetchall()
            if not bool(data_feed):
                msg = "No Users to show...."

                return render(request,"view_feedback.html",{"msgg":msg})
            else:
                return render(request,"view_feedback.html",{"data_feed":data_feed,"user":user_type})
    return render(request,"view_feedback.html")

def phone_number(request):
    utype = request.GET.get("type")
    
    if 'send' in request.POST:
        phone = request.POST.get("phone")
        print(phone,"phhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        if utype == 'advocate':
            s = "select count(*),adv_id from advocate where adv_phone = '"+str(phone)+"'"
            c.execute(s)
            data = c.fetchone()
            print(data)

            

            if data[0] != 0 :
                request.session["phone"] = phone
                request.session["u_id"] = data[1]
                request.session["utype"] = utype
                
                
                return HttpResponseRedirect("/gen_otp/")
            else:
                msg = "This is not a registered Email.Please use a valid number"
                return render(request,"phone_number.html",{"msg":msg})

        if utype == 'user':
            s = "select count(*),u_id from user where u_phone = '"+str(phone)+"'"
            c.execute(s)
            data = c.fetchone()
            print(data)

            

            if data[0] != 0 :
                request.session["phone"] = phone
                request.session["u_id"] = data[1]
                request.session["utype"] = utype
                
                
                return HttpResponseRedirect("/gen_otp/")
            else:
                msg = "This is not a registered phone number.Please use a valid number"
                return render(request,"phone_number.html",{"msg":msg})
    return render(request,"phone_number.html")

# def gen_otp(request):
#     phone = request.session["phone"]
#     print(phone)
#     otp = random.randrange(1000,9999,6)
#     print(otp)

#     request.session["otp"] = otp
#     request.session["pho"]=phone 
    
#     msg = str(otp)
    # sendsms(phone,msg)
    # return HttpResponseRedirect('<script>window.location.href="http://dattaanjaneya.biz/API_Services/SMS_Service.php?content='+msg+'&mobile='+phone+';</script>')
    # return HttpResponseRedirect("/sendsms1/")

    # return render(request,"phone_number.html")
    # return HttpResponseRedirect("/otp/")

# def sendsms1(request):
#     otp=request.session["otp"] 
#     phone=request.session["phone"]
    
#     msg = str(otp)
    
#     if "sub" in request.POST:
#         return HttpResponseRedirect("/otp/")
#     return render(request,"sendsms.html",{"msg":msg,"phone":phone})
# def otp(request):
#     phone = request.session["phone"]
#     otp_val = request.session["otp"]
#     print(phone)
#     print(otp_val)

#     if 'submit' in request.POST:
#         otp = request.POST.get("otp")
#         if str(otp) == str(otp_val):
#             return HttpResponseRedirect("/new_password/")
        
#         else:
#             msg = "please enter the valid"
#             return render(request,"otp.html",{"msg":msg})
            
#     return render(request,"otp.html")

def new_password(request):
    phone = request.session["phone"]
    # otp_val = request.session["otp"]
    u_id = request.session["u_id"]
    utype = request.session["utype"]
    print(phone)
    # print(otp_val)

    if 'submit' in request.POST:
        new_pass = request.POST.get("new_pass")
        q1 = "update login set password = '"+str(new_pass)+"' where user_id = '"+str(u_id)+"' and type = '"+str(utype)+"'"
        c.execute(q1)
        conn.commit()
        print(q1)
        msgg = "Password Reset Successfully. Login with your New Password."
        return render(request,"new_password.html",{"msgg":msgg})

       
    return render(request,"new_password.html")
