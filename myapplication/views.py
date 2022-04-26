import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from myapplication.models import login,tourstplce,bussiness,users,complaints,feedback,rating,service,package,packgesub,offers,booking,custompackage,interest,chat

# Create your views here.

def home_load(request):
    return render(request,'admin/home.html')

def login_load(request):
    return render(request,'a.html')
def login_post(request):
    uname=request.POST['email']
    psw=request.POST['pswd']
    res=login.objects.get(username=uname,password=psw)
    if res.type=="admin":
        return adm_index_load(request)
    elif res.type=="bussiness":
        request.session["lid"]=res.id
        if bussiness.objects.filter(LOGIN_id=res.id,status='approved').exists():
            print("yes")
            q=bussiness.objects.get(LOGIN_id=res.id)
            request.session["id"] = q.id
            return render(request,'bussiness/b_home.html')
        else:
            return login_load(request)

    elif res.type=="users":
        request.session["lid"] = res.id
        q=users.objects.get(LOGIN_id=res.id)
        request.session["id"] = q.id
        return render(request,'user/home.html')
    else:
        return HttpResponse("Invalid")



def adm_addplce_load(request):
    return render(request,'admin/addplce.html')
def adm_addplce_post(request):
    uname=request.POST['textfield']
    dscptn=request.POST['textfield2']
    img1=request.FILES['file']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "1.jpg"
    fs.save(filename, img1)
    url1 = '/media/' + filename

    img2=request.FILES['file2']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "2.jpg"
    fs.save(filename, img2)
    url2 = '/media/' + filename

    img3=request.FILES['file3']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "3.jpg"
    fs.save(filename, img3)
    url3 = '/media/' + filename
    opntym=request.POST['textfield3']
    plc=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    city=request.POST['textfield7']
    dstrct=request.POST['textfield8']
    state=request.POST['textfield9']
    latitde=request.POST['textfield11']
    logtitde=request.POST['textfield12']
    phn=request.POST['textfield10']


    print("phone",phn)



    ob=tourstplce()
    ob.name=uname
    ob.descripion=dscptn
    ob.image1=url1
    ob.image2=url2
    ob.image3=url3
    ob.openingtime=opntym
    ob.place=plc
    ob.post=post
    ob.pin=pin
    ob.city=city
    ob.district=dstrct
    ob.state=state
    ob.latitude=latitde
    ob.longtitude=logtitde
    ob.phone=phn
    ob.save()
    return render(request, 'admin/addplce.html')


def adm_index_load(request):
    return render(request,'admin/index.html')



def adm_editplce_load(request,id):
    t=tourstplce.objects.get(id=id)
    return render(request,'admin/editplce.html',{'t':t})
def adm_editplce_post(request):
    uname=request.POST['textfield']
    print(uname)
    dscptn=request.POST['textfield2']
    print(dscptn)
    img1=request.FILES['file']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "1.jpg"
    fs.save(filename, img1)
    url1 = '/media/' + filename

    img2=request.FILES['file2']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "2.jpg"
    fs.save(filename, img2)
    url2 = '/media/' + filename

    img3=request.FILES['file3']
    fs = FileSystemStorage()
    name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename = name1 + "3.jpg"
    fs.save(filename, img3)
    url3 = '/media/' + filename

    opntym=request.POST['textfield3']
    print(opntym)
    plc=request.POST['textfield4']
    print(plc)
    post=request.POST['textfield5']
    print(post)
    pin=request.POST['textfield6']
    print(pin)
    city=request.POST['textfield7']
    print(city)
    dstrct=request.POST['textfield8']
    print(dstrct)
    state=request.POST['textfield9']
    print(state)
    latitde=request.POST['textfield11']
    print(state)
    logtitde=request.POST['textfield12']
    print(logtitde)
    phn=request.POST['textfield10']
    print(phn)
    tid=request.POST['tid']
    print(tid)
    tourstplce.objects.filter(id=tid).update(name=uname,descripion=dscptn,image1=url1,image2=url2,image3=url3,openingtime=opntym,place=plc,post=post,pin=pin,city=city,district=dstrct,state=state,latitude=latitde,longtitude=logtitde,phone=phn)
    return adm_viewtourstplce_load(request)


