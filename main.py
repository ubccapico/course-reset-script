from tkinter import *
from tkinter import messagebox

import traceback

import accesstoken as init
import course_reset as rst_module

from canvasapi import Canvas
from tkinter import Canvas as ui

# Create the base window for the GUI
window = Tk()
window.title("Course Reset Script")
window.geometry("400x600")
window.configure(bg = "#623593")

# Create the graphical user interface
interface = ui(window,
                bg = "#623593",
                height = 600,
                width = 400,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
interface.place(x = 0, y = 0)

# Create white box
interface.create_rectangle(
    0.0,
    275,
    400,
    600,
    fill="#FFFFFF",
    outline="")

# Add Reset Graphic
rst_icon = PhotoImage(
    file=rst_module.relative_to_assets("refresh_img.png"))
rst_icon_img = interface.create_image(
    200.0,
    128.0,
    image=rst_icon
)

# Add text
interface.create_text(
    200,
    240.0,
    justify = "center",
    text="CANVAS COURSE RESET",
    fill="#FFFFFF",
    font=("Oswald SemiBold", 25 * -1)
)

interface.create_text(
    200,
    307.0,
    justify = "center",
    text="CANVAS ACCESS TOKEN",
    fill="#623593",
    font=("Oswald SemiBold", 18 * -1)
)

# Create the background for the prompts
entry_img = PhotoImage(
    file=rst_module.relative_to_assets("entrybox.png"))
token_entry_bg = interface.create_image(
    201.0,
    346.27464294433594,
    image=entry_img
)

# Create a Access Token Field
token_entry = Entry(
    bd=0,
    bg="#E5D3F0",
    highlightthickness=0,
    show="*"
)
token_entry.place(
    x=85.77464294433594,
    y=326.0,
    width=230.45071411132812,
    height=38.549285888671875
)
# Display Access token if it exists in accesstoken.py
token_entry.insert(0, init.access_token)

"""
    Function that controls the Show Token checkbox
"""
def toggle():
    global token_entry, showPW
    if showPW.var.get():
        token_entry.config(show = "*")
    else:
        token_entry.config(show = "")

# Create Show Token checkbox
showPW = Checkbutton(window, text="Show Token", bg="#FFFFFF", onvalue=False, offvalue=True, command=toggle)
showPW.var = BooleanVar(value=True)
showPW['variable'] = showPW.var
showPW.place(
    x=145.75,
    y=373.0,
    width=108.5,
    height=27
)

interface.create_text(
    200,
    420.0,
    justify = "center",
    text="COURSE CODE",
    fill="#623593",
    font=("Oswald SemiBold", 18 * -1)
)

courseID_entry_bg = interface.create_image(
    200.0,
    458.27464294433594,
    image=entry_img
)
courseID_entry = Entry(
    bd=0,
    bg="#E5D3F0",
    highlightthickness=0
)
courseID_entry.place(
    x=84.77464294433594,
    y=438.0,
    width=230.45071411132812,
    height=38.549285888671875
)

"""
    Function that confirms that the correct course ID 
    and access token was provided
"""
def confirmation_window():
    try:
        global window
        # Record course_ids
        init.course_id = courseID_entry.get()

        # If access token is not added in the init.py file, retrieve it from Window prompt
        if token_entry.get():
            init.access_token = token_entry.get()

        API_URL = init.base_url
        API_KEY = init.access_token

        # Get Canvas course information
        canvas = Canvas(API_URL, API_KEY)
        course = canvas.get_course(init.course_id)

        global short_course_name
        short_course_name = course.id
        global course_name
        course_name = course.name
        global course_code
        course_code = course.course_code
            
    except Exception as e:
        # remove the hashtag below to see where the error occurs
        # traceback.print_exc()
        print('The Course ID or Access Token is incorrect.\n If any problem still persists, restart the program, and try again.')
        messagebox.showinfo("Error","The Course ID, Access Token, or base URL is incorrect.",icon="error")
    
    # Display confirmation window
    delete_confirmation = messagebox.askquestion(
            "Delete All Content",
            "Course Name: %s \nCourse Code: %s \nPlease note that the course you chose is currently %s to students\n\nAre you sure you want to delete ALL course content for this course?" 
            %(course_name, course_code, course.workflow_state),
            icon='warning')
    try:
        if delete_confirmation == 'yes':
            # Delete previous window
            window.destroy()

            # Delete the course contents
            rst_module.delete_course()         

    except Exception as e:
        # Remove the hashtag below to see where the error occurs
        # traceback.print_exc()
        print('Unable to proceed with course reset.\n If any problem still persists, restart the program, delete the deets file, and try again.')
        messagebox.showinfo("Error","Course Reset Unsuccessful.",icon="error")

# Create a "Submit" Button
submit_btn_img = PhotoImage(
    file=rst_module.relative_to_assets("submit_btn.png"))
submit_btn = Button(
    image=submit_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=confirmation_window
)
submit_btn.place(
    x=123.62466430664062,
    y=505.0,
    width=152.75064086914062,
    height=34.93865966796875
)

# Create a "Cancel" Button
cancel_btn_img = PhotoImage(
    file=rst_module.relative_to_assets("cancel_btn.png"))
cancel_btn = Button(
    image=cancel_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy
)
cancel_btn.place(
    x=123.65109252929688,
    y=545.0,
    width=152.69784545898438,
    height=36.40576171875
)

window.resizable(False, False)
window.mainloop()



