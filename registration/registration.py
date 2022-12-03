import tkinter as tk
import tkinter.ttk as ttk

root = tk. Tk()
root.geometry('500x600')
root.title('Tkinter Hub')

head_frame = tk.Frame(root)

heading_lb = tk.Label(head_frame, text='Student Registration System',
                      font=('Bold', 13),
                      bg='red')
heading_lb.pack(fill=tk.X, pady=5)

student_id_lb = tk.Label(head_frame, text='Student Id:', font=('Bold', 10))
student_id_lb.place(x=0, y=50)

student_id = tk.Entry(head_frame, font=('Bold', 10))
student_id.place(x=110, y=50, width=180)

student_name_lb = tk.Label(head_frame, text='Student name:', font=('Bold', 10))
student_name_lb.place(x=0, y=100)

student_name = tk.Entry(head_frame, font=('Bold', 10))
student_name.place(x=110, y=100, width=180)

student_email_lb = tk.Label(head_frame, text='Student email:', font=('Bold', 10))
student_email_lb.place(x=0, y=150)

student_email = tk.Entry(head_frame, font=('Bold', 10))
student_email.place(x=110, y=150, width=180)

student_courses_lb = tk.Label(head_frame, text='Student courses:', font=('Bold', 10))
student_courses_lb.place(x=0, y=200)

student_courses = tk.Entry(head_frame, font=('Bold', 10))
student_courses.place(x=110, y=200, width=180)

register_btn = tk.Button(head_frame, text='Register', font=('Bold', 12))
register_btn.place(x=0, y=250)

update_btn = tk.Button(head_frame, text='Update', font=('Bold', 12))
update_btn.place(x=85, y=250)

delete_btn = tk.Button(head_frame, text='Delete', font=('Bold', 12))
delete_btn.place(x=163, y=250)

clear_btn = tk.Button(head_frame, text='Clear', font=('Bold', 12))
clear_btn.place(x=235, y=250)


                        

head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=300)

search_bar_frame= tk.Frame(root)

search_lb = tk.Label(search_bar_frame, text='Search Student By Id:',
                     font=('Bold', 10))
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame,
                     font=('Bold', 10))
search_entry.pack(anchor=tk.W)

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)

record_frame = tk.Frame(root)

record_lb = tk.Label(record_frame, text='Select Record for Delete or Update',
                     bg='red', font=('bold', 13))
record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X, pady=5)

record_table['column'] = ['Id', 'Name', 'Email', 'Courses']

record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)

record_table.column('Id', anchor=tk.W, width=50)
record_table.column('Name', anchor=tk.W, width=100)
record_table.column('Email', anchor=tk.W, width=100)
record_table.column('Courses', anchor=tk.W, width=200)

record_table.heading('Id', text='Id', anchor=tk.W)
record_table.heading('Name', text='Name', anchor=tk.W)
record_table.heading('Email', text='Email', anchor=tk.W)
record_table.heading('Courses', text='Courses', anchor=tk.W)

record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=400, height=200)

root.mainloop()