def adm_Bussines_load(request):
    res=bussiness.objects.filter()
    return render(request,'admin/Bussines.html',{"res":res})


def adm_aprovd_bussiness(request,cid):
    c=bussiness.objects.get(id=cid)
    c.status="approved"
    c.save()
    return adm_Bussines_load(request)

def adm_rejct_bussiness(request,cid):
    c=bussiness.objects.get(id=cid)
    c.status="reject"
    c.save()
    return adm_Bussines_load(request)


def adm_ChngePaswrd_load(request):
    return render(request,'admin/Changepassword.html')
def adm_ChngePaswrd_post(request):
    lid=request.session['lid']
    crntpswrd=request.POST['textfield2']
    nwpswrd=request.POST['textfield3']
    retppswrd=request.POST['textfield4']

    obj1=login.objects.get(id=lid,password=crntpswrd)
    if nwpswrd==retppswrd:
        obj1.password=retppswrd
        obj1.password=nwpswrd
        obj1.save()
    else:
        return HttpResponse("invalid")

    return adm_ChngePaswrd_load(request)

def adm_fedbck_load(request):
    res=feedback.objects.all()
    return render(request,'admin/feedback.html',{"res":res})


def adm_rtingandview_load(request):
    res=rating.objects.all()
    print(res)
    return render(request,'admin/ratingandrview.html',{"res":res})

def adm_sndrply_load(request,cid):
    return render(request,'admin/sendreplay.html',{'cid':cid})
def adm_sndrply_post(request):
    sndrply=request.POST['textarea1']
    cid=request.POST['cid']

    compobj=complaints.objects.get(id=cid)
    compobj.replay=sndrply
    compobj.save()


    return adm_viewcmpnlt_load(request)

def adm_search_load(request):
    datefrom=request.POST['d1']
    to=request.POST['d2']
    res=complaints.objects.filter(date__range=(datefrom,to))
    print(res)
    return render(request,'admin/viewcmplaint.html',{"res":res})

def adm_usrview_load(request):
    res=users.objects.all()
    return render(request,'admin/userview.html',{"res":res})

def adm_viewapprvdbusns_load(request):
    res=bussiness.objects.filter(status='approved')
    return render(request,'admin/viewapprovedbussiness.html',{"res":res})

def adm_blk_bussiness(request,cid):
    c=bussiness.objects.get(id=cid)
    c.status="bloked"
    c.save()
    return adm_viewapprvdbusns_load(request)



def adm_viewcmpnlt_load(request):
    res=complaints.objects.filter()
    return render(request,'admin/viewcmplaint.html',{"res":res})

def adm_viewtourstplce_load(request):
    res=tourstplce.objects.all()
    return render(request,'admin/viewtouristplace.html',{'res':res})


def adm_delete_touristplace(request,cid):
    c=tourstplce.objects.get(id=cid)
    c.delete()
    return adm_viewtourstplce_load(request)


#__________________________________BUSSINESS_________________________


def busns_index_load(request):
    return render(request,'bussiness/index.html')
def busns_signup1_load(request):
    return render(request,'signup.html')


def busns_addsrvc_load(request):
    return render(request,'bussiness/addservice.html')

def busns_addsrvc_post(request):
    nme=request.POST['textfield']
    price=request.POST['textfield3']

    s=service()
    s.name=nme
    s.price=price
    s.BUSSINESS=bussiness.objects.get(LOGIN_id=request.session['lid'])
    s.save()

    return render(request,'bussiness/addservice.html')

def busns_fedbck_load(request):
    res=feedback.objects.all()
    return render(request,'bussiness/feedback.html',{"res":res})

def busns_viewcmpnlt_load(request):
    res=complaints.objects.filter()
    return render(request,'bussiness/viewcmplaint.html',{"res":res})



def busns_ChngePaswrd_load(request):
    return render(request,'bussiness/Changepassword.html')
