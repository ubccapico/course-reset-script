import requests
import json
import accesstoken as init
import webbrowser


from tkinter import *
from tkinter import ttk
from canvasapi import Canvas

from tkinter import Canvas as ui

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def delete_external_tools ():
    percent_complete = float(0)
    total_num = 0
    ids = {}
    to_be_deleted_full_json = []
    to_be_deleted_items = requests.get(init.base_url+ '/api/v1/courses/' + init.course_id + '/external_tools/',
                                           headers= {'Authorization': 'Bearer ' + init.access_token})

    while True:
        to_be_deleted_items_json = json.loads(to_be_deleted_items.text)
        to_be_deleted_full_json += to_be_deleted_items_json

        num = len(to_be_deleted_items_json)
        total_num += num
        
        for x in range(num):
            ids[to_be_deleted_items_json[x][u'id']] = to_be_deleted_items_json[x][u'name']
            
        if to_be_deleted_items.links['current']['url'] == to_be_deleted_items.links['last']['url']:
            break
        else:
            to_be_deleted_items = requests.get(to_be_deleted_items.links['next']['url'],
                                               headers= {'Authorization': 'Bearer ' + init.access_token})

    if total_num == 0:
        print("There are no external tools to be deleted\n")
    else:
        print("There are " + str(total_num) + " external tools to be deleted")
        percent_inc = float(1 / total_num) * 100.0
        for x in ids.keys():
            to_be_deleted_items = requests.get(init.base_url + '/api/v1/courses/' + init.course_id + '/external_tools/' + str(x),
                                                   headers= {'Authorization': 'Bearer ' + init.access_token})
            to_be_deleted_items_json = json.loads(to_be_deleted_items.text)
            to_be_deleted_items = requests.delete(init.base_url + '/api/v1/courses/' + init.course_id + '/external_tools/' + str(x),
                                                      headers= {'Authorization': 'Bearer ' + init.access_token})
                
            percent_complete += percent_inc 
            print("External Tools: "+str(int(percent_complete)) +"% Complete!")
               
    print("Finished with External Tools\n")
    return total_num

"""
    Function to calculate the number of items to be deleted
"""
def calculate_num(items):
    num_to_be_deleted = 0
    for item in items: 
        num_to_be_deleted += 1  
    return num_to_be_deleted
    
