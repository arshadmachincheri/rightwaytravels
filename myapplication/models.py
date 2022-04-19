from django.db import models

#...Create your models here.



class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class tourstplce(models.Model):
    name=models.CharField(max_length=50)
    descripion=models.CharField(max_length=100)
    image1=models.CharField(max_length=200)
    image2=models.CharField(max_length=200)
    image3 = models.CharField(max_length=200)
    openingtime = models.CharField(max_length=200)
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    latitude=models.CharField(max_length=20)
    longtitude=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)


class bussiness(models.Model):
    name= models.CharField(max_length=30)
    image= models.CharField(max_length=200)
    about=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    place=models.CharField(max_length=20)
    pin=models.CharField(max_length=10)
    city=models.CharField(max_length=20,default="")
    post=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20,default="")
    latitude=models.CharField(max_length=15,default="")
    logtitde=models.CharField(max_length=15,default="")
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=20)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)

class users(models.Model):

    name=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=20)
    post=models.CharField(max_length=10)
    district=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class complaints(models.Model):
    complaint=models.CharField(max_length=150)
    date=models.DateField(max_length=20)
    replay=models.CharField(max_length=200)
    USER=models.ForeignKey(users,on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,default="")

class feedback(models.Model):
    feedback=models.CharField(max_length=250)
    date=models.CharField(max_length=10)
    USER = models.ForeignKey(users, on_delete=models.CASCADE)

class rating(models.Model):
    rate=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    USER = models.ForeignKey(users,on_delete=models.CASCADE)
    BUSSINESS = models.ForeignKey(bussiness,on_delete=models.CASCADE)
    review=models.CharField(max_length=200,default="")

class service(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)


    BUSSINESS = models.ForeignKey(bussiness,on_delete=models.CASCADE)

class package(models.Model):
    packgenme=models.CharField(max_length=20)
    amount=models.CharField(max_length=10)
    totldays=models.CharField(max_length=10)
    BUSSINESS = models.ForeignKey(bussiness, on_delete=models.CASCADE)

class packgesub(models.Model):
    foodinfo=models.CharField(max_length=20)
    descrptn=models.CharField(max_length=100)
    place=models.CharField(max_length=20)
    PACKAGE = models.ForeignKey(package,on_delete=models.CASCADE)

class offers(models.Model):
    offer=models.CharField(max_length=20)
    dscrptn=models.CharField(max_length=50)
    fromdte=models.CharField(max_length=20)
    todte=models.CharField(max_length=20)
    PACKAGE = models.ForeignKey(package,on_delete=models.CASCADE)
    BUSSINESS = models.ForeignKey(bussiness ,on_delete=models.CASCADE)

class booking(models.Model):
    USER = models.ForeignKey(users,on_delete=models.CASCADE)
    PACKAGE = models.ForeignKey(package,on_delete=models.CASCADE)
    bokgdte=models.DateField()
    status=models.CharField(max_length=20)

class custompackage(models.Model):

    USER = models.ForeignKey(users,on_delete=models.CASCADE)
    days=models.CharField(max_length=10)
    frmplce=models.CharField(max_length=20)
    toplce=models.CharField(max_length=20)
    foodinfo=models.CharField(max_length=30)
    frmdte=models.CharField(max_length=10)
    dscrptn=models.CharField(max_length=100)
    stus=models.CharField(max_length=20,default='pending')

class interest(models.Model):
    CUSTOMPACKAGE = models.ForeignKey(custompackage,on_delete=models.CASCADE)
    BUSSINESS = models.ForeignKey(bussiness,on_delete=models.CASCADE)
    descrtn=models.CharField(max_length=100)
    stats=models.CharField(max_length=50)

class chat(models.Model):
    BUSSINESS = models.ForeignKey(bussiness,on_delete=models.CASCADE)
    USER = models.ForeignKey(users,on_delete=models.CASCADE)
    messagetype=models.CharField(max_length=50)
    date=models.CharField(max_length=10)
    message=models.CharField(max_length=200, default="")