def busns_ChngePaswrd_post(request):
    lid=request.session['lid']
    crntpswrd=request.POST['textfield2']
    nwpswrd=request.POST['textfield3']
    retppswrd=request.POST['textfield4']

    obj1=login.objects.get(id=lid,password=crntpswrd)
    if nwpswrd==retppswrd:
        obj1.password=retppswrd
        obj1.password=nwpswrd
        obj1.save()
    else:
        return HttpResponse("invalid")

    return busns_ChngePaswrd_load(request)

def busns_pckmngnt_load(request):
    return render(request,'bussiness/packagemanagment.html')
def busns_pckmngnt_post(request):
    amount=request.POST['amount']
    totlday=request.POST['ttlday']
    packgnme=request.POST['packagenme']

    p=package()
    p.packgenme=packgnme
    p.amount=amount
    p.totldays=totlday
    p.BUSSINESS = bussiness.objects.get(LOGIN_id=request.session['lid'])
    p.save()

    lid=p.id
    request.session["pack_id"]=lid
    return busns_add_sub_package_load(request)


def busns_srvcmngmnt_load(request):
    res=service.objects.all()
    return render(request,'bussiness/servicemanagement.html',{'res':res})

def busns_delete_srvcmngmnt(request,cid):
    c=service.objects.get(id=cid)
    c.delete()
    return busns_srvcmngmnt_load(request)

def busns_editsrvcmngmnt_load(request,id):
    i=service.objects.get(id=id)
    return render(request,'bussiness/editservice.html',{'i':i})

def busns_editsrvcmngmnt_post(request):
    uname=request.POST['textfield']
    price=request.POST['textfield3']
    id=request.POST['id']
    service.objects.filter(id=id).update(name=uname,price=price)
    return busns_srvcmngmnt_load(request)

# def busns_signup_load(request):
#     return render(request,'bussiness/signup.html')
def busns_signup_post(request):
    name=request.POST['textfield']
    prfle=request.FILES['file']
    fs=FileSystemStorage()
    name1=datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename=name1+".jpg"
    fs.save(filename,prfle)
    url='/media/'+filename
    email=request.POST['textfield2']
    plc=request.POST['textfield4']
    about=request.POST['textarea']
    dscrptn=request.POST['textarea2']
    pst=request.POST['textfield6']
    pin=request.POST['textfield7']
    city=request.POST['textfield8']
    distrct=request.POST['textfield9']
    state=request.POST['textfield10']
    latitde=request.POST['textfield11']
    longtitde=request.POST['textfield12']
    phn=request.POST['textfield13']
    pswrd=request.POST['textfield14']
    cnfrmpswd=request.POST['textfield15']




    lo=login()
    lo.username=email
    lo.password=pswrd
    lo.type="bussiness"
    lo.save()

    ob=bussiness()
    ob.name=name
    ob.image=url
    ob.about=about
    ob.email = email
    ob.description=dscrptn
    ob.place=plc
    ob.pin=pin
    ob.city=city
    ob.post=pst
    ob.district=distrct
    ob.state=state
    ob.latitude=latitde
    ob.logtitde=longtitde
    ob.contact=phn
    ob.LOGIN=lo
    ob.save()



    return render(request,"a.html")

def busns_vwpckg_load(request):
    res = package.objects.filter(BUSSINESS=request.session["id"])

    return render(request,'bussiness/viewpackage.html',{'res':res})

def busns_vwpckgdel_load(request,cid):
    c=package.objects.get(id=cid)
    c.delete()
    return busns_vwpckg_load(request)


def busns_editpkge_load(request,id):
    p = package.objects.get(id=id)
    return render(request,'bussiness/editpackage.html',{'p':p})

def busns_editpkge_post(request):

    amount = request.POST['amount']
    totlday = request.POST['ttlday']
    packgnme = request.POST['packagenme']
    pid = request.POST['pid']
    package.objects.filter(id=pid).update(amount=amount,totldays=totlday,packgenme=packgnme)
    return busns_vwpckg_load(request)

def busns_add_sub_package_load(request):
    return render(request,'bussiness/addsubpackage.html')
