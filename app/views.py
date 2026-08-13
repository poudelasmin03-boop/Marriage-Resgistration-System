from django.shortcuts import render,get_object_or_404,redirect
from PIL import Image
import pytesseract
import cv2
import re
from .models import BrideTable,GroomTable


#====================================
# ==========Home Views=====
# ====================================

def home_views(request):
    return render(request,'home.html')



def register_views(request):
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
        
        
        
        
        ###=================Groom========
        groomName = request.POST.get('groomName')
        groomDOB = request.POST.get('groomDOB')
        groomFatherName = request.POST.get('groomFatherName')
        groomMotherName = request.POST.get('groomMotherName')
        groomAddress = request.POST.get('groomAddress')
        groomNidNo = request.POST.get('groomNidNo')
        groomEmail = request.POST.get('groomEmail')
        
        groomImage = request.FILES.get('groomImage')
        groomNidImage = request.FILES.get('groomNidImage')
       
        
        
        
        # ==========================================================================OCR + Regex==================
        # ==================================================== 
        
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
        image = Image.open(brideNidImage)
        image1 = Image.open(groomNidImage)
        
        keywords = [
              "LICENSE",
              "LICENSENO",
              "NEPAL",
        ]
        
        text = pytesseract.image_to_string(image)
        text1 = pytesseract.image_to_string(image1)

        
        text = text.replace(" ","").upper()
        text1 = text1.replace(" ","").upper()

        
        
        entered_text = re.sub(r'[^0-9a-zA-z]','',str(brideNidNo).upper())
        entered_text1 = re.sub(r'[^0-9a-zA-z]','',str(groomNidNo).upper())
        
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
        if entered_text1 in clean_text1 :
            counter +=1  
            
        print(counter)    
        if counter < 4: 
            return render(request,'register.html',{'error':'Document isnot valid','brideName':brideName,
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
        # #   ==============Enf of OCR=====================
        #   =============================================   
        
        brideData = BrideTable.objects.create(
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
        
        groomData = GroomTable.objects.create(
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
                    bride = brideData
                )
        
        return render(request,'home.html',{'msg':"Successfully Register"})       
    return render(request,'register.html')




###=====================================
# ==============REquest page for admin====
# ====================================

def request_page_views(request):
    details  = GroomTable.objects.all()
    return render(request,'requestpage.html',{'details':details})



#========================================
#======Detials of bride and Bride======
# ========-===============
def view_details(request,id):
    data = get_object_or_404(GroomTable,id=id)
    return render(request,'seeDetails.html',{'data':data})

def image_views(request):
    src =  request.GET.get('src')
    return render(request,'image.html',{'src':src})




'''===================Approve by Admin======================'''
def admin_approve_views(request,id):
    
    data  = get_object_or_404(GroomTable,id=id)
    data.is_valid = True
    data.status = "Approve"
    data.save()
    return redirect('request')



def admin_reject_view(request,id):
    data =  get_object_or_404(GroomTable,id=id)
    data.is_valid=False
    data.status = "Reject"
    data.save()
    return redirect('request')
    
