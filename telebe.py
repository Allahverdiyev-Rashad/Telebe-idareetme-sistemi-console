# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:32:14 2020

@author: MSI GAMING
"""
import re

class student:
    
    
    def __init__(self, studentCode = "Kod", name = "Ad", surname = "Soyad", email = "Email", number = "Nömrə"):
        
        ''' student class-nın parametrləri''' 
        
        self.studentCode = studentCode
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number
        
        
    
        

''' Nümunə üçün student class-dan 2 obyekt yaradılmışdır.
    İstəyə görə silinə də bilər'''
    
students = [student("123","Azər","Nəsibli","azer@gmail.com","+9941234567"),
            student("435","Elvin","Xələfov","elvinx@gmail.com","+9941325221")
            ]

  
def addStudent():
    
        ''' Daxil olan məlumatlar əsasında student class-dan obyekt
            yaradılır və students listinə əlavə edilir.
            Baş verə biləcək xətaların qarşısını almaq üçün while True daxilində yazılmışdır.
            Burada A tələbənin kodu, B tələbənin adı, C soyadı,
            D mail adresi, E isə nömrəsidir '''
            
        while True:
            
            A = input("Tələbənin 3 rəqəmli kodunu daxil edin: ")
            
            if len(A) != 3 or re.search("\s",A) or re.search("[a-zA-Z]",A):
            
                print("\n-----Səhvlik-----\n\nTələbə kodu 3 rəqəmli ədəd olmalıdır")
                
            else:
                
                break
        
            
        while True:
            
            B = input("Tələbənin adını daxil edin: ")
            
            if re.search("[0-9]",B) or re.search("\s",B):
                
                print("\n-----Səhvlik-----\n\nAd yalnız hərflərdən ibarət olmalıdır")              
            
            else:
                
                break
                
        
        while True:  
            
            C = input("Tələbənin soyadını daxil edin: ")
            
            if re.search("[0-9]",C) or re.search("\s",C):
                
                print("\n-----Səhvlik-----\n\nSoyad yalnız hərflərdən ibarət olmalıdır")
            
            else:
                
                break
            
        while True: 
            
            D = input("Tələbənin mail adresini daxil edin: ")
            
            if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',D) or re.search("\s",D):
            
                print("\n-----Səhvlik-----\n\nMail adresi düzgün deyil")
                
            else:
                
                break
                
        while True: 
            
            E = input("Tələbənin nömrəsini daxil edin: ")
            
            if not E.startswith('+994') or re.search("[a-zA-Z]",E) or re.search("\s",E):
            
                print("\n-----Səhvlik-----\n\nTələbənin mobil nömrəsi +994 ilə başlamalıdır və rəqəmlərdən ibarət olmalıdır")
                
            else:
                
                break
        
        students.append(student(A,B,C,D,E))
           
                      
            
def showAllStudentsData():
    
    ''' Hazırda students class-da olan məlumatların hamısını çap etmək üçün çağırılır'''
    
    for i in students:
        
        print(f"\nTələbənin kodu: {i.studentCode}\nTələbənin adı: {i.name}\nTələbənin soyadı: {i.surname}\n"
              f"Tələbənin mail adresi: {i.email}\nTələbənin nömrəsi: {i.number}\n")

def searchForName():
    
    ''' Tələbə adına görə axtarış etmək üçün çağırılır '''
    
    while True:
            
        Name = input("Tələbənin adını daxil edin: ")
            
        if re.search("[0-9]",Name) or re.search("\s",Name):
                
            print("\n-----Səhvlik-----\n\nAd yalnız hərflərdən ibarət olmalıdır")              
            
        else:
                
            break
        
    j = []
    
    for i in range(len(students)):
        
        if Name == students[i].name:
            
            j.append(students[i].name)
            
            print(f"Tələbənin kodu: {students[i].studentCode}\nTələbənin adı: {students[i].name}\n"
                  f"Tələbənin soyadı: {students[i].surname}\nTələbənin mail adresi: {students[i].email}\n"
                  f"Tələbənin nömrəsi: {students[i].number}")
            
        elif Name != students[i].name:
            
            j.append(students[i].name)
            
    if not Name in j:
        
        print("\n-----Səhvlik-----\n\nSiyahıda belə tələbə yoxdur\n\nAxtarışı dayandırmaq üçün 'dayan' əmrini daxil edin")
        
        searchForName()
            
            
def changeData():
    
    ''' Burada a tələbənin kodu, b tələbənin adı, c soyadı,
        d mail adresi, e isə nömrəsidir.Bu funksiya tələbələrin 
        məlumatlarını dəyişdirmək üçün çağırılır'''
        
    while True:
            
        a = input("Məlumatını dəyişmək istədiyiniz tələbənin kodunu daxil edin: ")
            
        if len(a) != 3 or re.search("\s",a) or re.search("[a-zA-Z]",a):
            
            print("\n-----Səhvlik-----\n\nTələbə kodu 3 rəqəmli ədəd olmalıdır")
                
        else:
                
            break
        
            
    while True:
            
        b = input("Tələbənin yeni adı: ")
            
        if re.search("[0-9]",b) or re.search("\s",b):
                
            print("\n-----Səhvlik-----\n\nAd yalnız hərflərdən ibarət olmalıdır")              
            
        else:
                
            break
                
        
    while True:  
            
        c = input("Tələbənin yeni soyadı: ")
            
        if re.search("[0-9]",c) or re.search("\s",c):
                
            print("\n-----Səhvlik-----\n\nSoyad yalnız hərflərdən ibarət olmalıdır")
            
        else:
                
            break
            
    while True: 
            
        d = input("Tələbənin yeni emaili: ")
            
        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',d) or re.search("\s",d):
            
            print("\n-----Səhvlik-----\n\nMail adresi düzgün deyil")
                
        else:
                
            break
                
    while True: 
            
        e = input("Tələbənin yeni nömrəsi: ")
            
        if not e.startswith('+994') or re.search("[a-zA-Z]",e) or re.search("\s",e):
            
            print("\n-----Səhvlik-----\n\nTələbənin mobil nömrəsi +994 ilə başlamalıdır və rəqəmlərdən ibarət olmalıdır")
                
        else:
                
            break
        
        
    for i in range(len(students)):
        
        if a == students[i].studentCode:
            
            students[i].name = b
            students[i].surname = c
            students[i].email = d
            students[i].number = e
            
            print((f"Tələbənin kodu: {students[i].studentCode}\nTələbənin adı: {students[i].name}\n"
                  f"Tələbənin soyadı: {students[i].surname}\nTələbənin mail adresi: {students[i].email}\n"
                  f"Tələbənin nömrəsi: {students[i].number}"))
            
def removeStudentData():
    
    ''' Burada x tələbənin kodudur.Bu funksiya students listindən 
        tələbələrin məlumatlarını silmək üçün çağırılır'''
    
    while True:
            
        x = input("Məlumatlarını silmək istədiyiniz tələbənin kodunu daxil edin: ")
            
        if len(x) != 3 or re.search("\s",x) or re.search("[a-zA-Z]",x):
            
            print("\n-----Səhvlik-----\n\nTələbə kodu 3 rəqəmli ədəd olmalıdır")
                
        else:
                
            break
        
    
    for i in range(len(students)):
        
        if x == students[i].studentCode:
            
            students.pop(i)            
            
            print("\n----------Tələbənin məlumatları silindi----------\n")
            
            break
           

''' Burada proqramdan istifadə qaydaları verilmişdir.
    Konsol aşağı sürüşdükcə qaydalar yuxarıda qaldığı üçün
    qaydaları çap edən rules funksiyası yaradılıb və 
    hər əməliyyatdan sonra çağırılır.'''

print("\n-----Proqram işə salındı-----\n")

def rules():
    
    print("\nİstifadə qaydaları aşağıdakı kimidir:\n1 - Tələbə əlavə et\n2 - Tələbə koduna görə tələbə məlumatlarını sil\n"
     "3 - Tələbə koduna görə tələbə məlumatlarını dəyişdir\n4 - Tələbə adına görə axtar və tələbənin məlumatlarına bax\n"
     "5 - Bütün tələbə məlumatlarını göstər\n6 - Proqramı sonlandır\n")

rules()

while True:   
    
    process = input("İcra etmək istədiyiniz əməliyyatı seçin: ")
    
    if process == "1":
        
        addStudent()
        rules()
        
    elif process == "2":
        
        removeStudentData()
        rules()
        
    elif process == "3":
        
        changeData()
        rules()
        
    elif process == "4":
        
        searchForName()
        rules()
        
    elif process == "5":
        
        showAllStudentsData()
        rules()
        
    elif process == "6":
        
        print("\n-----Proqram sonlandırıldı-----")
        
        break
    
    else:
        
        print("Daxil edilən məlumat səhvdir.Xahiş edirik yenidən yoxlayın")
        
  
    
    
    