def busns_add_sub_package_post(request):
    pack_id=str(request.session["pack_id"])
    print(pack_id)
    foodinfo=request.POST['text2']
    discription=request.POST['text3']
    place=request.POST['text4']
    p=packgesub()
    p.PACKAGE_id=pack_id
    p.foodinfo=foodinfo
    p.descrptn=discription
    p.place=place
    p.save()
    return render(request, 'bussiness/addsubpackage.html')

def busns_vwprfle_load(request):
    bid=request.session["id"]
    res=bussiness.objects.get(id=bid)
    return render(request,'bussiness/viewprofile.html',{'res':res})

def busns_vwprfle_post(request):


    name=request.POST['textfield']
    email=request.POST['textfield2']
    plc=request.POST['textfield3']
    abt=request.POST['textarea']
    post=request.POST['textfield4']
    pin=request.POST['textfield5']
    city=request.POST['textfield6']
    dstrct=request.POST['textfield7']
    state=request.POST['textfield8']
    latitde=request.POST['textfield9']
    logtitde=request.POST['textfield10']
    phn=request.POST['textfield11']


    if 'file' in request.FILES:
        prfle = request.FILES['file']
        fs = FileSystemStorage()
        name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
        filename = name1 + ".jpg"
        fs.save(filename, prfle)
        url = '/media/' + filename
        bussiness.objects.filter(id=request.session["id"]).update(name=name,image=url,email=email,place=plc,about=abt,post=post,pin=pin,city=city,district=dstrct,state=state,latitude=latitde,logtitde=logtitde,contact=phn)
    else:
        bussiness.objects.filter(id=request.session["id"]).update(name=name, email=email, place=plc,
                                                                  about=abt,
                                                                  post=post, pin=pin, city=city, district=dstrct,
                                                                  state=state, latitude=latitde, logtitde=logtitde,
                                                                  contact=phn)
    return HttpResponse('''<script>alert("updated");window.location='/rwt/busns_vwprfle_load/'</script>''')

def busns_addofr_load(request):
    vv=package.objects.all()
    hh=offers.objects.all()
    return render(request,'bussiness/addoffer.html',{'vv':vv,'hh':hh})


def busns_addofr_post(request):
    offr=request.POST['textfield']
    dscption=request.POST['textarea']
    frmdte=request.POST['textfield2']
    todate=request.POST['textfield3']
    pg=request.POST['pg']

    o=offers()
    o.offer=offr
    o.dscrptn=dscption
    o.fromdte=frmdte
    o.todte=todate
    o.PACKAGE_id=pg
    o.BUSSINESS = bussiness.objects.get(LOGIN_id=request.session['lid'])
    o.save()
    return busns_addofr_load(request)

def busns_offerdelet_load(request,cid):
    o=offers.objects.get(id=cid)
    o.delete()
    return busns_addofr_load(request)


def busns_usrtble_post(request):
    nme=request.POST['textfield']
    email=request.POST['textfield2']
    contact=request.POST['textfidel3']
    name=request.POST['textfield4']
    days=request.POST['textfield5']
    return 'ok'



def busns_vwcstmrpkg_load(request):
    res=custompackage.objects.filter(stus='pending')
    return render(request,'bussiness/view_cstmr_pachgd_snd_intrst.html',{'res':res})
def busns_sendintrest(request,cpid):
    return render(request,'bussiness/sendintrest.html',{'cpid':cpid})
def busns_sendintrest_post(request):
    dscpetn=request.POST['textarea']
    cpakageid=request.POST['cpid']

    sd=interest()
    sd.descrtn=dscpetn
    sd.BUSSINESS_id=request.session['id']
    sd.CUSTOMPACKAGE_id=cpakageid
    sd.stats='pending'
    sd.save()

    return busns_vwcstmrpkg_load(request)
def busns_vwcmtdpkg_load(request):
    res=interest.objects.filter(BUSSINESS=request.session['id'])
    return render(request,'bussiness/viewcmmited_custmed_pckage.html',{'res':res})

def busns_vwpkgtbl_load(request,pid):
    data=packgesub.objects.filter(PACKAGE=pid)
    return render(request,'bussiness/viewpackagetable.html',{'pid':pid,'data':data})
