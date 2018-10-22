import requests
import json
import csv

def course_id_validation(continue_prompt):
    while continue_prompt != "y":
        print("Please enter the course ID of the course you wish to cleanup")

        course_id = input("Course ID = ")

        print("Searching for your course...\n")

        chosen_course = requests.get(url + '/api/v1/courses/' + course_id,
                                     headers= {'Authorization': 'Bearer ' + token})

        chosen_course_json = json.loads(chosen_course.text)

        try:
            course_name = chosen_course_json[u'name']
        
        except KeyError:
            print ("The course ID you entered is invalid, please try again.")

        else:
            print("The course you selected is " + course_name)

            if chosen_course_json[u'workflow_state'] == u'available':
                print("Please note that the course you chose is already available to students")
        

            print("Would you like to proceed with the cleanup of this course?\n")

            continue_prompt = input("Please enter \"y\" for yes and \"n\" for no: ")

    return course_id

def delete_component (course_id,
                      token,
                      to_be_deleted,
                      ids,
                      to_be_deleted_full_json,
                      backup):

    print("Deleting " + to_be_deleted + "...")

    percent_complete = float(0)
    total_num = 0

    if to_be_deleted == "pages":
        blank_page = requests.post(url + '/api/v1/courses/' + course_id + '/pages/',
                                   headers = {'Authorization': 'Bearer ' + token},
                                   data = {'wiki_page[title]' : 'Blank Page (for FrontPage trigger)',
                                           'wiki_page[published]' : 'true',
                                           'wiki_page[front_page]' : 'true'})

    if to_be_deleted == "announcements":
        to_be_deleted_items = requests.get(url + '/api/v1/courses/' + course_id + '/discussion_topics/',
                                           headers= {'Authorization': 'Bearer ' + token},
                                           data = {'only_announcements' : 'true'})

    else:
        to_be_deleted_items = requests.get(url + '/api/v1/courses/' + course_id + '/' + to_be_deleted + '/',
                                           headers= {'Authorization': 'Bearer ' + token})

    print("Calculating how many " + to_be_deleted + " are there to be deleted...\n")

    while True:
        to_be_deleted_items_json = json.loads(to_be_deleted_items.text)
        to_be_deleted_full_json += to_be_deleted_items_json

        num = len(to_be_deleted_items_json)
        total_num += num
        
        for x in range(num):
            if to_be_deleted == "discussion_topics" or to_be_deleted == "quizzes" or to_be_deleted == "announcements":
                ids[to_be_deleted_items_json[x][u'id']] = to_be_deleted_items_json[x][u'title']
                
            elif to_be_deleted == "files":
                ids[to_be_deleted_items_json[x][u'id']] = to_be_deleted_items_json[x][u'display_name']

            elif to_be_deleted == "pages":
                ids[to_be_deleted_items_json[x][u'url']] = to_be_deleted_items_json[x][u'title']

            else:
                ids[to_be_deleted_items_json[x][u'id']] = to_be_deleted_items_json[x][u'name']
            
        if to_be_deleted_items.links['current']['url'] == to_be_deleted_items.links['last']['url']:
            json.dump(to_be_deleted_full_json,
                      backup)

            backup.close()
            break

        else:
            to_be_deleted_items = requests.get(to_be_deleted_items.links['next']['url'],
                                               headers= {'Authorization': 'Bearer ' + token})
            
    if total_num == 0:
        print("There are no " + to_be_deleted + " to be deleted\n")

    else:
        print("There are " + str(total_num) + " of " + to_be_deleted + " to be deleted")

        percent_inc = float(1 / total_num) * 100.0
    
        for x in ids.keys():
            if to_be_deleted == "announcements":
                to_be_deleted_items = requests.get(url + '/api/v1/courses/' + course_id + '/discussion_topics/',
                                           headers= {'Authorization': 'Bearer ' + token},
                                           data = {'only_announcements' : 'true'})
            else:
                to_be_deleted_items = requests.get(url + '/api/v1/courses/' + course_id + '/' + to_be_deleted + '/' + str(x),
                                                   headers= {'Authorization': 'Bearer ' + token})

            to_be_deleted_items_json = json.loads(to_be_deleted_items.text)

            if to_be_deleted == "files" or to_be_deleted == "folders":
                to_be_deleted_items = requests.delete(url + '/api/v1/' + '/' + to_be_deleted + '/' + str(x),
                                                      headers= {'Authorization': 'Bearer ' + token},
                                                      data = {'force' : 'true'})
            elif to_be_deleted == "announcements":
                to_be_deleted_items = requests.delete(url + '/api/v1/courses/' + course_id + '/discussion_topics/' + str(x),
                                                      headers= {'Authorization': 'Bearer ' + token},
                                                      data = {'only_announcements' : 'true'})
            else:
                to_be_deleted_items = requests.delete(url + '/api/v1/courses/' + course_id + '/' + to_be_deleted + '/' + str(x),
                                                      headers= {'Authorization': 'Bearer ' + token})
                
            percent_complete += percent_inc 

            print(str(int(percent_complete)) +"% Complete!")
               
    print("All " + to_be_deleted + " have now been deleted\n")

