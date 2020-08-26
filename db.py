#           DataBase
class student:
    
    
    def __init__(self, studentCode = "Kod", name = "Ad", surname = "Soyad", email = "Email", number = "Nömrə"):
        
        '''student class-nın parametrləri''' 
        
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