def busns_vwpkgtbl_post(request):
    pid=request.POST['pid']
    day=request.POST['textfield']
    food=request.POST['checkbox']

    dscprtn=request.POST['textarea']
    plcinfo=request.POST['textfield2']
    pc=packgesub()
    pc.PACKAGE_id=pid
    pc.foodinfo=food
    pc.descrptn=dscprtn
    pc.place=plcinfo
    pc.save()
    return busns_vwpkgtbl_load(request, pid)


def busns_subpackage_del(request,psid,pid):
    c=packgesub.objects.get(id=psid)
    c.delete()
    return busns_vwpkgtbl_load(request,pid)


def busns_vwpndgbkg_load(request):
    res=booking.objects.filter(status='pending')

    return render(request,'bussiness/viewpendingbooking.html',{'res':res})


def busns_vwpndgbkg_post(request):
    d1=request.POST["d1"]
    d2=request.POST["d2"]
    res=booking.objects.filter(bokgdte__range=(d1,d2),status='pending')

    return render(request,'bussiness/viewpendingbooking.html',{'res':res})


def busns_vwpndgaccpt_post(request):
    bid = str(request.session["booking"])

    button = request.POST["Submit"]
    if button == "Accept":
        booking.objects.filter(id=bid).update(status='Accepted')
    else:
        booking.objects.filter(id=bid).update(status='Rejected')
    return busns_usrtble_load(request,str(bid),str(request.session["pid"]))

def busns_usrtble_load(request,bid,pid):
    request.session["booking"]=bid
    request.session["pid"] = pid
    uersdata=booking.objects.get(id=bid)
    p_sub_info=packgesub.objects.filter(PACKAGE=pid)
    pp=package.objects.get(id=pid)
    return render(request,'bussiness/usertable.html',{'userinfo':uersdata,'package':p_sub_info,'pp':pp})

def busns_vwapprgbkg_load(request):
    res=booking.objects.filter(status='Accepted')
    return render(request,'bussiness/viewapprovedbooking.html',{'res':res})



def busns_vwapprgbkg_loadpost(request):
    date1=request.POST['d1']
    date2=request.POST['d2']
    res=booking.objects.filter(date__rang=(date1,date2),status='Ápproved')
    return render(request,'bussiness/viewapprovedbooking.html',{'res':res})

def busns_app_usrtble_load(request,bid,pid):
    request.session["booking"]=bid
    request.session["pid"] = pid
    uersdata=booking.objects.get(id=bid)
    p_sub_info=packgesub.objects.filter(PACKAGE=pid)
    pp=package.objects.get(id=pid)
    return render(request,'bussiness/APPusertable.html',{'userinfo':uersdata,'package':p_sub_info,'pp':pp})

def busns_vwapprbkg_post(request):
    d1=request.POST["d1"]
    d2=request.POST["d2"]
    res=booking.objects.filter(bokgdte__range=(d1,d2),status='Approved')

    return render(request,'bussiness/viewapprovedbooking.html',{'res':res})

# def busns_vwusrtg_load(request):
#     res=rating.objects.all()
#     return render(request,'bussiness/viewuserrating.html',{'res':res})



