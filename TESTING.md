## Project Testing

Testing is a very important tool and has a lot of benefits in terms of achieving a successfull final effect. 
Having testing in my project helped to find the errors I made while building the website. 
I was aware that I had to come up with a simple but effective testing plan. I decided that each line of 
my code had to be carefully scrutinised to make sure all was working properly. 
Using [Balsamiq](https://balsamiq.com/) I created the wireframes which allowed me deliver a clear outcome by conducting 
a number of tests using website selected features. I also used the popular validation tools to make 
sure the created content had no major defects: 

1. [Markup Validation Service](https://validator.w3.org/) - to validate HTML

2. [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - to validate CSS

3. [PEP8](http://pep8online.com/) - to validate Python code

4. [JSHint](https://jshint.com/) - to validate JavaScript/jQuery


### Features Testing

#### 1. About Us... Page

**1.1 Test type:** Check the buttons functionality available for the user.
        Do they redirect the user to specific website sections as initially designed?

**Result:** Positive. All buttons working properly and redirect the user as 
            planned (Sign Up/Log In/Guitar Guitar shop, etc.).


#### 2. Log In Page

**2.1 Test type:** Submit an empty login form. Does the error message pop up 
        informing to fill in all requested fields?

**Result:** Positive. Short message appears reminding the user to fill in
            each field. 

**2.2 Test type:** Fill in the username and password fields using wrong username
        or password. Does the system come up with a warning message?

**Result:** Positive. Message appears on screen informing the user a wrong username 
            and/or Password was incorrect. 


#### 3. Sign Up! Page

**3.1 Test type:** Fill in the form leaving one of the fields blank and try submit the request.
        Does the system remind the user not to leave the form with blank fields?
    
**Result:** Positive. Message appears to remind the user that no field can be left blank.

**3.2 Test type:** Click on Log In link. Does it redirect the user to Log In page?

**Result:** Positive. Once the link is clicked it redirects the user to Log In page. 


#### 4. All Guitars

**4.1 Test type:** Use the link provided to add a guitar if the the guitar list does not 
        display any guitars. Does the link redirect the user to correct place?

**Result:** Positive. Once the user clicks on the link it redirects to Add Guitar page. 

**4.2 Test type:** View the guitars list. Can the user view and check the guitars displayed on
        the page?
    
**Result:** Positive. The user can view the added guitars. 


#### 4. Log Out Page

**5.1 Test type:** Click on Log Out icon placed either in top navbar or mobile sidenav. Does the user
    log out successfully?

**Result:** Positive. The user can log out using log out icon. 


#### 6. Add Guitar!/All Guitars Page

`C in CRUD - Creating`

**6.1 Test type:** The logged in/registered user can use Add Guitar! option in the navbar/sidenav.
    Does the Add Guitar! page render correctly? 

**Result:** Positive. The page renders correctly. The user can see Add Guitar form.

**6.2 Test type:** The user submits an empty form. Does the system come back with an error?

**Result:** Positive. The user sees a reminder no field can be left blank. 

**6.3 Test type:** The user completes all required fields in the form and hits Add Your Guitar button.
        Does the user submit the form successfully?

**Result:** Positive. The form is successfully submitted. 


`R in CRUD - Reading/Viewing`

**6.4 Test type:** The user clicks on guitar card. Does the image upload correctly (using url)?

**Result:** Positive. The image uploads the way it should. Other details about the added guitar display too.


`U in CRUD - Updating`

**6.5 Test type:** The edit button is clicked by the user. Does the edit option appear in the correct way?

**Result:** Positive. The user can edit the info on the guitar card. 

**6.6 Test type:** The user clicks on save button. Does the user record the changes by clicking the save button?

**Result:** Positive. The changes are saved successfully and displayed correctly in the updated guitar card. 


`D in CRUD - Delete`

**6.7 Test type:** The user clicks on delete button in All Guitars page. Does the delete button remove the guitar
    information card completely?
    
**Result:** Positive. The guitar card is removed. 


#### 7. Error Page

**7.1 Test type:** User typed the wrong url name. Does the error message appear?

**Result:** Positive. The error page appears.

**7.2 Test type:** User clicks on Back to Homepage button. Does the button action redirect the user to homepage (About Us...)?

**Result:** Positive. The user is redirected to About Us... page (homepage).

### Bugs 

While testing the project I found an issue/bug related to content overflow. I managed to debug this issue using 
a really handy tool called [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB).
I also experienced a tiny issue with images added to the website. I managed to resolve that by adding a class called img-responsive and declaring a proper
CSS property value.

### Additional testing: 

I kindly asked my family and friends to have a go and test my website. I was advised a user's list of favourite guitars could be added in the future, so each 
user would have own list. This idea was included in **Features to be implemented in the future** in [README.md](https://github.com/KrisK1978/buzzing-strings/blob/master/README.md) file.  
