import tkinter as tk
import tkinter.font as font
from tkinter import *


#Initialize the main window
root = tk.Tk()
root.title("Log in Form")
root.resizable(False,False)
root.geometry("657x510+350+100")

#BACKGROUND IMAGE
frame_bg = tk.PhotoImage(file='imagebg.png')

#CREATE MAIN FRAME
main_frame = Frame(root, height=510,width=657)
main_frame.place(x=0,y=0)


#CREATE LOGIN FRAME
login_frame = Frame(main_frame,height=420, width=275, bg="white")
login_frame.place(x=103, y=45)

#create font style
login_font = ('Inter', 24,'bold')
email_font = ('Inter', 11)
signup_font = ('Inter', 8, 'bold')
forgot_font = ('Inter', 7, 'bold')


#Show background image 
frame_lbl_bg = Label(main_frame,image=frame_bg)
frame_lbl_bg.place(x=0,y=0)

#user login image/icon
login_image = tk.PhotoImage(file="user_icon.png")
login_image_icon = Label(
    login_frame,
    image=login_image,
    background='white'
    )
login_image_icon.place(x=98,y=25,height=65,width=65)

#Login title
login_title = Label(login_frame,text='Login', bg='white')
login_title.configure(font=login_font, fg='#7f7fcc')
login_title.place(x=85,y=85)


#Password Label
label_email1 = Label(login_frame, text= 'Email', bg='white')
label_email1.configure(font=email_font, fg='#7f7fcc')
label_email1.place(x=22,y=150)

#email entry
entry_email = Entry(login_frame, borderwidth=0,fg='#6c6c6c')
entry_email.place(x=25,y=182, width=200)


#Email label
label_pass = Label(login_frame, text='Password', bg='white')
label_pass.configure(font=email_font, fg='#7f7fcc')
label_pass.place(x=22,y=230)

#entry password
entry_password = Entry(login_frame, borderwidth=0, fg='#6c6c6c')
entry_password.place(x=25,y=262, width=170)

#entry and password line
frame_email_line = Frame(login_frame)
frame_email_line.place(x=25,y=200, width=200)
frame_password_line = Frame(login_frame)
frame_password_line.place(x=25,y=280, width=170)

#show/Hide button
button_show_image = tk.PhotoImage(file='pass_hide.png')
button_show = Button(
    login_frame,image=button_show_image, 
    borderwidth=0,
    background='white', 
    activebackground='white'
    )
button_show.place(x=200,y=250)

#login button
button_login_image = tk.PhotoImage(file='login.png')
button_login = Button(
    login_frame,
    image=button_login_image,
    background='white', 
    activebackground='white', 
    borderwidth=0
    )
button_login.place(x=85, y=300)

#not a member yet show label
label_forgot = Label(
    login_frame, 
    text='Not a member yet |',
    fg='#7f7fcc', 
    background='white'
    ).place(x=60,y=350)

#signup button
button_signup_text = Button(
    login_frame,
    command=lambda:frame_create_account.tkraise(),
    text='Sign Up', 
    fg='#7f7fcc',
    font=signup_font, 
    background='white', 
    borderwidth=0, 
    activebackground='white',
    activeforeground='#7f7fcc'
    )
button_signup_text.place(x=170, y=350)

#forgot password label
button_forgot_pass = Button(login_frame)
button_forgot_pass.configure(
    text='Forgot Password', 
    fg='#7f7fcc',
    font= forgot_font, 
    background='white', 
    borderwidth=0, 
    activebackground='white',
    activeforeground='#7f7fcc',
    command=lambda:frame_forgot_password.tkraise()
    )
button_forgot_pass.place(x=100,y=390)


#CREATE frame_create_account
frame_create_account = Frame(
    main_frame,
    height=420, 
    width=275,
    background='white'
    )
frame_create_account.place(x=103, y=45)

#display image icon - frame_create_account

login_image_icon_create = Label(
    frame_create_account,
    image=login_image,
    background='white')
login_image_icon_create.place(x=98,y=25,height=65,width=65)

#Login tile - frame_create_account
login_font = ('Inter', 18,'bold')
create_title = Label(
    frame_create_account,
    text='Create Account', 
    bg='white'
    )
create_title.configure(font=login_font, fg='#7f7fcc')
create_title.place(x=43,y=85)

