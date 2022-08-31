# Canvas Course Reset Script
 
This script will delete the contents of a course without deleting the course shell. This updated script also features a graphical user interface that will make it easier for users to interact with the script. 

## User Interface Design
<p align="left">
<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/main-window.png" alt="Start Window" width="270"/>
<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/progress-terminal.png" alt="Progress Window" width="390"/>
<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/completion-window.png" alt="Summary Window" width="330"/>
</p>


## Getting Started

### Requirements:
- Python 3.9 or later - can be downloaded from [here](https://www.python.org/getit/)

> Please ensure that the **Add Python 3.X to PATH**	checkbox is checked

- [Canvas API Token](https://learninganalytics.ubc.ca/for-students/canvas-api/)
- The course ID of the course you are resetting
> Ex. For https://canvas.ubc.ca/courses/1326, 1326 is the Course ID

### How to get a Canvas API token
1. Log in to [Canvas](https://canvas.ubc.ca).
2. Click on **Account** on the Global Navigation menu.
3. Select **Settings**. 

<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/canvas_settings.png" alt="Steps 2 and 3 on how to get a Canvas API token" width="250"/>

4. Under the **Approved Integrations** section, click on the **+ New Access Token** button.

<img src="https://github.com/jguarin16/screenshots/blob/master/access_token_button.png" alt="New Access Token button" width="150"/>

5. In the pop-up window, fill in the **Purpose** field.
6. Click on the **Generate Token** button. 

<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/access_token.png" alt="Steps 5 and 6 on how to get a Canvas API token" width="275"/>

7. Copy and paste the token provided to you onto a secure text file on your local machine. 

<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/token_details.png" alt="Access Token Details" width="350"/>

> Note: Once you close this window, you will not be able to access this token again. Therefore, a new token will need to be generated if you lose your current one.

### Setting up the environment:
1. Clone the [repository](https://github.com/ubccapico/course-reset-script/archive/refs/heads/master.zip) into your local computer.
2. Install the libraries needed by running a pip install in the terminal.

```
pip install -r requirements.txt
```

## Running the Python Script:
1. Open the [`accesstoken.py`](https://github.com/ubccapico/course-reset-script/blob/with-gui/accesstoken.py) file using Notepad or Visual Studio Code. 
2. Copy and paste your Canvas API Token in the `access_token` field. Then, save the file.
3. Right-click on the [`main.py`](https://github.com/ubccapico/course-reset-script/blob/with-gui/main.py) script and select **Edit with IDLE** > **Edit with IDLE 3.10**.

<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/edit_with_IDLE.png" alt="Step 3 on how to Run the Python Script" width="350"/>

4. Click **Run** > **Run Module**.

<img src="https://github.com/ckpaz12/readme-images/blob/main/artsisit/run_module.png" alt="Step 4 on how to Run the Python Script" width="200"/>

5. Fill in the prompts in the application window and click **Submit** to proceed with the course reset.
6. Once the script has finished running, a pop-up window will show a summary of what has been deleted. There is also a **Go to Course** button that will redirect you to the Canvas course page so that you may review the course.