def delete_syllabus (course_id,
                     token):
    backup = open ("Canvas Course Backup: Course","w")

    course = requests.get(url + '/api/v1/courses/' + course_id,
                          headers= {'Authorization': 'Bearer ' + token})
    course_json = json.loads(course.text)

    json.dump(course_json,
              backup)
    backup.close()
        
    delete_syllabus = requests.put(url + '/api/v1/courses/' + course_id,
                                   headers= {'Authorization': 'Bearer ' + token},
                                   data = {'course[syllabus_body]': ''})

    print ("Finished deleting the Syllabus")

def reset_navigation (course_id,
                      token):
    backup = open ("Canvas Course Backup: Navigation","w")
    
    all_tabs = ['Announcements',
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
                'Chat',
                'CoursEval']

                
    course_tabs = requests.get(url + '/api/v1/courses/' + course_id + '/tabs',
                               headers= {'Authorization': 'Bearer ' + token})

    course_tabs_json = json.loads(course_tabs.text)

    json.dump(course_tabs_json,
              backup)
    backup.close()
    
    total_tabs = len(course_tabs_json)

    for x in range(total_tabs):
        ids[course_tabs_json[x][u'id']] = course_tabs_json[x][u'label']

    for x in ids.keys():
        try:       
            course_tabs = requests.put(url + '/api/v1/courses/' + course_id + '/tabs' + str(x),
                                       headers= {'Authorization': 'Bearer ' + token},
                                       data = {'position': (all_tabs.index(ids[x])+1)})
        except ValueError:
            course_tabs = requests.put(url + '/api/v1/courses/' + course_id + '/tabs' + str(x),
                                       headers= {'Authorization': 'Bearer ' + token},
                                       data = {'hidden': 'true'})

    print ("Navigation for the course has been reset\n")




url = "https://ubc.instructure.com"
continue_prompt = "n"
undo = "n"
ids = {}
to_be_deleted_full_json = []
all_tabs = []
total_num = 0
components_to_be_deleted = ['announcements',
                            'discussion_topics',
                            'quizzes',
                            'modules',
                            'assignments',
                            'assignment_groups',
                            'groups',
                            'files',
                            'folders',
                            'pages',
                            'external_tools']

with open('token', 'r') as token_file:
    token = token_file.read()
        

course_id = course_id_validation(continue_prompt)

for to_be_deleted in components_to_be_deleted:    
    backup = open ("Canvas Course Backup: " + to_be_deleted,"w")

    delete_component (course_id,
                      token,
                      to_be_deleted,
                      ids,
                      to_be_deleted_full_json,
                      backup)
    ids={}
    print ("Finished with " + to_be_deleted +"\n")

delete_syllabus (course_id,
                 token)

reset_navigation (course_id,
                  token)

requests.put(url + '/api/v1/courses/' + course_id,
             headers= {'Authorization': 'Bearer ' + token},
             data = {'offer': 'false'})

print ("Done")

