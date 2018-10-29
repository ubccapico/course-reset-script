# Canvas "Course Reset" Script

## Purpose: 
To script the "Course Reset" button already available in Canvas, without deleting the current course shell. This script deletes everything in the course you provide the script. Once the script is complete your course should be identical to a new Canvas course shell. 	

## Requirements:
- Python 3
- A Canvas API Token
- The course ID of the course you are resetting
=> for example: for https://ubc.instructure.com/courses/1326, 1326 is the course id

## How to get a Canvas API token
1. Log-in to canvas.ubc.ca
2. Click on "Account" on the left hand Global Navigation menu
3. Click on "Settings" 

![settings](https://github.com/jguarin16/screenshots/blob/master/account_settings.png)

4. Scroll to the very bottom of the page, then click on the ![new_access_token](https://github.com/jguarin16/screenshots/blob/master/access_token_button.png) button
5. Provide a purpose under the "Purpose feed", then click on "Generate Token"

![access-token-window](https://github.com/jguarin16/screenshots/blob/master/access_token_window.png)

6. Copy and Paste the token provided to you onto a secure/encrypted text file in your local machine. Once you close this window, you will not be able to access the token again, so please be careful where you save your text file.

![access-token-details](https://github.com/jguarin16/screenshots/blob/master/save_token.png)

## How to use the script:
1. Open the "token.txt" file and paste your Canvas API Token. Save the file.
2. Open the script using Python 3 IDLE
3. Run the script
4. You will be prompted to enter the course id of your course in the console of the IDLE
5. Enter "y" to continue
6. The script is complete once you see a "Done" message on the console
