from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
import os
from student import Student_details

from train2 import Trainmodel
from face_recognition2 import face_recognition
class face_recognition_system():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x730+0+0")
        self.root.title("Face Recognition System")



         # first image
        img = Image.open("Images/img4.png")
        img = img.resize((483,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width='483',height='130')


        #second img
        img1 = Image.open("Images/IMG.png")
        img1 = img1.resize((483,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)


        first_label = Label(self.root,image=self.photoimg1)
        first_label.place(x=483,y=0,width='483',height='130')
        #third img
        img2 = Image.open("Images/img5.png")
        img2 = img2.resize((400,130),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root,image=self.photoimg2)
        first_label.place(x=966,y=0,width='400',height='130')
        
        
        # title label
        label_title = Label(self.root,text='FACE RECOGNITION ATTENDANCE SYSTEM ',font = ('times new roman',35,'bold'),bg='white',fg='red')
        label_title.place(x=0,y=130,width='1450',height='45')


        # Image Buttons .
        # ONE rOW

        # studetn details
        img4 = Image.open("Images/img6.png")
        img4 = img4.resize((220,180),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=140,y=220,width='220',height='180')

        b1_1 = Button(self.root,text='STUDENT DETAILS',cursor='hand2',command=self.student_details,font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=140,y=380,width='220',height='40')



        # face detection
        img5 = Image.open("Images/img8.png")
        img5 = img5.resize((220,180),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,command=face_recognition,cursor='hand2')
        b1.place(x=580,y=220,width='220',height='180')
        b2_2 = Button(self.root,text='FACE DETECTION',cursor='hand2',command=face_recognition,font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b2_2.place(x=580,y=380,width='220',height='40')


        #Attendance
        img6 = Image.open("Images/img9.png")
        img6 = img6.resize((220,180),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,cursor='hand2')
        b1.place(x=1020,y=220,width='220',height='180')
        b3_3 = Button(self.root,text='ATTENDANCE',cursor='hand2',font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b3_3.place(x=1020,y=380,width='220',height='40')


        # Image Buttons .
        # SECOND rOW

        #trainmdoel
        img7 = Image.open("Images/brain.png")
        img7 = img7.resize((220,180),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,command=Trainmodel,cursor='hand2')
        b1.place(x=140,y=450,width='220',height='180')
        b1_1 = Button(self.root,text='TRAIN MODEL',command=Trainmodel,cursor='hand2',font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=140,y=630,width='220',height='40')


        #Photos data
        img8 = Image.open("Images/phtos.png")
        img8 = img8.resize((220,180),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1=Button(self.root,image=self.photoimg8,command=self.open_img,cursor='hand2')
        b1.place(x=580,y=450,width='220',height='180')
        b1_1 = Button(self.root,text='PHOTOS DATA',command=self.open_img,cursor='hand2',font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=580,y=630,width='220',height='40')


        #developer
        img9 = Image.open("Images/devel.png")
        img9 = img9.resize((220,180),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1=Button(self.root,image=self.photoimg9,cursor='hand2')
        b1.place(x=1020,y=450,width='220',height='180')
        b1_1 = Button(self.root,text='DEVELOPER',cursor='hand2',font = ('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=1020,y=630,width='220',height='40')

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student_details(self.new_window)
    
    def open_img(self):
        os.startfile('DATA')


if __name__=='__main__':
   root=Tk()
   obj=face_recognition_system(root)
   root.mainloop()