#Name label - frame_create_account
name_font = ('Inter', 11)
label_name_create = Label(
    frame_create_account,
    text= 'Name',
    bg='white'
    )
label_name_create.configure(font=email_font, fg='#7f7fcc')
label_name_create.place(x=22,y=140)

#Name entry - frame_create_account
entry_name_create = Entry(
    frame_create_account, 
    borderwidth=0,
    fg='#6c6c6c'
    )
entry_name_create.place(x=30,y=170, width=200)

#Name entry line - frame_create_account
frame_name_line_create = Frame(frame_create_account)
frame_name_line_create.place(x=30,y=188, width=200)


#Email label - frame_create_account
label_email_create = Label(
    frame_create_account, 
    text= 'Email', 
    bg='white'
    )
label_email_create.configure(font=email_font, fg='#7f7fcc')
label_email_create.place(x=22,y=210)

#Email entry - frame_create_account
entry_email_create = Entry(
    frame_create_account, 
    borderwidth=0,
    fg='#6c6c6c'
    )
entry_email_create.place(x=30,y=237, width=200)

#Email Entry Line - frame_create_account
frame_email_line = Frame(frame_create_account)
frame_email_line.place(x=30,y=255, width=200)


#Password Label - frame_create_account
label_password_create = Label(
    frame_create_account, 
    text= 'Password', 
    bg='white'
    )
label_password_create.configure(font=email_font, fg='#7f7fcc')
label_password_create.place(x=22,y=280)

#Password entry - frame_create_account
entry_password_create = Entry(
    frame_create_account, 
    borderwidth=0,
    fg='#6c6c6c')
entry_password_create.place(x=30,y=307, width=200)

#Password Entry line - frame_create_account
frame_password_line = Frame(frame_create_account)
frame_password_line.place(x=30,y=325, width=170)

#show/Hide button - frame_create_account
button_show_image_create = tk.PhotoImage(file='pass_hide.png')
button_show_image_create = Button(
    frame_create_account,image=button_show_image, 
    borderwidth=0,
    background='white', 
    activebackground='white'
    )
button_show_image_create.place(x=210,y=300)

#Create account button - frame_reset_password
imagebt_create_account = tk.PhotoImage(file='create_accbtn.png')
button_create_acccount = Button(frame_create_account,
                                image=imagebt_create_account,
                                borderwidth=0,
                                activebackground='white',
                                background='white',
                                command=lambda:login_frame.tkraise()
                                )
button_create_acccount.place(x=75,y=350)


#Create signin button - frame_create_account
button_signin = Button(
    frame_create_account, 
    text='Sign In', 
    font=signup_font,
    command=lambda:login_frame.tkraise(),    
    activebackground='white',
    background='white',
    fg='#7f7fcc',
    borderwidth=0,
    activeforeground='#7f7fcc'
    )
button_signin.place(x=165, y=390)

#Create label already member - frame_create_account
label_already_account = Label(
    frame_create_account, 
    text='Already a member |',
    font='inter, 8',
    fg='#7f7fcc', 
    background='white'
    ).place(x=65,y=390)


#CREATE RESET PASSWORD FRAME -frame_reset_password

frame_reset_password = Frame(main_frame,height=420,width=275,background='white')
frame_reset_password.place(x=103,y=45)

#display login icon
login_image_icon_create = Label(
    frame_reset_password,
    image=login_image,
    background='white')
login_image_icon_create.place(x=98,y=25,height=65,width=65)

#display reset password title - frame_reset_password
login_font = ('Inter', 18,'bold')
create_reset_label = Label(
    frame_reset_password,
    text='Reset Password', 
    bg='white'
    )
create_reset_label.configure(font=login_font, fg='#7f7fcc')
create_reset_label.place(x=43,y=85)

#New Password Label - frame_reset_password
reset_new_password = Label(
    frame_reset_password, 
    text= 'New Password', 
    bg='white'
    )
reset_new_password.configure(font=email_font, fg='#7f7fcc')
reset_new_password.place(x=22,y=150)

#New Password entry - frame_create_account
entry_new_password_reset = Entry(
    frame_reset_password, 
    borderwidth=0,
    fg='#6c6c6c')
entry_new_password_reset.place(x=30,y=180, width=200)