"""
    Function to delete Announcements
"""
def delete_announcements(course):
    percent_complete = float(0)
    all_announcements = course.get_discussion_topics(only_announcements=True)
    num_to_be_deleted = calculate_num(all_announcements)

    if num_to_be_deleted == 0:
        print("There are no announcements to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " announcements to be deleted")
        for announcement in all_announcements:
            announcement.delete()
            percent_complete +=  percent_inc
            print("Announcements: "+str(int(percent_complete)) +"% Complete!")
        
    print ("Finished with Announcements\n") 
    return num_to_be_deleted

"""
    Function to delete Discussions
"""
def delete_discussions(course):
    percent_complete = float(0)
    all_discussions = course.get_discussion_topics()
    num_to_be_deleted = calculate_num(all_discussions)

    if num_to_be_deleted == 0:
        print("There are no discussions to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " discussions to be deleted")
        for discussion in all_discussions:
            discussion.delete()
            percent_complete +=  percent_inc
            print("Discussions: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Discussions\n") 
    return num_to_be_deleted

"""
    Function to delete Course Modules
"""
def delete_modules(course):
    percent_complete = float(0)
    all_modules = course.get_modules()
    num_to_be_deleted = calculate_num(all_modules)

    if num_to_be_deleted == 0:
        print("There are no modules to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " modules to be deleted")
        for module in all_modules:
            module.delete()
            percent_complete +=  percent_inc
            print("Modules: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Modules\n") 
    return num_to_be_deleted

"""
    Function to delete Assignments and New Quizzes
"""
def delete_assignments(course):
    percent_complete = float(0)
    all_hw = course.get_assignments()
    num_to_be_deleted = calculate_num(all_hw)

    if num_to_be_deleted == 0:
        print("There are no assignments and/or new quizzes to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " assignments to be deleted")
        for hw in all_hw:
            hw.delete()
            percent_complete +=  percent_inc
            print("Assignments & New Quizzes: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Assignments and New Quizzes\n") 
    return num_to_be_deleted

"""
    Function to delete Assignment Groups
"""
def delete_assignment_groups(course):
    percent_complete = float(0)
    all_hw_groups = course.get_assignment_groups()
    num_to_be_deleted = calculate_num(all_hw_groups)

    if num_to_be_deleted == 0:
        print("There are no assignment groups to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " assignment groups to be deleted")
        for hw_group in all_hw_groups:
            hw_group.delete()
            percent_complete +=  percent_inc
            print("Assignment Groups: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Assignment Groups\n") 
    return num_to_be_deleted

"""
    Function to delete Course Files
"""
def delete_files(course):
    percent_complete = float(0)
    all_files = course.get_files()
    num_to_be_deleted = calculate_num(all_files)

    if num_to_be_deleted == 0:
        print("There are no files to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " files to be deleted")
        for file in all_files:
            file.delete()
            percent_complete +=  percent_inc
            print("Files: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Files\n") 
    return num_to_be_deleted

"""
    Function to delete Folders
"""
def delete_folders(course):
    percent_complete = float(0)
    all_folders = course.get_folders()
    num_to_be_deleted = calculate_num(all_folders)

    if num_to_be_deleted == 0:
        print("There are no folders to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted - 1) + " folders to be deleted")
        for folder in all_folders:
            # Do not delete the root folder
            if folder.parent_folder_id is None:
                percent_complete +=  percent_inc
                print("Folders: "+str(int(percent_complete)) +"% Complete!")
                num_to_be_deleted -= 1
                continue

            # Delete folders even if they are not empty
            folder.delete(force = True)
            percent_complete +=  percent_inc
            print("Folders: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Folders\n") 
    return num_to_be_deleted

"""
    Function to delete Pages
"""
def delete_pages(course):
    percent_complete = float(0)

    # Create a new blank front page
    course.create_page(
        wiki_page={
            'title':'Blank Page',
            'front_page': True,
            'published' : True
        }
    )
    all_pages = course.get_pages()
    num_to_be_deleted = calculate_num(all_pages)

    if num_to_be_deleted == 0:
        print("There are no pages to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted - 1) + " pages to be deleted")
        for page in all_pages:
            # Do not delete the new front page
            if page.front_page is True:
                percent_complete +=  percent_inc
                print("Pages: "+str(int(percent_complete)) +"% Complete!")
                num_to_be_deleted -= 1
                continue

            page.delete()
            percent_complete +=  percent_inc
            print("Pages: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Pages\n") 
    return num_to_be_deleted

"""
    Function to delete Groups
"""
def delete_groups(course):
    percent_complete = float(0)
    groupset = course.get_group_categories()
    num_to_be_deleted = calculate_num(groupset)

    if num_to_be_deleted == 0:
        print("There are no groups to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " groups to be deleted")
        for group in groupset:
            group.delete()
            percent_complete +=  percent_inc
            print("Groups: "+str(int(percent_complete)) +"% Complete!")
  
    print ("Finished with Groups\n") 
    return num_to_be_deleted

"""
    Function to delete Calendar Events
"""
def delete_calendar_events(canvas, course):
    course_context = "course_" + str(course.id)
    percent_complete = float(0)
    all_calendar_events = canvas.get_calendar_events(all_events=True,context_codes=[course_context])
    num_to_be_deleted = calculate_num(all_calendar_events)

    if num_to_be_deleted == 0:
        print("There are no calendar events to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " calendar events to be deleted")
        for cal_event in all_calendar_events:
            cal_event.delete()
            percent_complete +=  percent_inc
            print("Calendar Events: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Calendar Events\n") 
    return num_to_be_deleted

"""
    Function to delete Classic Quizzes
"""
def delete_quizzes(course):
    percent_complete = float(0)
    all_quizzes = course.get_quizzes()
    num_to_be_deleted = calculate_num(all_quizzes)

    if num_to_be_deleted == 0:
        print("There are no quizzes to be deleted.\n")
    else:
        percent_inc = float(1.0 / num_to_be_deleted) * 100.0
        print("There are " + str(num_to_be_deleted) + " classic quizzes to be deleted")
        for quiz in all_quizzes:
            quiz.delete()
            percent_complete +=  percent_inc
            print("Classic Quizzes: "+str(int(percent_complete)) +"% Complete!")

    print ("Finished with Quizzes\n") 
    return num_to_be_deleted

"""
    Function to remove Syllabus
"""
def reset_syllabus(course):
    # Display Course Summary
    course.update_settings(syllabus_course_summary = True)
    course.update(course={'syllabus_body':''})
    print ("Finished deleting Syllabus\n") 

"""
    Function to reset Course Navigation
"""
def reset_nav(course):
    all_tabs = ['Home',
               'Announcements',
               'Assignments',
               'Discussions',
               'Grades',
               'People',
               'Page',
               'Files',
               'Syllabus',
               'Outcomes',
               'Quizzes',
               'Modules',
               'My Media',
               'Media Gallery',
               'Settings']

    current_tabs= course.get_tabs()
    
    # Hide External Tools tabs
    for tab in current_tabs:
        # Check if course tab is in our list of tabs
        if tab.label not in all_tabs:
            # Disable from Course Navigation
            tab.update(hidden = True)
        else:
            if tab.label != 'Home' and tab.label != 'Settings':
                tab.update(hidden = False)
                # Arrange the tabs in the Course Navigation
                tab.update(position=all_tabs.index(tab.label)+1)

    print ("Finished resetting Course Navigation.\n") 


"""
    Function to set up Course deletion summary window
"""
def delete_course():
    global course_id
    global url 

    course_id = init.course_id
    url = init.base_url
    token = init.access_token

    # Get Course Information
    canvas = Canvas(url, token)
    course = canvas.get_course(init.course_id, include ='syllabus_body')

    # Create a new window
    progress = Tk()
    progress.title("Course Reset Script Summary")
    progress.geometry("400x600")
    progress.configure(bg = "#FFFFFF")

    # Create the graphical user interface
    interface = ui(progress,
                    bg = "#623593",
                    height = 600,
                    width = 400,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
    interface.place(x = 0, y = 0)
    interface.create_rectangle(
                    0.0,
                    131.65354919433594,
                    400.0,
                    630.7401580810547,
                    fill="#FFFFFF",
                    outline="")

    # Add Task Graphic
    complete_img = PhotoImage(
    file=relative_to_assets("complete_img.png"))
    complete_img_icon = interface.create_image(
                    61.92643737792969,
                    71.08662033081055,
                    image=complete_img)

    # Add Text
    interface.create_text(
                    92.87376403808594,
                    51.56693649291992,
                    anchor="nw",
                    text="COURSE RESET COMPLETE!",
                    fill="#FFFFFF",
                    font=("Oswald SemiBold", 24 * -1))

    interface.create_text(
                    200,
                    152.07,
                    justify = "center",
                    text="Summary of Course Reset:",
                    fill="#623593",
                    font=("Orienta Regular", 18 * -1))

    interface.create_text(
                    200,
                    172.07,
                    justify = "center",
                    text= ("%s" %course.name),
                    fill="#623593",
                    font=("Orienta Regular", 18 * -1))

    # Create a "Go to Course" Button
    course_btn_img = PhotoImage(
                    file=relative_to_assets("course_btn.png"))
    course_btn = Button(
                    image=course_btn_img,
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda: webbrowser.open_new_tab( "%s/courses/%s" %(init.base_url,init.course_id)),
                    relief="flat")
    course_btn.place(
                    x=103.82807159423828,
                    y=536.0708618164062,
                    width=192.34384155273438,
                    height=49.18896484375)

    # Create a Frame that displays the Course Reset Summary
    liFrame =ttk.Frame(progress, width=40,height=10)
    liFrame.place(
        x=30.71,
        y=189.10,
        width=338.58,
        height=326.74)

    scrollbar = ttk.Scrollbar(liFrame)
    completionList = Listbox(liFrame,width=50,height=15,yscrollcommand=scrollbar.set)
    scrollbar.configure(command=completionList.yview)
    completionList.pack (side="left")
    scrollbar.pack(side="right", fill="y")   

    """
        Function to delete course contents
    """
    def reset_course(canvas, course):
        num_deleted = 0
        progressList =[]

        for to_be_deleted in components_to_be_deleted:    
            if to_be_deleted == 'announcements':
                num_deleted = delete_announcements(course)
            elif to_be_deleted == 'discussion_topics':
                num_deleted = delete_discussions(course)
            elif to_be_deleted == 'quizzes':
                num_deleted = delete_quizzes(course)
            elif to_be_deleted == 'modules':
                num_deleted = delete_modules(course)
            elif to_be_deleted == 'assignments':
                num_deleted = delete_assignments(course)
            elif to_be_deleted == 'assignment_groups':
                num_deleted = delete_assignment_groups(course)
            elif to_be_deleted == 'files':
                num_deleted = delete_files(course)
            elif to_be_deleted == 'folders':
                num_deleted = delete_folders(course)
            elif to_be_deleted == 'pages':
                num_deleted = delete_pages(course)
            elif to_be_deleted == 'groups':
                num_deleted = delete_groups(course)
            elif to_be_deleted == 'calendar_events':
                num_deleted = delete_calendar_events(canvas, course)
            elif to_be_deleted == 'external_tools':
                num_deleted = delete_external_tools ()

            progressList.append("Finished deleting %s %s" %(num_deleted, to_be_deleted))
            completionList.insert('end',"Finished deleting %s %s" %(num_deleted, to_be_deleted))    

        # Remove Syllabus
        reset_syllabus(course)
        progressList.append("Finished deleting syllabus")
        completionList.insert('end',"Finished deleting Syllabus")  

        # Reset Course Navigation
        reset_nav(course)
        progressList.append("Finished reseting navigation")
        completionList.insert('end',"Finished reseting Course Navigation")   

        # Modify Course Settings
        course.update(course={'event':'claim',                          # Unpublish Course
                            'default_view':'syllabus',                  # Set Default View to Syllabus
                            'self_enrollment':False,                    # Disable Self-enrollment link
                            'grading_standard_enabled':False})          # Disable Course Grading Scheme

        course.update_settings(filter_speed_grader_by_student_group = False,    # Disable Launch SpeedGrader Filtered by Student Group
                                show_announcements_on_home_page = False,        # Disable Showing Announcements on Home Page
                                default_due_time = "23:59:59")                  # Set Default Due Time to 11:59:59 PM
    
    components_to_be_deleted = ['announcements',
                                'discussion_topics',
                                'quizzes',
                                'modules',
                                'assignments',
                                'assignment_groups',
                                'files',
                                'folders',
                                'calendar_events',
                                'groups',
                                'pages',
                                'external_tools']
    
    reset_course(canvas, course)

    progress.resizable(False, False)
    progress.mainloop()


