from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import threading
from dotenv import load_dotenv
import os


load_dotenv()
class Student_details():
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1450x730+0+0")
        self.root.title("Face Recognition System")
        self.db_config={
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "port":3306
        }
      
        # variables 
        self.var_course=StringVar()
        self.var_department=StringVar()
        self.var_section=StringVar()
        self.var_batch=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentid=StringVar()
        self.var_studentname=StringVar()
        self.var_classrollno=StringVar()
        self.var_universityrollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phonenumber=StringVar()
        self.var_email=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
        self.get_next_id()


         # first image
        img = Image.open("Images/img4.png")
        img = img.resize((483,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width='483',height='130')


        #second img
        img1 = Image.open("Images/student.png")
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
        
        
         
        img3=Image.open("Images/img6.png")
        img3 = img3.resize((1450,730),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1450,height=730)
         


        
        # title label
        label_title = Label(bg_img,text='STUDENT MANAGEMENT SESSION',font = ('times new roman',35,'bold'),bg='white',fg='darkgreen')
        label_title.place(x=0,y=0,width='1450',height='45')


        main_frame = Frame(bg_img,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=5,y=50,width=1350,height=600)

        #left tlabel frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Details',font = ('times new roman',13,'bold'),bg='white',fg='black')
        left_frame.place(x=10,y=10,width=660,height=500)
        
        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text='Current Course Information',font = ('times new roman',13,'bold'),bg='white',fg='black')
        current_course_frame.place(x=5,y=2,width=645,height=160)
     
        # Row 0 → Department + Course Type

        dep_label=Label(current_course_frame,text='Department',font=('times new roman',12,'bold'),bg='white')
        dep_label.grid(row=0,column=2,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=('times new roman',12,'bold'),width=17)
        dep_combo['values']=("Select Department",'CSE','CSE-AIML','ECE','ME','CE','EE','AE')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10)


        course_type_label=Label(current_course_frame,text='Course Type',font=('times new roman',12,'bold'),bg='white')
        course_type_label.grid(row=0,column=0,padx=10)

        course_type_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),width=17)
        course_type_combo['values']=("Select Course","B.Tech","BBA","BCA","M.Tech","MBA")
        course_type_combo.current(0)
        course_type_combo.grid(row=0,column=1,padx=2,pady=10)


        # Row 1 → Course + Batch

        section_label=Label(current_course_frame,text='Section',font=('times new roman',12,'bold'),bg='white')
        section_label.grid(row=1,column=0,padx=10)

        section_combo=ttk.Combobox(current_course_frame,textvariable=self.var_section,font=('times new roman',12,'bold'),width=17)
        section_combo['values']=("Select Section","A","B","C","D")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=2,pady=10)

        batch_label=Label(current_course_frame,text='Batch',font=('times new roman',12,'bold'),bg='white')
        batch_label.grid(row=1,column=2,padx=10)

        batch_combo=ttk.Combobox(current_course_frame,textvariable=self.var_batch,font=('times new roman',12,'bold'),width=17)
        batch_combo['values']=("Select Batch","2022-26","2023-27","2024-28","2025-29")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=3,padx=2,pady=10)


        # Row 2 → Year + Semester

        year_label=Label(current_course_frame,text='Year',font=('times new roman',12,'bold'),bg='white')
        year_label.grid(row=2,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),width=17)
        year_combo['values']=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=2,pady=10)


        semester_label=Label(current_course_frame,text='Semester',font=('times new roman',12,'bold'),bg='white')
        semester_label.grid(row=2,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('times new roman',12,'bold'),width=17)
        semester_combo['values']=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=2,column=3,padx=2,pady=10)


       
        # Student Information Frame
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text='Student Information',
                                    font=('times new roman',13,'bold'),bg='white',fg='black')
        class_student_frame.place(x=5,y=164,width=645,height=300)

   
      # Row 0 → Student id(autoGenerated)+ student name
               
        student_id_label=Label(class_student_frame,text='Student ID',font=('times new roman',12,'bold'),bg='white')
        student_id_label.grid(row=0,column=0,padx=10,pady=5)

        student_id_value=Label(class_student_frame,text=self.var_studentid,textvariable=self.var_studentid,font=('times new roman',15,'bold'),bg='white',fg='black')
        student_id_value.grid(row=0,column=1,padx=10,pady=5)
                
        student_name_label=Label(class_student_frame,text='Student Name',font=('times new roman',12,'bold'),bg='white')
        student_name_label.grid(row=0,column=2,padx=10,pady=5)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentname,width=20,font=('times new roman',12,'bold'))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5)


        

        # Row 1 →class Roll number+ Univ Roll No 
        class_roll_label=Label(class_student_frame,text='Class Roll No.',font=('times new roman',12,'bold'),bg='white')
        class_roll_label.grid(row=1,column=0,padx=10,pady=5)

        class_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_classrollno,width=20,font=('times new roman',12,'bold'))
        class_roll_entry.grid(row=1,column=1,padx=10,pady=5)

        Univ_rollNumber_label=Label(class_student_frame,text='Univ. Roll No.',font=('times new roman',12,'bold'),bg='white')
        Univ_rollNumber_label.grid(row=1,column=2,padx=10,pady=5)

        studentUniv_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_universityrollno,font=('times new roman',12,'bold'))
        studentUniv_entry.grid(row=1,column=3,padx=10,pady=5)



        # Row 2 → Gender +Phone 

        gender_label=Label(class_student_frame,text='Gender',font=('times new roman',12,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=5)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),width=18,state='readonly')
        gender_combo['values']=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5)


        DOB_label=Label(class_student_frame,text='DOB',font=('times new roman',12,'bold'),bg='white')
        DOB_label.grid(row=2,column=2,padx=10,pady=5)
        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('times new roman',12,'bold'))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5)

       
        
        # Row 3->>Phone+ Email
        phone_label=Label(class_student_frame,text='Phone No.',font=('times new roman',12,'bold'),bg='white')
        phone_label.grid(row=3,column=0,padx=10,pady=5)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phonenumber,width=20,font=('times new roman',12,'bold'))
        phone_entry.grid(row=3,column=1,padx=10,pady=5)

        email_label=Label(class_student_frame,text='Email ID',font=('times new roman',12,'bold'),bg='white')
        email_label.grid(row=3,column=2,padx=10,pady=5)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('times new roman',12,'bold'))
        email_entry.grid(row=3,column=3,padx=10,pady=5)

        # Radio BUttons
        
        radiobtn1=ttk.Radiobutton(class_student_frame,text='Take Photo Sample',variable=self.var_radio1,value='Yes')
        radiobtn1.grid(row=4,column=0,padx=15,pady=10)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,text='No Photo Sample',variable=self.var_radio1,value='No')
        radiobtn2.grid(row=4,column=1,padx=15,pady=10)


        # buttons first create frame then inside buttons
        # button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=10,y=190,width=620,height=35)

        save_btn=Button(btn_frame,text='Save',command=self.database_entry,width=18,font=('times new roman',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

    
        Update_btn=Button(btn_frame,text='Update',command=self.update_function,width=15,font=('times new roman',12,'bold'),bg='blue',fg='white')
        Update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text='delete',command=self.delete_Function,width=15,font=('times new roman',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text='Reset',command=self.reset_function,width=18,font=('times new roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=10,y=225,width=620,height=35)

        Take_Photo_btn=Button(btn_frame1,text='Take Photo',command=self.take_photo_thread,width=35,font=('times new roman',12,'bold'),bg='blue',fg='white')
        Take_Photo_btn.grid(row=0,column=0)
        
        Update_photo_btn=Button(btn_frame1,text='Update photo',width=35,font=('times new roman',12,'bold'),bg='blue',fg='white')
        Update_photo_btn.grid(row=0,column=1)









        #right tlabel frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Data',font = ('times new roman',13,'bold'),bg='white',fg='black')
        right_frame.place(x=680,y=10,width=660,height=500)
        
        # search System
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text='Search System',
                                    font=('times new roman',13,'bold'),bg='white',fg='black')
        search_frame.place(x=5,y=10,width=645,height=70)
        
        search_label=Label(search_frame,text='Search Bar',font=('times new roman',12,'bold'),bg='white')
        search_label.grid(row=0,column=0,padx=10,pady=2)
        
        Search_combo=ttk.Combobox(search_frame,font=('times new roman',12,'bold'),width=16,state='readonly')
        Search_combo['values']=("Select","Class Roll No","Univ Roll No","Phone Number")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=10,pady=2)

        
        Search_entry=ttk.Entry(search_frame,width=15,font=('times new roman',12,'bold'))
        Search_entry.grid(row=0,column=2,padx=10,pady=2)


        Search_btn=Button(search_frame,text='Search',width=10,font=('times new roman',11,'bold'),bg='blue',fg='white')
        Search_btn.grid(row=0,column=3,padx=5)

        ShowAll_btn=Button(search_frame,text='Show All',width=10,font=('times new roman',11,'bold'),bg='blue',fg='white')
        ShowAll_btn.grid(row=0,column=4)
 

        # table Frame 
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE
                                    )
        table_frame.place(x=5,y=85,width=645,height=370)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,columns=("StudentId","Name",'ClassRollNo','UnivRollNo','DOB','Gender','PhoneNumber','Email','Course','Department','Section','batch','year','Semester','picturedata'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("StudentId", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("ClassRollNo", text="Class Roll No")
        self.student_table.heading("UnivRollNo", text="University Roll No")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("PhoneNumber", text="Phone Number")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("picturedata", text="picturedata")
        
        self.student_table['show'] = 'headings'
        for col in ("StudentId","Name","ClassRollNo","UnivRollNo","DOB","Gender",
            "PhoneNumber","Email","Course","Department","Section","batch","year","Semester",'picturedata'):
               self.student_table.column(col, width=110, anchor=CENTER)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    def get_next_id(self):
      conn = mysql.connector.connect(**self.db_config)
      cursor = conn.cursor()

      cursor.execute("SELECT COUNT(*) FROM student")
      count = cursor.fetchone()[0]

      next_id = count + 1
      self.var_studentid.set(next_id)

      conn.close()

    def check_duplicate(self):
        print(self.db_config)
        conn = mysql.connector.connect(**self.db_config)
        my_cursor = conn.cursor()
        my_cursor.execute("""SELECT * FROM student WHERE (name=%s AND class_roll_no=%s) OR (name=%s AND university_roll_no=%s)""",(
                  self.var_studentname.get().lower(),
                  self.var_classrollno.get(),
                  self.var_studentname.get().lower(),
                  self.var_universityrollno.get()
               ))

        result = my_cursor.fetchone()
        conn.close()

        if result:
                  messagebox.showerror("Error","Student already exists!")
                  return True
        return False
        #DAtabase entry for Save Button
    def database_entry(self):
         
         if (self.var_department.get() == "Select Department" or
            self.var_course.get() == "Select Course" or
            self.var_section.get() == "Select Section" or
            self.var_batch.get() == "Select Batch" or
            self.var_year.get() == "Select Year" or
            self.var_semester.get() == "Select Semester" or
            self.var_studentname.get() == "" or
            self.var_classrollno.get() == "" or
            self.var_universityrollno.get() == "" or
            self.var_gender.get() == "Select Gender" or
            self.var_dob.get() == "" or
            self.var_phonenumber.get() == "" or
            self.var_email.get() == ""):

            messagebox.showerror("Error", "All fields are required!",parent=self.root)
         elif len(self.var_phonenumber.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits")
         elif "@" not in self.var_email.get():
            messagebox.showerror("Error", "Invalid Email")
         else:
            try:
               
               conn = mysql.connector.connect(**self.db_config)
               my_cursor = conn.cursor()
               if self.check_duplicate():
                   return 
               

               my_cursor.execute("""
               INSERT INTO student 
               (name, class_roll_no, university_roll_no, dob, gender, phone, email, 
               course, department, section, batch, year, semester,picturedata)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
               """,(
                  self.var_studentname.get().lower(),
                  self.var_classrollno.get(),
                  self.var_universityrollno.get(),
                  self.var_dob.get(),
                  self.var_gender.get(),
                  self.var_phonenumber.get(),
                  self.var_email.get(),
                  self.var_course.get(),
                  self.var_department.get(),
                  self.var_section.get(),
                  self.var_batch.get(),
                  self.var_year.get(),
                  self.var_semester.get(),
                  self.var_radio1.get()
                  
               ))

               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success", "Data Saved Successfully!",parent=self.root)

            except Exception as e:
                messagebox.showinfo('Error',e,parent=self.root)
                
   ### Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(**self.db_config)
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
               self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()



   ### get cursor
    def get_cursor(self,event):
      cursor_focus = self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content['values']
      self.var_studentid.set(data[0])
      self.var_studentname.set(data[1])
      self.var_classrollno.set(data[2])
      self.var_universityrollno.set(data[3])
      self.var_dob.set(data[4])
      self.var_gender.set(data[5])
      self.var_phonenumber.set(data[6])
      self.var_email.set(data[7])
      self.var_course.set(data[8])
      self.var_department.set(data[9])
      self.var_section.set(data[10])
      self.var_batch.set(data[11])
      self.var_year.set(data[12])
      self.var_semester.set(data[13])
      self.var_radio1.set(data[14])

      # Update data
    def update_function(self):
        if (self.var_department.get() == "Select Department" or
            self.var_course.get() == "Select Course" or
            self.var_section.get() == "Select Section" or
            self.var_batch.get() == "Select Batch" or
            self.var_year.get() == "Select Year" or
            self.var_semester.get() == "Select Semester" or
            self.var_studentname.get() == "" or
            self.var_classrollno.get() == "" or
            self.var_universityrollno.get() == "" or
            self.var_gender.get() == "Select Gender" or
            self.var_dob.get() == "" or
            self.var_phonenumber.get() == "" or
            self.var_email.get() == ""):

            messagebox.showerror("Error", "All fields are required!",parent=self.root)
        elif len(self.var_phonenumber.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits")
        elif "@" not in self.var_email.get():
            messagebox.showerror("Error", "Invalid Email")
        else:
            try:
                Update = messagebox.askyesno("Update","Do You Want To Update This Details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(**self.db_config)
                    my_cursor = conn.cursor()
                    # checking for Already Existed Student Roll Number
                    my_cursor.execute("""
                     SELECT * FROM student 
                     WHERE ((name=%s AND class_roll_no=%s) 
                     OR university_roll_no=%s)
                     AND student_id != %s
                     """,(
                        self.var_studentname.get(),
                        self.var_classrollno.get(),
                        self.var_universityrollno.get(),
                        self.var_studentid.get()
                     ))

                    result = my_cursor.fetchone()

                    if result:
                        messagebox.showerror("Error","Student already exists!")
                        return

                    my_cursor.execute("""UPDATE Student SET 
                                      name=%s, class_roll_no=%s, university_roll_no=%s, dob=%s, gender=%s, phone=%s, email=%s, 
               course=%s, department=%s, section=%s, batch=%s, year=%s, semester=%s,picturedata=%s 
               WHERE student_id=%s""",(
                  self.var_studentname.get().lower(),
                  self.var_classrollno.get(),
                  self.var_universityrollno.get(),
                  self.var_dob.get(),
                  self.var_gender.get(),
                  self.var_phonenumber.get(),
                  self.var_email.get(),
                  self.var_course.get(),
                  self.var_department.get(),
                  self.var_section.get(),
                  self.var_batch.get(),
                  self.var_year.get(),
                  self.var_semester.get(),
                  self.var_radio1.get(),
                  self.var_studentid.get()
               ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student Details Successfully changed")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f'{str(e)}',parent=self.root)

   ## Delete Function
    def delete_Function(self):
        if self.var_studentid.get()=='':
               messagebox.showerror("Error","Student id Must be Required",parent=self.root)
        else:
            delete=messagebox.askyesno("Student Delete",'Do you Want TO Delete This Student',parent=self.root)
            if delete:
                try:
                     conn = mysql.connector.connect(**self.db_config)
                     my_cursor = conn.cursor()

                     deleteQuery="""DELETE FROM student WHERE student_id=%s"""
                     val=(self.var_studentid.get(),)

                     my_cursor.execute(deleteQuery,val)
                     conn.commit()
                     if my_cursor.rowcount == 0:
                        messagebox.showerror("Error","No record found to delete",parent=self.root)
                     else:
                        self.fetch_data()  
                        messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
                        
                except Exception as e:
                      messagebox.showerror("Error",str(e),parent=self.root)
                    
            else:
                if not delete:
                    return
            self.fetch_data()  
            conn.close()

      ## Reset Function
    def reset_function(self):   
     
      self.var_department.set("Select Department")
      self.var_course.set("Select Course")
      self.var_section.set("Select Section")
      self.var_batch.set("Select Batch")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_gender.set("Select Gender")

      self.get_next_id() 
      self.var_studentname.set("")
      self.var_classrollno.set("")
      self.var_universityrollno.set("")
      self.var_dob.set("")
      self.var_phonenumber.set("")
      self.var_email.set("")

      self.var_radio1.set("")

      










      #=====================================================
      # We are starting Opencv Tasks
      # generating Dataset from Images of Students 
     

    def take_photo_thread(self):
         t = threading.Thread(target=self.generate_dataset)
         t.start()
    def generate_dataset(self):
        if (self.var_department.get() == "Select Department" or
            self.var_course.get() == "Select Course" or
            self.var_section.get() == "Select Section" or
            self.var_batch.get() == "Select Batch" or
            self.var_year.get() == "Select Year" or
            self.var_semester.get() == "Select Semester" or
            self.var_studentname.get() == "" or
            self.var_classrollno.get() == "" or
            self.var_universityrollno.get() == "" or
            self.var_gender.get() == "Select Gender" or
            self.var_dob.get() == "" or
            self.var_phonenumber.get() == "" or
            self.var_email.get() == ""):

            messagebox.showerror("Error", "All fields are required!",parent=self.root)
        elif len(self.var_phonenumber.get()) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits")
        elif "@" not in self.var_email.get():
            messagebox.showerror("Error", "Invalid Email")
        else:
            try:
               conn = mysql.connector.connect(**self.db_config)
               my_cursor = conn.cursor()
               my_cursor.execute("SELECT * FROM Student")
               myresult=my_cursor.fetchall()

               id=self.var_studentid.get()
               self.var_radio1.set('Yes')
               my_cursor.execute("""UPDATE Student SET 
                                      name=%s, class_roll_no=%s, university_roll_no=%s, dob=%s, gender=%s, phone=%s, email=%s, 
               course=%s, department=%s, section=%s, batch=%s, year=%s, semester=%s,picturedata=%s 
               WHERE student_id=%s""",(
                  self.var_studentname.get().lower(),
                  self.var_classrollno.get(),
                  self.var_universityrollno.get(),
                  self.var_dob.get(),
                  self.var_gender.get(),
                  self.var_phonenumber.get(),
                  self.var_email.get(),
                  self.var_course.get(),
                  self.var_department.get(),
                  self.var_section.get(),
                  self.var_batch.get(),
                  self.var_year.get(),
                  self.var_semester.get(),
                  self.var_radio1.get(),
                  self.var_studentid.get()
               ))
               conn.commit()
               
               conn.close()

               #====load Predefined Model on aFace Frontals from opencv
               face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   # 1.3 scaling Factor 
                   # 5 Minimum Neigbour 

                   for (x,y,w,h) in faces:
                       face_cropped=img[y:y+h , x:x+w]
                       return face_cropped
               cap=cv2.VideoCapture(2,cv2.CAP_DSHOW)
               img_id=0
               while True:
                   ret,myframe=cap.read()
                   if not ret or myframe is None:
                       messagebox.showinfo("Error",'Camera not Working')
                       break  # skip this frame
                   facex=face_cropped(myframe)

                   if facex is not None:
                        img_id+=1
                        face = cv2.resize(facex,(200,200))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path='DATA/user.'+str(id)+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_name_path,face)

                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                        

                   # after 100 samples we stop image sampling 
                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("result",'Generating Dataset Completed')

            except Exception as e:
                messagebox.showinfo("Error", str(e))

         




if __name__=='__main__':
   root=Tk()
   obj=Student_details(root)
   root.mainloop()