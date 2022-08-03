# Canvas Course Reset Script
 
This script will delete the contents of a course without deleting the course shell. This updated script now features a new graphical user interface that will make it easier for users to interact with the script. 

## User Interface Design

## Getting Started

### Requirements:
- Python 3.9 or later - can be downloaded from [here](https://www.python.org/getit/)
- [Canvas API Token](https://learninganalytics.ubc.ca/for-students/canvas-api/)
- The course ID of the course you are resetting
> Ex. For https://canvas.ubc.ca/courses/1326, 1326 is the Course ID

### How to get a Canvas API token
1. Log in to [Canvas](https://canvas.ubc.ca).
2. Click on **Account** on the left hand Global Navigation menu.
3. Click on **Settings**. 

![settings](https://github.com/jguarin16/screenshots/blob/master/account_settings.png)

4. Scroll to the very bottom of the page, then click on the **+ New Access Token** button

![new_access_token](https://github.com/jguarin16/screenshots/blob/master/access_token_button.png)

5. Provide a purpose under the **Purpose** field, then click on the **Generate Token** button. 

![access-token-window](https://github.com/jguarin16/screenshots/blob/master/access_token_window.png)

6. Copy and paste the token provided to you onto a secure/encrypted text file in your local machine. Once you close this window, you will not be able to access the token again, so please remember where you save your token.

![access-token-details](https://github.com/jguarin16/screenshots/blob/master/save_token.png)

## Running the Python Script:
1. Clone the repository into your local computer.
2. Open the [`accesstoken.py`](https://github.com/ubccapico/course-reset-script/blob/with-gui/accesstoken.py) file using Notepad or Visual Studio Code and paste your Canvas API Token in the `access_token` field. Save the file.
3. Right-click on the [`main.py`](https://github.com/ubccapico/course-reset-script/blob/with-gui/main.py) script and select **Edit with IDLE** > **Edit with IDLE 3.10**.
4. Select **Run** > **Run Module**.
5. Fill in the prompts in the application window to proceed with the course reset.
6. Once the script has finished running, a pop-up window will show a summary of what has been deleted. There is also a **Go to Course** button that will redirect you to the Canvas course page so that you may review the course.