def busns_vwusrtg_load(request):
    qry=rating.objects.filter(BUSSINESS_id=request.session["id"])
    ar_rt = []
    # for im in range(0, len(qry)):
    #     val = str(qry[im]["avg(rate.review)"])
    #     ar_rt.append(val)
    # fs = "/static/star/full.jpg"
    # hs = "/static/star/half.jpg"
    # es = "/static/star/empty.jpg"
    # arr = []
    # print(ar_rt)
    # for rt in ar_rt:
    #         print(rt)
    #         a = float(rt)
    #
    #         if a >= 0.0 and a < 0.4:
    #             print("eeeee")
    #             ar = [es, es, es, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 0.4 and a < 0.8:
    #             print("heeee")
    #             ar = [hs, es, es, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 0.8 and a < 1.4:
    #             print("feeee")
    #             ar = [fs, es, es, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 1.4 and a < 1.8:
    #             print("fheee")
    #             ar = [fs, hs, es, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 1.8 and a < 2.4:
    #             print("ffeee")
    #             ar = [fs, fs, es, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 2.4 and a < 2.8:
    #             print("ffhee")
    #             ar = [fs, fs, hs, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 2.8 and a < 3.4:
    #             print("fffee")
    #             ar = [fs, fs, fs, es, es]
    #             arr.append(ar)
    #
    #         elif a >= 3.4 and a < 3.8:
    #             print("fffhe")
    #             ar = [fs, fs, fs, hs, es]
    #             arr.append(ar)
    #
    #         elif a >= 3.8 and a < 4.4:
    #             print("ffffe")
    #             ar = [fs, fs, fs, fs, es]
    #             arr.append(ar)
    #
    #         elif a >= 4.4 and a < 4.8:
    #             print("ffffh")
    #             ar = [fs, fs, fs, fs, hs]
    #             arr.append(ar)
    #
    #         elif a >= 4.8 and a <= 5.0:
    #             print("fffff")
    #             ar = [fs, fs, fs, fs, fs]
    #             arr.append(ar)
    # print(arr)
    # return render(request,'bussiness/viewuserrating.html',{'res':qry,'r1':arr,'ln':len(arr)})
    return render(request,'bussiness/viewuserrating.html',{'res':qry})


def busns_vwusrtg_post(request):
    dtefrm=request.POST['textfield']
    to=request.POST['textfield2']
    return 'ok'
def busns_view_send_intrest(request):
    res=interest.objects.filter(BUSSINESS=request.session['id'])
    return render(request,'bussiness/viewsendintrest.html',{'res':res})


def busns_chat_load(request):
    return render(request, "bussiness/fur_chat.html")

# drviewmsg
def busnsviewmsg(request,receiverid):

    bid=request.session["id"]
    print("!!!!!!!!!!",bid,receiverid)
    doc=bussiness.objects.get(id=bid)
    obj=chat.objects.filter(BUSSINESS=doc,USER=users.objects.get(id =receiverid))
    user_data=users.objects.get(id=receiverid)
    print("********************",obj)

    res = []
    for i in obj:
        s = {'id':i.pk, 'date':i.date,'msg':i.message,'type':i.messagetype}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res,'name':user_data.name,'image':user_data.image})

def chatview(request):
    da = users.objects.all()
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email,'image':i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})

# doctor_insert_chat
def bussiness_insert_chat(request,receiverid,msg):

    dlid= request.session["id"]
    dobj=bussiness.objects.get(id=dlid)

    obj=chat()
    obj.USER=users.objects.get(pk=receiverid)
    obj.BUSSINESS=dobj
    obj.message=msg
    obj.messagetype='bussiness'
    obj.date=datetime.datetime.now().date()
    obj.save()
    return JsonResponse({'status':'ok'})



########################user##############################


def user_signup_load(request):
    return render(request,'user/signup1.html')
def user_home_load(request):
    return render('user/index.html')



def user_signup_post(request):
    nme=request.POST['textfield']

    image=request.FILES['file']
    fs=FileSystemStorage()
    nme1=datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
    filename=nme1+".jpg"
    fs.save(filename,image)
    url="/media/"+filename
    em=request.POST['textfield2']
    pl=request.POST['textfield4']
    po=request.POST['tex_ptfield6']
    pi=request.POST['textfield7']
    dist=request.POST['textfield9']
    ph=request.POST['textfield13']
    pwd=request.POST['textfield14']
    cpwd=request.POST['textfield15']


    lo=login()
    lo.username=em
    lo.password=pwd
    lo.type="users"
    lo.save()

    ob=users()
    ob.name=nme
    ob.image=url
    ob.email = em
    ob.place=pl
    ob.pin=pi
    ob.post=po
    ob.district=dist
    ob.contact=ph
    ob.LOGIN_id=lo.id
    ob.save()
    return render(request,"a.html")

def user_ChngePaswrd_load(request):
    return render(request,'user/Changepassword.html')
