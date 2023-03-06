# Covid19_appointments



## Statement

#### *Description:*
*Build a system that allows a user to request a covid-19 vaccination appointment, receive its confirmation and validate it at the day of the vaccination.*

#### *Considerations:*
*You can code using your preferred languages, infrastructure, etc.*
*We will take into consideration your thoughts (not necessarily coded) in your solution for the following components:*
- *Front-end server*
- *Back-end server*
- *API interface*
- *Data persistence*
- *Security*
- *Code quality*
- *Scalability*

#### *Follow-up Instructions:*
- *Upload your solution into a code repository (github, gitlab, bitbucket, etc.)*
- *Send us the repository link where you coded the exercise.*
- *Expect to explain your exercise solution and perform a demo.*




## Solution
- **Front-end server:**  Html and CSS
- **Back-end server, API interface:** Python, Django, SQLite3, GitHub and Heroku
- **Data persistence:** The database in Heroku keeps the data even after the app is closed. A good ***follow up*** from the data persistance consideration would be:
  - add some recurrent backup, this could be done maybe through Github Actions, the most correct would be to have our own DB's but the fastest solution I can think of would be to paste the DBs data it into a spreadsheet using gsheet.action maybe?
- **Security:** Django authentification and we don't let people acces to other users appointments. Good ***follow ups*** from the security consideration would be:
  - instead than redirecting when entering another user appintment list, just don't let them see their info.
  - add HTTP end to end encryption, a way to do this would be with Heroku payment plans for example.
- **Code quality:** I followed best practices when writting the code, following a common Django file structure, good ***follow ups*** from the code quality perspective would be to:
  - comment more the code if I had more time.
  - search for better Github Action test for our CI/CD of the project.
  - build the project in Docker containers instead than in a venv for when you need to modify and try it locally.
- **Scalability:** Django and Heroku are totally scalable, and the code I wrote too since, I used for loops for the elements of the web. Good ***follow ups*** would be to:
  - maybe order the list in some way acording to DBs indexes, to reduce O() notation complexity for the elements search and paste into the web
  - if someone has too many appointments make it jump to a second, third page, or maybe delete old ones...
