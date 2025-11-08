# university-chatbot-project
This project aims to create a website that contains education programs that a student can enroll into. The student will be aided by a chatbot at various stages of their time as a student and will perform different tasks depending on user input, ranging from page redirection and feedback collection to the delivery of program material via email.

# Version: Iteration 2
As of Iteration 2, our system has a variety of pages populated statically with the University's programs to which our chatbot can redirect potential students to depending on their program of interest. To reach these pages, the user has to click on No at the time of opening the chat, which is the chatbot asking the user if they are already enrolled. Clicking on Yes leads to the functionality reserved for already enrolled students which is not yet in place due to the enrollment system being an Iteration 3 feature. Iteration 3 will also see our pages migrate from Static to Dynamic.

# Run & Deployment Instructions

To run our project, a user would need to clone our repository and install Django via the pip command:

pip install django

After installing django, they’d need to position themselves on the application by navigating to ~/NextGenUniversityChatbot/uni-chatbot/ which would be the relative path where our application is located and then run the following commands:

python manage.py migrate (obtain the db schema)
python manage.py loaddata superuser.json (to recreate a superuser on the empty schema)
python manage.py runserver (to run the program on their localhost)

The relative path where the manage.py file lives should be ~/NextGenUniversityChatbot/uni-chatbot/manage.py