def user_ChngePaswrd_post(request):
    lid=request.session['lid']
    crntpswrd=request.POST['textfield2']
    nwpswrd=request.POST['textfield3']
    retppswrd=request.POST['textfield4']

    obj1=login.objects.get(id=lid,password=crntpswrd)
    if nwpswrd==retppswrd:
        obj1.password=retppswrd
        obj1.password=nwpswrd
        obj1.save()
    else:
        return HttpResponse("invalid")

    return user_ChngePaswrd_load(request)


def user_viewtourstplce_load(request):
    res=tourstplce.objects.all()
    return render(request,'user/viewtouristplace.html',{'res':res})


def user_Bussines_load(request):
    res=bussiness.objects.all()
    print(res)
    return render(request,'user/Bussines.html',{"res":res})

def user_feedback_load(request):
    return render(request,'user/feedback.html')

def user_feedback_post(request):
    fed=request.POST['textarea1']
    uid=request.session["id"]

    fd=feedback()
    fd.feedback=fed
    fd.USER_id=uid
    fd.replay='pending'
    fd.date=datetime.datetime.now().date()
    fd.save()
    return render(request,'user/feedback.html')

def user_complaint_load(request):
    return render(request,'user/complaint.html')

def user_complaint_post(request):
    comp=request.POST['textarea2']
    uid=request.session["id"]
    co=complaints()
    co.complaint=comp
    co.USER_id=uid
    co.date=datetime.datetime.now().date()
    co.replay="pending"
    co.contact=users.contact
    co.save()
    return render(request,'user/complaint.html')

def user_offer_load(request):
    res=offers.objects.all()
    return render(request,'user/offer.html',{'res':res})
def user_view_package_load(request,id):
    res=package.objects.filter(BUSSINESS_id=id)
    return  render(request,'user/viewpackage.html',{'res':res})

def user_view_service(request,id):
    res=service.objects.filter(BUSSINESS_id=id)
    return render(request,'user/viewservice.html',{'res':res})

def user_view_complaint_load(request):
    res=complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/view complaint.html',{'res':res})

def user_view_profile(request):
    c=users.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/viewprofile.html',{'c':c})

def user_view_profile_post(request):

    nm=request.POST['textfield']
    em=request.POST['textfield2']
    plc=request.POST['textfield3']
    po=request.POST['textfield4']
    pin=request.POST['textfield5']
    dis=request.POST['textfield7']
    ph=request.POST['textfield11']

    if 'file' in request.FILES:

        pr = request.FILES['file']
        fs = FileSystemStorage()
        name1 = datetime.datetime.now().strftime("%y-%m-%d-%h-%M")
        filename = name1 + ".jpg"
        fs.save(filename, pr)
        url = '/media/' + filename

        usersobj=users.objects.get(LOGIN_id=request.session['lid'])
        usersobj.image=url;
        usersobj.name=nm;
        usersobj.email=em;
        usersobj.place=plc;
        usersobj.post=po;
        usersobj.pin=pin;
        usersobj.district=dis;
        usersobj.contact=ph;
        usersobj.save()
        return redirect('/rwt/user_view_profile/')
    else:
        usersobj = users.objects.get(LOGIN_id=request.session['lid'])

        usersobj.name = nm;
        usersobj.email = em;
        usersobj.place = plc;
        usersobj.post = po;
        usersobj.pin = pin;
        usersobj.district = dis;
        usersobj.contact = ph;
        usersobj.save()
        return redirect('/rwt/user_view_profile/')

def user_booking_load(request,id):
    import datetime
    toda=datetime.datetime.now()
    res=booking()
    res.USER_id=request.session['id']
    res.PACKAGE_id=id
    res.status="pending"
    res.bokgdte=toda
    res.save()
    return  HttpResponse("<script>alert('Booking Done successfully');window.location='/rwt/user_Bussines_load/'</script>")

def user_sendcustom_package_load(request):
    return render(request,'user/sendcustompackage.html')
def user_sendcustom_package_post(request):
    dte=request.POST['textfield1']
    frplce=request.POST['textfield2']
    toplce=request.POST['textfield3']
    foodinfo=request.POST['textfield4']
    frmdte=request.POST['textfield5']
    disc=request.POST['textfield6']

    cu=custompackage()
    cu.days=dte
    cu.frmplce=frplce
    cu.toplce=toplce
    cu.foodinfo=foodinfo
    cu.frmdte=frmdte
    cu.dscrptn=disc
    cu.USER_id=request.session["id"]
    cu.stus='pending'
    cu.save()
    return render(request,'user/sendcustompackage.html')

