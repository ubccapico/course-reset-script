# Canvas "Course Reset" Script

## Purpose: 
To script the "Course Reset" button already available in Canvas, without deleting the current course shell. This script deletes everything in the course you provide the script. Once the script is complete your course should be identical to a new Canvas course shell. 	

## Requirements:
- Python 3
- A Canvas API Token
- The course ID of the course you are resetting
=> for example: for https://canvas.ubc.ca/courses/1326, 1326 is the course id

## How to get a Canvas API token
1. Log-in to https://canvas.ubc.ca.
2. Click on **Account** on the left hand Global Navigation menu.
3. Click on **Settings**. 

![settings](https://github.com/jguarin16/screenshots/blob/master/account_settings.png)

4. Scroll to the very bottom of the page, then click on the **+ New Access Token** button

![new_access_token](https://github.com/jguarin16/screenshots/blob/master/access_token_button.png)

5. Provide a purpose under the **Purpose feed**, then click on the **Generate Token** icon. 

![access-token-window](https://github.com/jguarin16/screenshots/blob/master/access_token_window.png)

6. Copy and Paste the token provided to you onto a secure/encrypted text file in your local machine. Once you close this window, you will not be able to access the token again, so please be careful where you save your text file.

![access-token-details](https://github.com/jguarin16/screenshots/blob/master/save_token.png)

## How to use the script:
1. Open the "accesstoken.py" file using Notepad and paste your Canvas API Token in the **access_token** field. Save the file.
2. Right-click on the main.py script and select **Edit with IDLE** > **Edit with IDLE 3.10**.
3. Select **Run** > **Run Module**.
4. Fill in the prompts in the application window to proceed with the course reset.
5. Once the script has finished running, a pop-up window will show a summary of what has been deleted. There is also a **Go to Course** button that will redirect you to the Canvas course page so that you may review the course.
