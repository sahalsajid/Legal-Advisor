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

def adv_header_footer(request):
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_header_footer.html")

def adv_home(request):
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_home.html")

def adv_ipc(request):
    s = "select * from ipc order by ipc_section"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_ipc.html",{"data":data})

def adv_list(request):
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
                return render(request,"adv_list.html",{"data":data,"data2":data2,"msg":msg})
            return render(request,"adv_list.html",{"data":data,"data2":data2})
        else:
            s1 = " select * from advocate where adv_category = '"+str(category)+"' "
            print(s1)
            c.execute(s1)
            data1 =c.fetchall()
            print(data1)
            if not bool(data1):
                msg = "No Advocate List To show"
                return render(request,"adv_list.html",{"data":data,"data2":data1,"msg":msg})
            return render(request,"adv_list.html",{"data":data,"data2":data1})
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_list.html",{"data":data})

def adv_view_adv(request):
    adv_id = request.GET.get("adv_id")
    print(adv_id)
    s = "select * from advocate where adv_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_view_adv.html",{"data":data})

def adv_case_request(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.adv_id  and c.user_id = u.u_id and c.status = 'Applied'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"adv_case_request.html",{"data":data,"msgg":msgg})
    return render(request,"adv_case_request.html",{"data":data})

def view_case_request(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")

    s = "select * from case_request c , user u  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()

    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()

    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"view_case_request.html",{"data":data,"msgg":msgg,"data1":data1})
    return render(request,"view_case_request.html",{"data":data,"data1":data1})


def status(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    st = request.GET.get("st")

    if st == 'Approved':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Accepted"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_request")


    if st == 'Rejected':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Rejected"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_request")


    if st == 'Proceeding':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Proceeding"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/view_case_request?case_id="+str(case_id)+"&u_id="+str(u_id))

    # data = c.fetchall()
    # print(data)
    # if not bool(data):
    #     msgg = "No case Applications"
    # # if 'login' in request.POST:
    #     # return HttpResponseRedirect("/login")
    # return HttpResponseRedirect("/view_case_request?case_id=case_id&u_id=u_id")
    return render(request,"adv_case_request.html")

def case_ipc(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")

    if 'ipc' in request.POST:
        ipc_description = request.POST.get("ipc_description")
        s = "update case_request set ipc_sections= '"+str(ipc_description)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        
        # return render(request,"case_ipc.html",{"msg":msg})
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))


    # data = c.fetchall()
    # print(data)
    # if not bool(data):
    #     msgg = "No case Applications"
    # # if 'login' in request.POST:
    #     # return HttpResponseRedirect("/login")
    # return HttpResponseRedirect("/view_case_request?case_id=case_id&u_id=u_id")
    return render(request,"case_ipc.html")

def add_fee(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")
    tdate = now.date()
    if 'fee' in request.POST:
        amount = request.POST.get("amount")
        s = "insert into payment(`user_id`,`adv_id`,`case_id`,`posted_date`,`amount`,`status`) values('"+str(u_id)+"', '"+str(adv_id)+"', '"+str(case_id)+"','"+str(tdate)+"','"+str(amount)+"','Not Paid')"
        print(s)
        c.execute(s)
        conn.commit()
        
        # return render(request,"case_ipc.html",{"msg":msg})
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))


    # data = c.fetchall()
    # print(data)
    # if not bool(data):
    #     msgg = "No case Applications"
    # # if 'login' in request.POST:
    #     # return HttpResponseRedirect("/login")
    # return HttpResponseRedirect("/view_case_request?case_id=case_id&u_id=u_id")
    return render(request,"add_fee.html")

def adv_feedback(request):
    adv_id = request.session["adv_id"]
    tdate = now.date()

    if 'submit' in request.POST:
        subject = request.POST.get("subject")
        feedback_desc = request.POST.get("feedback_desc")
        s = "insert into feedback(`u_id`,`feed_subject`,`feed_description`,`type`,`posted_date`) values('"+str(adv_id)+"','"+str(subject)+"','"+str(feedback_desc)+"','advocate','"+str(tdate)+"')"
        c.execute(s)
        conn.commit()
        msg = "Feedback Send Successfully"
    # if request.POST:
    #     return HttpResponseRedirect("/payment5/")
        return render(request,"adv_feedback.html",{"msg":msg})
    return render(request,"adv_feedback.html")



