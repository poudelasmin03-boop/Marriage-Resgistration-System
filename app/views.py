from django.shortcuts import render,get_object_or_404,redirect
from PIL import Image
import pytesseract

import re
from django.core.mail import send_mail
from django.conf import settings
from .models import Bride,Groom,MarrigaeRequest,MarriageRecorde
from django.contrib.auth import authenticate,login as login_auth,logout as logout_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
import datetime
import random
from  django.db.models import Q


#====================================
# ==========Home Views=====
# ====================================

def home_views(request):
    return render(request,'home.html')


'''Id register'''
def register(request):
  
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

      
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        user.save()
        return redirect('login')

    return render(request,"register.html")
  
  
def logout(request):
  logout_auth(request)
  messages.success(request,'You are successfully logout')
  return redirect('home')










'''Id login '''


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if not User.objects.filter(username= username).exists():
            return render(request,'login.html',{"Error":'Username not exists'})
        if not  user:
            return render(request,'login.html',{"Error":"Incorrect Password"})
            
        login_auth(request,user)
        return redirect('home')

    return render(request,'login.html')

'''================Marriage Register================'''
def register_marriage_views(request):
    if request.method == "POST":
        brideName = request.POST.get('brideName')
        brideDOB = request.POST.get('brideDOB')
        brideFatherName = request.POST.get('brideFatherName')
        brideMotherName = request.POST.get('brideMotherName')
        brideAddress = request.POST.get('brideAddress')
        brideEmail = request.POST.get('brideEmail')
        brideNidNo = request.POST.get('brideNidNo')
        
        brideImage = request.FILES.get('brideImage')
        brideNidImage = request.FILES.get('brideNidImage')
        
        
        
        
        '''=================Groom Data Enter  ======='''
        groomName = request.POST.get('groomName')
        groomDOB = request.POST.get('groomDOB')
        groomFatherName = request.POST.get('groomFatherName')
        groomMotherName = request.POST.get('groomMotherName')
        groomAddress = request.POST.get('groomAddress')
        groomNidNo = request.POST.get('groomNidNo')
        groomEmail = request.POST.get('groomEmail')
        
        request.session['set_email'] =groomEmail
        
        groomImage = request.FILES.get('groomImage')
        groomNidImage = request.FILES.get('groomNidImage')
       
        
         
        ''' ========Marriage Request============='''
        marriageDate = request.POST.get('marriageDate')
        registrationDate = request.POST.get('registrationDate')
        place_of_marriage=  request.POST.get('place_of_marriage')
        
        
        
        #==========================================================================OCR + Regex==================
        # ==================================================== 
        
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
    
        image1 = Image.open(groomNidImage)
        image = Image.open(brideNidImage)
        
        print(image)
        print(image1)
        
        keywords = [
              "LICENSE",
              "LICENSENO",
              "NEPAL",
              'CITIZENSHIP'
        ]
        
        text = pytesseract.image_to_string(image)
        text1 = pytesseract.image_to_string(image1)

        
        text = text.replace(" ","").upper()
        text1 = text1.replace(" ","").upper()
        
        
        print(groomDOB)
        # print(type(groomdob))
        
        
        
        
        
        entered_text = re.sub(r'[^0-9A-Za-z]','',str(brideNidNo).upper())
        entered_text1 = re.sub(r'[^0-9A-Za-z]','',str(groomNidNo).upper())
        groomdob = re.sub(r'[a-zA-Z]','',groomDOB.upper())
        bridedob = re.sub(r'[a-zA-Z]','',brideDOB.upper())
        
        print(entered_text,entered_text1)
        print(type(entered_text))
        
        counter = 0
        
        for i in keywords:
           if i in text.upper():
               counter+=1
        for j in keywords:
            if j in text1.upper():
                counter+=1       
        
        clean_text = re.sub(r'[^0-9a-zA-z]','',str(text).upper())
        clean_text1 = re.sub(r'[^0-9a-zA-z]','',str(text1).upper())
    
        if entered_text in clean_text:
           counter +=1
        if bridedob in clean_text:
            counter+=1 
        if entered_text1 in clean_text1 :
            counter +=1  
        if groomdob in clean_text1:
            counter+=1    
            
        print(counter)    
        if counter < 6: 
            return render(request,'marriageregister.html',{'error':'Document isnot valid','brideName':brideName,
                    'brideDOB':brideDOB,
                    'brideAddress':brideAddress,
                    'brideEmail':brideEmail,
                    'brideFatherName':brideFatherName,
                     'brideNidNo':brideNidNo,
                    'brideMotherName':brideMotherName,
                    'groomName':groomName,
                    'groomDOB':groomDOB,
                    'groomFatherName':groomFatherName,
                    'groomMotherName':groomMotherName,
                    'groomNidNo':groomNidNo,
                    'groomEmail':groomEmail,
                    'groomAddress':groomAddress})    
           
        #   ================================================
        # #   ==============End of OCR=====================
        #   =============================================   
        
        bride = Bride.objects.create(
            brideName = brideName,
            brideDOB =brideDOB,
            brideEmail =brideEmail,
            brideFatherName =brideFatherName,
            brideMotherName =brideMotherName,
            brideAddress = brideAddress,
            brideNidNo = brideNidNo,
            brideImage = brideImage,
            brideNidImage = brideNidImage,
            is_valid = True
        )    
        
        groom = Groom.objects.create(
                    groomName = groomName,
                    groomDOB =groomDOB,
                    groomEmail =groomEmail,
                    groomFatherName =groomFatherName,
                    groomMotherName =groomMotherName,
                    groomAddress = groomAddress,
                    groomNidNo = groomNidNo,
                    groomImage = groomImage,
                    groomNidImage = groomNidImage,
                    is_document_valid = True,
                 
                )
        
        
        MarrigaeRequest.objects.create(
            groom = groom,
            bride = bride,
            marriageDate =marriageDate, 
            registrationDate =registrationDate,
            place_of_marriage = place_of_marriage
            
            
        )
      
        
        return render(request,'home.html',{'msg':"Successfully Register"})       
    return render(request,'marriageregister.html')




