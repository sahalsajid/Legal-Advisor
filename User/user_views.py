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
def user_home(request):
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_home.html")

def user_header_footer(request):
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_header_footer.html")

def user_ipc(request):
    s = "select * from ipc order by ipc_section"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_ipc.html",{"data":data})

#     SELECT 
# tbl_column, 
# CAST(tbl_column as SIGNED) AS casted_column
# FROM db_table
# ORDER BY casted_column ASC , tbl_column ASC

# SELECT 
# tbl_column, 
# BIN(tbl_column) AS binray_not_needed_column
# FROM db_table
# ORDER BY binray_not_needed_column ASC , tbl_column ASC


def user_adv_list(request):
    s = "select * from category order by cat_name"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)

    if 'cat' in request.POST:
        category = request.POST.get("category")
        print(category)
        if category == 'All':
            s2 = "select * from advocate order by adv_category"
            print(s2)
            c.execute(s2)
            data2 =c.fetchall()
            print(data2)
            if not bool(data2):
                msg = "No Advocate List To show"
                return render(request,"user_adv_list.html",{"data":data,"data2":data2,"msg":msg})
            return render(request,"user_adv_list.html",{"data":data,"data2":data2})
        else:
            s1 = " select * from advocate where adv_category = '"+str(category)+"' "
            print(s1)
            c.execute(s1)
            data1 =c.fetchall()
            print(data1)
            if not bool(data1):
                msg = "No Advocate List To show"
                return render(request,"user_adv_list.html",{"data":data,"data2":data1,"msg":msg})
            return render(request,"user_adv_list.html",{"data":data,"data2":data1})
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_adv_list.html",{"data":data})

def view_adv(request):
    adv_id = request.GET.get("adv_id")
    print(adv_id)
    s = "select * from advocate where adv_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"view_adv.html",{"data":data})

def add_case(request):
    uid = request.session["uid"]
    print(uid)
    adv_id = request.GET.get("adv_id")
    print(adv_id)
    s = "select * from advocate where adv_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    if 'register' in request.POST:
        case_title = request.POST.get("case_title")
        case_desc = request.POST.get("case_desc")
        # case_file = request.POST.get("case_file")

        myfile = request.FILES["case_file"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        s1 = "insert into case_request(`adv_id`,`user_id`,`case_title`,`case_desc`,`case_file`,`status`) values('"+str(adv_id)+"','"+str(uid)+"','"+str(case_title)+"','"+str(case_desc)+"','"+str(uploaded_file_url)+"','Applied')"
        c.execute(s1)
        conn.commit()   
        msg = "Case Registered Successfully"    
        # return HttpResponseRedirect("/login")
        return render(request,"add_case.html",{"msg":msg})

    return render(request,"add_case.html",{"data":data})

def case_status(request):
    uid = request.session["uid"]
    s = "select * from case_request c , user u, advocate a  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id and c.adv_id = a.adv_id  order by c.case_id desc"

    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"case_status.html",{"data":data,"msgg":msgg})
    return render(request,"case_status.html",{"data":data})

def user_view_case_status(request):
    u_id = request.session["uid"]
    case_id = request.GET.get("case_id")
    adv_id = request.GET.get("adv_id")



    s = "select * from case_request c , user u,advocate a  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"' and c.user_id = u.u_id and c.adv_id = a.adv_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()

    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()

    s2 = "select * from documents where case_id = '"+str(case_id)+"' order by doc_id"
    print(s2)
    print("haiiiiiiiiii")
    c.execute(s2)
    conn.commit()
    data2 = c.fetchall()


    s3 = "select * from rating  where case_id = '"+str(case_id)+"' and  adv_id = '"+str(adv_id)+"' "
    print(s3)
    print("haiiiiiiiiii")
    c.execute(s3)
    conn.commit()
    data3 = c.fetchall()
    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"user_view_case_status.html",{"data":data,"msgg":msgg,"data1":data1,"data2":data2,"data3":data3})
    return render(request,"user_view_case_status.html",{"data":data,"data1":data1,"data2":data2,"data3":data3})



def payment1(request):
    u_id = request.session["uid"]
    case_id = request.GET.get("case_id")
    adv_id = request.GET.get("adv_id")
    request.session["amt"] = request.GET.get("amt")
    request.session["pay_id"] = request.GET.get("pay_id")
    s = "select u_account,u_cvv from user where u_id = '"+str(u_id)+"'"
    c.execute(s)
    fee_data = c.fetchone()
    request.session["cno"] = fee_data[0]
    if request.POST:
        cardno=request.POST.get("cardno")
        pinno=request.POST.get("pinno")
        if cardno == fee_data[0] and pinno == fee_data[1]:
            return HttpResponseRedirect("/payment2/")
        else:
            msg = "Account Details Not valid"
            return render(request,"payment1.html",{"msg":msg})
    return render(request,"payment1.html")