def user_view_custm_package_load(request):
    res=custompackage.objects.filter(USER=request.session["id"])
    return render(request,'user/view_cstmr_pachgd_view_intrst.html',{'res':res})
def user_view_intrest_load(request,cpid):
    res=interest.objects.filter(CUSTOMPACKAGE=cpid)
    return render(request,'user/viewintrest.html',{'res':res,'cpid':cpid})

def user_accept_intrest_load(request,intrest_id,cpid):
    res=interest.objects.filter(id=intrest_id).update(stats='Accepted')
    res=custompackage.objects.filter(id=cpid).update(stus='completed')
    # return user_view_intrest_load(request,cpid)
    return user_view_custm_package_load(request)

def user_reject_intrest_load(request,intrest_id,cpid):
    res=interest.objects.filter(id=intrest_id).update(stats='reject')
    return user_view_intrest_load(request,cpid)

def user_more_package_load(request,id):
    res=packgesub.objects.filter(PACKAGE_id=id)
    return render(request,'user/morepackage.html',{'res':res})

def user_view_history_load(request):
    res=booking.objects.filter(USER_id=request.session['id'])
    return render(request,'user/viewhistory.html',{'res':res})

def user_add_rating_load(request,id):
    return render(request,'user/addrating.html',{"x":id})


def user_add_rating_post(request):
    dt=request.POST['text2']
    re=request.POST['textarea1']
    bi = request.POST['textarea1']
    bid = request.POST['nn']
    rat=request.POST['ratings']
    ra=rating()
    ra.date=dt
    ra.review=re
    ra.rate=rat
    ra.USER_id = request.session['id']
    ra.BUSSINESS_id=bid
    ra.save()

    return render(request,'user/addrating.html')

def user_view_rating_load(request):
    res=rating.objects.all()
    return render(request,'user/viewrating.html',{'res':res})
#----------------------------------------user chattttttttttttttttttt=======================


def user_chat_load(request):
    return render(request, "user/fur_chat.html")

# drviewmsg
def userviewmsg(request,receiverid):

    uid=request.session["id"]
    print("!!!!!!!!!!",uid,receiverid)
    doc=users.objects.get(id=uid)
    obj=chat.objects.filter(BUSSINESS=bussiness.objects.get(id =receiverid),USER=doc)
    user_data=bussiness.objects.get(id=receiverid)
    print("********************",obj)

    res = []
    for i in obj:
        s = {'id':i.pk, 'date':i.date,'msg':i.message,'type':i.messagetype}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res,'name':user_data.name,'image':user_data.image})

def userchatview(request):
    da = bussiness.objects.all()
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email,'image':i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})

# doctor_insert_chat
def user_insert_chat(request,receiverid,msg):

    ulid= request.session["id"]
    user=users.objects.get(id=ulid)

    obj=chat()
    obj.USER=user
    obj.BUSSINESS=bussiness.objects.get(pk=receiverid)
    obj.message=msg
    obj.messagetype='user'
    obj.date=datetime.datetime.now().date()
    obj.save()
    return JsonResponse({'status':'ok'})




#----------------------------chat finish---


#####>......................................public..............

def public_mainhome_load(request):
    return render(request,'public/index2.html')

def public_veiwbussunes_load(request):
    res=bussiness.objects.all()
    return render(request,'public/Bussines.html',{'res':res})

def public_veiwservc_load(request):
    res=service.objects.all()
    return render(request,'public/servicemanagement.html',{'res':res})

def public_viewratg_load(request):
    res=rating.objects.all()
    return render(request,'public/viewrating.html',{'res':res})


def public_viewtourstplce_load(request):
    res=tourstplce.objects.all()
    return render(request,'public/viewtouristplace.html',{'res':res})

def public_searching_post(request):

    return public_viewtourstplce_load(request)