###=====================================
# ==============REquest page for admin====
# ====================================

def request_page_views(request):
    details  = MarrigaeRequest.objects.all()
    return render(request,'requestpage.html',{'details':details})



#========================================
#======Detials of bride and Bride======
# ========-===============
def view_details(request,id):
    data = get_object_or_404(MarrigaeRequest,id=id)
    return render(request,'seeDetails.html',{'data':data})

def image_views(request):
    src =  request.GET.get('src')
    return render(request,'image.html',{'src':src})




'''===================Approve by Admin======================'''
def admin_approve_views(request,id):
    data  = get_object_or_404(MarrigaeRequest,id=id)
    get_email = data.groom.groomEmail or request.session.get('set_email')

   
    data.is_valid = True
    data.status = "Approve"
    data.save()


    
    
   
    
    certificate = MarriageRecorde.objects.filter(marriageRequest=data).first()
    if not certificate:
      certificateNo = random.randint(100000,999999)     
      certificateNo = str(certificateNo)  
      MarriageRecorde.objects.create(marriageRequest=data,certificateNo=certificateNo)
    if get_email:
        subject = "Marriage Registration Application Approval"
        url = request.build_absolute_uri(
            reverse('certificate', args=[data.id])
        )
        text_content = f"""
    Dear {data.groom.groomName},
    
    Your marriage registration application has been Approved.
    
    Please Check your marriage certificate.
    
    Regards,
    Marriage Registration Office
    E-Governance System
    """
        html_content = f"""
     <span>Click Here to Download your certificate</span>
     <a href="{url}">Click Here</a>
    """
        
        try:
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@egovernance.gov'),
                to=[get_email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=True)
        except Exception as e:
            print("Email sending failed:", e)

    request.session.pop('set_email', None)
    return redirect('request')