#New Password Entry line - frame_create_account
frame_new_password_line = Frame(frame_reset_password)
frame_new_password_line.place(x=30,y=200, width=200)


#Confirm Password Label - frame_reset_password
reset_new_password = Label(
    frame_reset_password, 
    text= 'Confirm New Password', 
    bg='white'
    )
reset_new_password.configure(font=email_font, fg='#7f7fcc')
reset_new_password.place(x=22,y=220)

#Confirm New Password entry - frame_create_account
entry_confirm_password_reset = Entry(
    frame_reset_password, 
    borderwidth=0,
    fg='#6c6c6c')
entry_confirm_password_reset.place(x=30,y=250, width=170)

#Confirm New Password Entry line - frame_create_account
frame_reset_password_line = Frame(frame_reset_password)
frame_reset_password_line.place(x=30,y=268, width=170)

#Create reset button - frame_reset_password
imagebt_reset_account = tk.PhotoImage(file='change_button.png')
button_create_acccount = Button(frame_reset_password,
                                image=imagebt_reset_account,
                                borderwidth=0,
                                activebackground='white',
                                background='white',
                                command=lambda:login_frame.tkraise()
                                )
button_create_acccount.place(x=75, y=335)

#CREATE FORGOT PASSWORD FRAME - frame_forgot_password

frame_forgot_password = Frame(main_frame, height=420, width=275, background='white')
frame_forgot_password.place(x=103,y=45)

#display user icon - frame_forgot_password
login_image_icon_create = Label(
    frame_forgot_password,
    image=login_image,
    background='white')
login_image_icon_create.place(x=98,y=25,height=65,width=65)

#display reset password title - frame_forgot_password
login_font = ('Inter', 18,'bold')
create_forgot_label = Label(
    frame_forgot_password,
    text='Forgot Password',
    font='inter, 17' ,
    bg='white'
    )
create_forgot_label.configure(font=login_font, fg='#7f7fcc')
create_forgot_label.place(x=35,y=85)

#New Password Label - frame_forgot_password
forgot_password = Label(
    frame_forgot_password, 
    text= 'Enter Email Address', 
    bg='white'
    )
forgot_password.configure(font=email_font, fg='#7f7fcc')
forgot_password.place(x=65,y=160)


#Entry Enter email address - frame_forgot_account
entry_enter_email = Entry(
    frame_forgot_password, 
    borderwidth=0,
    fg='#6c6c6c')
entry_enter_email.place(x=50,y=210, width=170)

#Confirm New Password Entry line - frame_forgot_account
frame_forgot_password_line = Frame(frame_forgot_password)
frame_forgot_password_line.place(x=50,y=228, width=170)

#Create forgot button - frame_forgot_password
imagebt_forgot_account = tk.PhotoImage(file='Button.png')
button_forgot_acccount = Button(frame_forgot_password,
                                image=imagebt_forgot_account,
                                borderwidth=0,
                                activebackground='white',
                                background='white',
                                command=lambda:frame_reset_password.tkraise()
                                )
button_forgot_acccount.place(x=80, y=335)






login_frame.tkraise()
root.mainloop()




#Show and Hide password

# def hide_show_pass():
        
#         if login_passVar['show'] == '*':
#                 login_passVar.config(show='') 
#                 show_btn = Button(root,
#                         bg="white",
#                         borderwidth=0,
#                         command=hide_show_pass,
#                         activebackground='white')
#                 show_btn.place(x=302, y=290)      
#                 show_btn.config(image=show_img)

#         else:
#                 login_passVar.config(show='*')
#                 newhide_btn = Button(root,
#                         borderwidth=0,
#                         bg="white",
#                         command=hide_show_pass,
#                         activebackground='white')
#                 newhide_btn.place(x=302, y=290)
#                 newhide_btn.config(image=newhide_btn_img)


#Display ONLY of hide password icon
# hide_btn_img = tk.PhotoImage(file="C:\images\pass_hide.png")
# hide_btn = Button(root,
#         image=hide_btn_img,
#         borderwidth=0,
#         bg="white",
#         command=hide_show_pass)
# hide_btn.place(x=302, y=290)

# show_img = tk.PhotoImage(file="C:\images\pass_show.png")
# newhide_btn_img = tk.PhotoImage(file="C:\images\pass_hide.png")


