from functions import *

print("\n-----Proqram işə salındı-----\n")
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
          