def adv_case_status(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.adv_id  and c.user_id = u.u_id and c.status != 'Applied' and c.status != 'Rejected' and c.status != 'Completed'   order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"adv_case_status.html",{"data":data,"msgg":msgg})
    return render(request,"adv_case_status.html",{"data":data})


def view_case_status(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")

    s = "select * from case_request c , user u  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()

    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()
    print("hloooo")
    s2 = "select * from documents where case_id = '"+str(case_id)+"' order by doc_id"
    print(s2)
    print("haiiiiiiiiii")
    c.execute(s2)
    conn.commit()
    data2 = c.fetchall()

    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"view_case_status.html",{"data":data,"msgg":msgg,"data1":data1,"data2":data2})
        
    return render(request,"view_case_status.html",{"data":data,"data1":data1,"data2":data2})

def add_doc(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")
    tdate = now.date()
    if 'doc' in request.POST:
        file_name = request.POST.get("file_name")
        # file_doc = request.POST.get("file_doc")
        myfile = request.FILES["file_doc"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ss = "select count(*) from documents where document = '"+str(uploaded_file_url)+"'"
        c.execute(ss)
        doc_count = c.fetchone()
        if doc_count[0] == 0: 
            s = "insert into documents(`case_id`,`u_id`,`adv_id`,`doc_name`,`document`,`posted_date`) values('"+str(case_id)+"','"+str(u_id)+"', '"+str(adv_id)+"','"+str(file_name)+"','"+str(uploaded_file_url)+"',  '"+str(tdate)+"')"
            print(s)
            c.execute(s)
            conn.commit()
            return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))
        else:
            msg = "file Already Exists"
        return render(request,"add_doc.html",{"msg":msg})
    return render(request,"add_doc.html")
        # return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))

def status1(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    st = request.GET.get("st")

    # if st == 'Approved':
    #     s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
    #     print(s)
    #     c.execute(s)
    #     conn.commit()
    #     msg = "Mark as Accepted"
    #     # return render(request,"adv_case_request.html",{"msg":msg})
    #     return HttpResponseRedirect("/adv_case_request")


    if st == 'Rejected':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Rejected"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_status")

    if st == 'Completed':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Completed"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_status")


    if st == 'Proceeding':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Proceeding"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))

    # data = c.fetchall()
    # print(data)
    # if not bool(data):
    #     msgg = "No case Applications"
    # # if 'login' in request.POST:
    #     # return HttpResponseRedirect("/login")
    # return HttpResponseRedirect("/view_case_request?case_id=case_id&u_id=u_id")
    return render(request,"adv_case_status.html")



def rej_com_case(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.adv_id  and c.user_id = u.u_id and c.status = 'Completed'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)

    s1 = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.adv_id  and c.user_id = u.u_id and c.status = 'Rejected'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()
    print(data1)



    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"rej_com_case.html",{"data":data,"msgg":msgg,"data1":data1})

    
    return render(request,"rej_com_case.html",{"data":data,"data1":data1})







def adv_cat_list(request):
    s = "select * from category order by cat_id"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_cat_list.html",{"data":data})

def advocate_profile(request):
    adv_id = request.session["adv_id"]

    s = "select * from advocate a , login l where a.adv_id = '"+str(adv_id)+"' and a.adv_id = l.user_id and l.type = 'advocate' "
    c.execute(s)
    data = c.fetchone()
    print(data)
    return render(request,"advocate_profile.html",{"data":data})

def adv_change_password(request):
    adv_id = request.session["adv_id"]

    
    if 'change_pass' in request.POST:
        password = request.POST.get("new_pass")
        s = "update login set password = '"+str(password)+"' where user_id = '"+str(adv_id)+"' and type = 'advocate' "
        c.execute(s)
        conn.commit()
        
        return HttpResponseRedirect("/advocate_profile/")
    return render(request,"adv_change_password.html")