def payment2(request):
    amt= request.session["amt"] 
    request.session["pay_id"] = request.GET.get("pay_id")
    cno= request.session["cno"]
    if request.POST:

        request.session['t1']=request.POST.get('t1')
        request.session['t2']=request.POST.get('t2')
        request.session['t3']=request.POST.get('t3')
        request.session['t4']=request.POST.get('t4')
        return HttpResponseRedirect("/payment3/")
    return render(request,"payment2.html",{'cno':cno,"amt":amt})
def chat(request):
    import chatgui
    
    return render(request,"user_home.html")
def payment3(request):
  
    if request.POST:
        return HttpResponseRedirect("/payment4/")
    return render(request,"payment3.html")
def payment4(request):
  
    if request.POST:
        return HttpResponseRedirect("/payment5/")
    return render(request,"payment4.html")
def payment5(request):
  
    pay_id=request.session['pay_id']
    amt= request.session["amt"] 
    t1= request.session["t1"] 

    tdate=now.date()
    s= "update payment set paid_date = '"+str(tdate)+"',status = 'Paid'"
    c.execute(s)
    conn.commit()
    return render(request,"payment5.html",{'t1':t1,'tdate':tdate,'amt':amt})


def user_feedback(request):
    u_id = request.session["uid"]
    tdate = now.date()

    if 'submit' in request.POST:
        subject = request.POST.get("subject")
        feedback_desc = request.POST.get("feedback_desc")
        user="user"
        s = "insert into feedback(`u_id`,`feed_subject`,`feed_description`,`type`,`posted_date`) values('"+str(u_id)+"','"+str(subject)+"','"+str(feedback_desc)+"','"+ user +"','"+str(tdate)+"')"
        c.execute(s)
        conn.commit()
        msg = "Feedback Send Successfully"
    # if request.POST:
    #     return HttpResponseRedirect("/payment5/")
        return render(request,"user_feedback.html",{"msg":msg})
    return render(request,"user_feedback.html")

    
def user_cat_list(request):
    s = "select * from category order by cat_id"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_cat_list.html",{"data":data})



def add_rating(request):
    if 'rating' in request.POST:
        u_id = request.session["uid"]
        case_id = request.GET.get("case_id")
        adv_id = request.GET.get("adv_id")
        u_rating = request.POST.get("u_rating")
        rating_desc = request.POST.get("rating_desc")


        s = "select count(*) from rating where case_id = '"+str(case_id)+"' and adv_id = '"+str(adv_id)+"' and user_id = '"+str(u_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        cnt = c.fetchone()
        if cnt[0] == 0 :

            
            s1 = "insert into rating(`case_id`,`user_id`,`adv_id`,`rating`,`rate_desc`) values('"+str(case_id)+"','"+str(u_id)+"','"+str(adv_id)+"','"+str(u_rating)+"' ,'"+str(rating_desc)+"')"
            c.execute(s1)
            conn.commit()
            # msg = str(ipc_section)+" added Successfully"
            # return render(request,"add_rating.html")
            return HttpResponseRedirect("/user_view_case_status?case_id="+str(case_id)+"&adv_id="+str(adv_id))

        else:
            msg = " already done rating"
            # return render(request,"add_rating.html",{"msg":msg})
            return HttpResponseRedirect("/user_view_case_status?case_id="+str(case_id)+"&adv_id="+str(adv_id))

    return render(request,"add_rating.html")

def user_about(request):
    return render(request,"user_about.html")

def user_profile(request):
    u_id = request.session["uid"]
    s = "select * from user u , login l where u.u_id = '"+str(u_id)+"' and u.u_id = l.user_id and l.type = 'user' "
    c.execute(s)
    data = c.fetchone()
    print(data)
    return render(request,"user_profile.html",{"data":data})

def change_password(request):
    u_id = request.session["uid"]
    if 'change_pass' in request.POST:
        password = request.POST.get("new_pass")
        s = "update login set password = '"+str(password)+"' where user_id = '"+str(u_id)+"' and type= 'user' "
        c.execute(s)
        conn.commit()
        
        return HttpResponseRedirect("/user_profile/")
    return render(request,"user_password.html")
def change_number(request):
    u_id = request.session["uid"]
    if 'change_number' in request.POST:
        password = request.POST.get("new_num")
        s = "update user set u_phone = '"+str(password)+"' where u_id = '"+str(u_id)+"'"
        c.execute(s)
        conn.commit()
        
        return HttpResponseRedirect("/user_profile/")
    return render(request,"user_number.html")
    
    