## Table of Contents
[User Experience](#user-experience)
- [Project Goal](#project-goal)
    - [Users Stories](#users-stories)
    - [Designer Strategy](#designer-strategy)
    - [Design Elements](#design-elements)
    - [Wireframes](#wireframes)

- [Features](#features)
    - [Features to be implemented in the future](#features-to-be-implemented-in-the-future)

- [Technologies used](#technologies-used)
    - [Other sources used to build the project](#other-sources-used-to-build-the-project)

- [Testing](#testing)

- [Project deployment](#project-deployment)
    - [Local deployment](#local-deployment)
    - [Heroku deployment](#deploying-an-app-to-heroku)

- [Project database structure](#project-database-structure)

- [Credits](#credits) 
    - [Contents](#content)
    - [Media](#media)
    - [Inspiration and motivation](#inspiration-and-motivation)
    - [Acknowledgements](#acknowledgements)

- [Disclaimer](#disclaimer)

## User Experience

### Project Goal
The main goal for creating this website is to deliver interesting information about different type of guitars. This website 
is not only recommended for guitarists who would like to check/add/review the guitars they like, but to any website user who 
would like to gain more knowledge about this fantastic instrument. 

### User Stories
1. **Visiting User**

- as a visiting user I want to find the website easy to use and navigate
- as a visiting user I want to find the website content approachable and not overwhelming
- as a visiting user I want to access the information about the guitars easily
- as a visiting user I want to have an ability to register and log in with no obstacles
- as a visiting user I want to find information about a guitar of the month
- as a visiting user I want to be able to visit social-media sites provided by the website host

2. **Registered User**

- as a registered user I want to be log in successfully
- as a registered user I want to be able to add and delete guitar's type
- as a registered user I want to be able to add a review about the guitars
- as a registered user I want to have an option to remove my profile from the website

### Designer's Strategy
- to create a website which will be a user-friendly and easy to navigate;

- to deliver a website with easy to read, informative, concise text which will play a major role in search engine placement;

- to create a website which engages its users and continues to hold their attention when they browse through it;

- to provide a simple information accessibility and place key information in a plain manner, so the users can only locate  
 a certain bit of info i.e. register form, social-media links, etc., without perusing the entire site;

- to create a website which will be intuitive and would anticipate the users' needs;

### Design Elements
Being aware of how important it is to built a website reflects designer's idea, I decided to use *eye-catching* colours
and fonts. My goal was to mix both simplicity and elegance at the same time. I believed it would build a nice connection between 
the users and the website host.

#### Fonts
I decided to use two type of [Google Fonts](https://fonts.google.com/):

- **Dancing Script** for the titles

- **Playfair Display** for the website content 

#### Colours
I used a vivid colours pallete to create a visually positive experience for the users. The following colours 
have been applied during creation of the project:






### Wireframes
I used [SmartDraw](https://www.smartdraw.com/) software to create the wireframes. The wireframes allowed me to carefully plan what I wanted to achieve, and
what would be a final effect of the written code. 

The wireframes can be found [here](https://github.com/KrisK1978/buzzing-strings/tree/master/wireframes).

## Features

### Features to be implemented in the future

## Technologies used

### Languages

1. **HTML**

2. **CSS**

3. **JavaScript**

4. **JSON**

5. **Python**

### Other tools/libraries/platforms used to build the project

1. [GitHub](https://github.com/)

2. [MongoDB Atlas](https://www.mongodb.com/)

3. [Heroku](https://www.heroku.com/)

4. [Flask](https://flask.palletsprojects.com/en/1.1.x/)

5. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

6. [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)

7. [jQuery](https://jquery.com/)

8. [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)

9. [Materialize](https://materializecss.com/)

10. [Font Awesome](https://fontawesome.com/icons?d=gallery)

11. [Google Fonts](https://fonts.google.com/)

12. [Favicon](https://www.favicon-generator.org/)

13. [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)

14. [Am I Responsive?](http://ami.responsivedesign.is/)

15. [Find Unclosed Tags](https://www.aliciaramirez.com/closing-tags-checker/)

16. [Autoprefixer CSS](https://autoprefixer.github.io/)

17. [RandomKeygen](https://randomkeygen.com/)


## Testing
The project testing details can be found [here](https://github.com/KrisK1978/buzzing-strings/blob/master/TESTING.md).

## Project deployment 
This project was built on [GitPod](https://www.gitpod.io/). [GitHub](https://github.com/login) was used to host the repository.

Make sure you have the following tools installed to make the deployment successful:

- **PIP**
- **Python3**
- **IDE** (pick the most suitable for you)
- **MongoDB Atlas** account

### Local deployment
The following steps need to be used to clone the project from **GitHub**:

1. Follow the link to the [project-repository](https://github.com/KrisK1978/buzzing-strings).

2. Go to **Code** tab and use **Clone** to copy the URL `https://github.com/KrisK1978/buzzing-strings.git`
   from **Clone** with **HTTPs** for the repository.

3. Go to your local **IDE** and open a new command line - terminal.

4. Type in `git clone` in your terminal.

**IMPORTANT:**

Please check the instructions for operating in your virtual environment as they can vary depending on what type
operating system is being used. The **Python Documentation** can be found [here](https://docs.python.org/3/library/venv.html).

5. Create a file called `.flaskenv` and add the following items:
    -    *FLASK_APP=run.py*
    -    *FLASK_ENV=development*

6. Install the required dependencies from **requirements.txt** file using the command below:
    - `pip3 -r requirements.txt`

7. Register a new account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) 
   and create a new database called **buzzing_strings** and set up the required **Collections** for 

8. In your **IDE** create a file where you can store the following information:

    - `IP`
    - `PORT`
    - `MONGO_DBNAME`
    - `MONGO_URI`
    - `SECRET_KEY`

9. Run an application using either `python3 app.py` or `flask run` command:

### Deploying an app to Heroku 
Use the following steps to deploy [buzzing-strings]() to Heroku:

1. Create a **requirements.txt** file using the command below:

    `pip3 freeze --local > requirements.txt`

2. Create a **Procfile** file using the following command:

    `echoweb: python app.py > Procfile`

    - *make sure it is a capital P and there is no file extension added*
    - *open a Procfile file and remove a blank line as if left it can cause problems with an app*

3. Push new created files to **GitHub** repository.
4. Go to [Heroku](https://id.heroku.com/login) and create a new app for this project using **Heroku Dashboard**.
5. Remember to give your app a unique name and set up a region.
6. In **Deployment** tab go to **Deployment Method** and click on **GitHub** icon to connect an app. Type in 
   *repository name* and hit *search*. Once repository is found click **Connect**.
7. Go to **Settings** tab and open **Config Vars**. Add the following information:

    |   **Key**         |                             **Value**                                                       |
    | ----------------- | ------------------------------------------------------------------------------------------- |                        
    |       IP          |                              0.0.0.0                                                        |
    |      PORT         |                              5000                                                           |
    |   MONGO_DBNAME    |                         'database name'                                                     |
    |    MONGO_URI      | mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority|           
    |   SECRET_KEY      |                           'secret_key'                                                      |


8. Go back to **Deploy** tab and scroll down to find **Automatic Deploys**. Click on **Enable Automatic Deployment**.
9. Remember to click **Deploy Branch** as we have only one branch for this project. **Heroku** will receive the code from
   **GitHub**. When new changes are pushed to **GitHub** next time, our app content should be updated accordingly. 


## Project database structure

Using the features **MongoDB Atlas** provides, I was able to create the following collections:

1. Guitar Categories


2. Guitars 


3. Guitar review


4. Users


## Credits 

### Contents
The content of the website was written by me. 

### Media 
I used the following media platforms to complete this project:

- [Guitar Guitar](https://www.guitarguitar.co.uk/)

- [Kenny's Music](https://www.kennysmusic.co.uk/)

- [Gear4Music](www.gear4music.com)

- [Traversy Media](https://www.traversymedia.com/)

### Inspiration and motivation 
[Guitar Guitar](https://www.guitarguitar.co.uk/) and my friend Dawid, a fantastic guitarist, was my main inspration to build [buzzing-strings]() website. 
I have always considered a guitar as one the most magical instruments in music history. I had a great opportunity to 
see some fantastic guitarists in my life and was able to admire how a sound connection can be built between an instrument and a human.
My motivation was not only to highlight the fact how great this instrument is but also to give an opportunity to the website users to share
their thoughts about their favourite guitars. I was also motivated to deliver some interesting facts/information to users who never played a guitar,
but would like to gain some knowledge about this instrument. 

### Acknowledgements
This project would not be completed without a great support of my family and friends and my mentor [Simen Daehlin](https://github.com/Eventyret).
Their constructive advice delivered valid and well-reasoned opinions. It involved both positive and negative comments which helped 
me to see my project from a different perspective and amend the content to achieve the ultimate goal, a user-friendly and
interesting website. 

Also, I would like to thank my fellow [Code Institute](https://codeinstitute.net/) students and tutors who always been there for me, 
offering a friendly advice when I was having problems with sorting things out. Last but not least [Slack](https://slack.com/signin#/signin) 
community which I found extremely helpful in resolving code-related issues. 

### Disclaimer  
This website was created for educational purpose only.

[Back to top](#table-of-contents)