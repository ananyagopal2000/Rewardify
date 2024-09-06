
# NLEvaluations

## Problem Set I - Regex

Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

**Solution:**
```bash
import json
import re

inputString = ('{"orders": [{"id":1}, {"id": 220 }, {"id":23453 }, {"id": 43}, {"id":521}], '
     '"errors":[{"code":3, "message":"[PHP Warning #2] count(): 2 Parameter must be an array or an'
     'object that implements Countable(153)"}]}')

'''
 this function checks if the input string is a valid json
'''
def checkIfFormatIsValid(json_string):
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

'''
    Regex used: \"[a-zA-Z0-9]+\":\s*([0-9]+)\s*
    Please find below the steps behind the decision for the regex and the breakdown of the regex
        1. Firstly, I am identifying the key-value pairs with value being only numbers
        2. \"[a-zA-Z0-9]+\" -> This part captures the key part of the json with alphanumeric
                            content. This includes the double quotes as well as it identifies the key
        3. : -> This part identifies the delimiter between key and value
        4. \s*([0-9]+)\s* -> This part captures the values if they are numbers. It also accounts 
                           for spaces between delimiter, value and after value
'''


if __name__ == "__main__":
    '''
        We need to check if the input string is a valid json
    '''
    if checkIfFormatIsValid(inputString):
        print("Entered the function as the JSON is valid")
        numberList = re.findall('\"[a-zA-Z0-9]+\":\s*([0-9]+)\s*', inputString)
        print(numberList)
        result = [int(i) for i in numberList]
        print(result)
    else:
        print("JSON is invalid")
```
# Problem Set 2

Rewardify is a web application that allows users to earn rewards by completing tasks, such as downloading apps, and track their progress through a user-friendly interface. The platform includes features for task management, and reward tracking.


## Features

- **User Authentication:** Secure user registration and login functionality.
- **Task Management:** Users can view available tasks, such as downloading apps, and upload screenshots as proof of task completion.
- **Points System:** Users earn points for completing tasks, which are tracked and displayed in their profiles.
- **Admin Interface:** Admins can manage the list of apps, assign tasks, and allocate points to the users.
- **Drag-and-Drop Upload:** Users can easily upload screenshots of completed tasks using a drag-and-drop interface.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript 
- **Database:** SQLite
- **APIs:** RESTful APIs for handling user authentication, task management, and point allocation.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ananyagopal2000/Rewardify
   cd rewardify
   ```
   
2. **Set up virtual environment:**
```bash
   python -m venv venv
source venv/bin/activate
```
3. **Apply migrations:**
```bash
   python manage.py migrate
```
4. *Run the development server:**
```bash
   python manage.py runserver
```
Access the application:

Open your web browser and navigate to http://localhost:8000

## Usage

**User Interface**

Signup/Login: Users can register for an account or log in using their credentials.

View Tasks: After logging in, users can view available tasks on the main page

Upload Screenshots: Users can upload screenshots of completed tasks via the drag-and-drop feature for a particular app.

Profile: Users can view their profile, which displays their earned points and completed tasks.

**Admin Interface**

Manage Apps: Admins can add new apps, specify download links, and assign points for task completion.

**API Endpoints**

Authentication:

POST /login/ - User login

POST /signup/ - User signup

Tasks:

GET /main_page/ - View list of tasks in the main page

POST /main_page/upload_screenshot/ - Upload a screenshot for a task

Admin:

POST /add_app/ - Add a new app

# Problem Set 3

A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

B. In what circumstances would you use Flask instead of Django and vice versa? 

**Solution:**

y choice would be to use Celery for the periodic tasks. Celery is a distributed system with a queue to perform tasks asynchronously. It can also be used to run scheduled periodic tasks. There’s a component called Celery Beat within the Celery system responsible for scheduling the tasks. The flow is as follows:

    1. Celery beat schedules the tasks

	2. Celery then sends the scheduled tasks to the queue

	3. There are workers which pickup the tasks from the queue and run the task. The workers are responsible for running the tasks.

I chose it because of the following reasons:

The schedule is easily defined using the crontab in Celery
There are ways to signal / notify when the job has completed successfully or failed.
The system is distributed by using a queue and set of workers consuming from the queue. We can send a lot of tasks to the queue and it is picked asynchronously. Since we can increase / decrease the number of workers, the system will scale.  
Even though the system will make sure to run the task with an available worker and we can also add an enhancement to retry the task on failure, it is not completely reliable because if the celery beat process stops, then the tasks will not be scheduled. 


When the scale increases, the above system can handle it. However, the following steps could be followed in production.


We can increase the number of workers used in celery
If there are a lot of cron jobs, then it would be difficult to get a visibility on how the tasks are performing. To get a more detailed visibility, we could use Airflow which is a task scheduler with a UI or Google Cloud Scheduler.
We can also increase the number of queues or the queue size in production to handle the scale.
To improve reliability, we can increase the size of the scheduler (Celery beat) to handle high number of jobs in production. In order to make sure to handle scheduler failures, we need to have another machine running the scheduler as a backup.

Flask vs Django:

Different types of databases can be integrated to Flask as compared to Django which supports the relational database management systems integration.
Since Django comes with ready to use functionalities like user authentication, content administration, site maps and other middlewares etc. , if we want to develop a project with the above functionalities, we can use Django instead of Flask
When we are working with complex applications which require optimized database handling, asynchronous processing, caching and other middlewares, we would prefer Django as it already contains the above features as opposed to Flask which is lightweight without many libraries / packages integrated within the framework.
When designing a simple application or an application which needs to be developed with some custom database choices, specific libraries/packages, then Flask is a better choice as the developer has more flexibility.
Django is based on Model-View-Controller (MVC) framework with a strict structure whereas Flask is not designed based on that. If we want the application to be structured based on MVC, we can use Django. If we want to have a customized structure, then we would use Flask