def admin_reject_view(request,id):
    data = get_object_or_404(MarrigaeRequest,id=id)
    subject = "Marriage Registration Application Rejected"
    get_email = data.groom.groomEmail or request.session.get('set_email')
    


    
    if get_email:
        text_content = f"""
Dear {data.groom.groomName},

Your marriage registration application has been rejected.

Reason:
Incorrect or unverifiable information or documents were provided.

Please review your information and submit the application again with accurate and valid documents.

Regards,
Marriage Registration Office
E-Governance System
"""

        html_content = f"""
    <html>
    <body style="margin:0; padding:0; background:#f4f6f8; font-family:Arial, sans-serif;">
        <div style="max-width:600px; margin:40px auto; background:white; border-radius:10px; overflow:hidden; box-shadow:0 3px 12px rgba(0,0,0,0.1);">
            <div style="background:#dc3545; color:white; padding:25px; text-align:center;">
                <h2 style="margin:0;">Marriage Registration</h2>
                <p style="margin:8px 0 0;">Application Status</p>
            </div>
            <div style="padding:30px;">
                <h3 style="color:#333;">Dear {data.groom.groomName},</h3>
                <p style="color:#555; line-height:1.6;">We regret to inform you that your marriage registration application has been rejected.</p>
                <div style="background:#fff3f3; border-left:5px solid #dc3545; padding:15px; margin:20px 0;">
                    <strong>Reason for Rejection:</strong>
                    <p style="margin-bottom:0;">Incorrect or unverifiable information or documents were provided.</p>
                </div>
                <p style="color:#555; line-height:1.6;">Please review the information you provided and submit the application again with accurate and valid documents.</p>
                <hr style="border:none; border-top:1px solid #eee;">
                <p style="color:#777; font-size:13px;">Thank you for using our E-Governance Marriage Registration System.</p>
                <p style="color:#333;"><strong>Marriage Registration Office</strong><br>E-Governance System</p>
            </div>
        </div>
    </body>
    </html>
    """

        try:
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@egovernance.gov'),
                to=[get_email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=True)
        except Exception as e:
            print("Email sending failed:", e)

    data.is_valid = False
    data.status = "Reject"
    data.save()
    request.session.pop('set_email', None)
    return redirect('request')


'''========Marriage Certificate when Admin approves'''


    
def marriageCertifficate(request,id=id):
        data =  get_object_or_404(MarriageRecorde,id=id)
        return render(request,'marraigecertificate.html',{'data':data})



'''=======================
----Help and info -----
======================'''
def help_views(request):
    return render(request,'help&info.html')
    
    
    
'''=======================
----Trems  and condition -----
======================'''    
def terms_condition_views(request):
    return render(request,'terms&condtion.html')


def privacy_view(request):
    return render(request, "privacy&policy.html")

def data_protection_view(request):
    return render(request, "dataprotection.html")


def disclaimer_view(request):
    return render(request, "disclaimer.html")

def contactus_views(request):
    return render(request, "contactus.html")

def adminlogin_views(request):
     if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if not User.objects.filter(username= username).exists():
                return render(request,'adminlogin.html',{"Error":'Username not exists'})
            if not  user:
                return render(request,'adminlogin.html',{"Error":"Incorrect Password"})
                
            login_auth(request,user)
            return redirect('home')
    
           
     return render(request,"adminlogin.html")


# ======================
# ==Dashboard========
# =========================



def dashboard_views(request):
    total_user = User.objects.count()
    total_request = MarrigaeRequest.objects.count()
    total_pending = MarrigaeRequest.objects.filter(status = 'Pending').count()
    total_reject = MarrigaeRequest.objects.filter(status = 'Reject').count()
    total_approve = MarrigaeRequest.objects.filter(status = 'Approve').count()
    request_data = MarrigaeRequest.objects.all().order_by('-id')[:5]
    
    
    
    
    
    return render(request,'dashboard.html',{
      'total_user':total_user, 
      'total_request':total_request,
      'total_pending':total_pending,
      'total_reject':total_reject,
      'total_approve':total_approve,
      'request_data':request_data
    })
  
  
# ==========
# MarrraigeVerification'
'''Addng also searching here'''
# ============    
def marriageverification(request):
    
  
     q = request.GET.get('q')
    
     if q: 
        q = q.strip()
        query = re.sub(r'^[0-9]','',q)
        data = MarriageRecorde.objects.filter(Q(marriageRequest__bride__brideNidNo__icontains = query) | Q(marriageRequest__groom__groomNidNo__icontains = query)).first()
        
        if data:    
            return render(request,'marriageverification.html',{'data' : data})
        else:
         return render(request,'marriageverification.html',{'error_msg':'erNo Marriage Record Foundror' })
     return render(
        request,
        'marriageverification.html'
    )