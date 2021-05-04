<h1 align="center">nft.</h1> 

![Mockups](https://github.com/rudberga/CI-MS4-nft/blob/master/static/img/mockups.png?raw=true)

<p align="center"><strong>Milestone 4 project - Full Stack Web Developer course - Code Institute</strong></p>

<p align="center">This website is developed for users who are looking for a platform where they can buy digital art pieces as an NFT.</p>

[Link to deployed website!](https://rudberga-nft.herokuapp.com/)
 
## UX

### User Stories

These are the user stories I have focused on solving.

As a new visitor:

> *- "I expect to find a layout which is user friendly, so I easily can navigate throughout the website"*
> 
> *- "I expect to find an about page, so I can get a summarized information about the website"*
> 
> *- "I expect to find a FAQ page, so I can get an answer to the most common questions about the website"*
> 
> *- "I expect to be able to open the website on any device, so that I will be able to read it on any screen size"*
> 
> *- "I expect to be able to find where to register an account, so that I will be able to take advantage of benefits"*

As a shopper:

> *- "I expect to find a page with all pieces, so I can get an overview over what is for sale"*
> 
> *- "I expect to be able to search pieces, so I can find what I want and buy it"*
> 
> *- "I expect to be able to sort pieces by category, so I can find what to buy"*
> 
> *- "I expect to be able to see a image of each piece, so I can find what to buy and see what piece interests me"*
> 
> *- "I expect to be able to sort all of the pieces, so I can find pieces that fits my criterias"*
> 
> *- "I expect to be able to see summarized information (price, artist etc.) about the piece without having to go into details page, so I can quickly see if the piece interests me"*
> 
> *- "I expect to be able to see larger image when I click on the piece , so I can make a decision if I like it or not"*
> 
> *- "I expect to be able to see the cart updating as I add items, so I can easily see the total and what I have in my cart without going to the cart page"*
> 
> *- "I expect to be able to see a summarized shopping cart page, so I can remove or update amount of the piece I want to buy"*
> 
> *- "I expect to be able to see all information and grand total on checkout page, so I can get a simple overview over what I need to pay"*
> 
> *- "I expect to be able to pay with credit card in a secure way, so I can feel safe when I go through with the purchase"*
> 
> *- "I expect to be able to see a order summary after order is done, so I can double check that everything is correct"*

As a registered user:

> *- "I expect to be able to leave comments on each piece, so I can see what other users think and share my own thoughts"*
> 
> *- "I expect to be able to save my address information, so I can receive the proof of purchase that the store sends to your home"*
> 
> *- "I expect to be able to add my favorite pieces to my profile, so I can save them for when I want to purchase them"*
> 
> *- "I expect to be able to see my order history, so I can go back and check the information whenever I need"*

As an admin:

> *- "I expect to be able to edit, add, update and remove pieces in the store, so I can manage the pieces directly on the website"*
> 
> *- "I expect to be able to edit, add, update and remove other data in the admin panel, so I can manage this data in a easy to understand environment"*

### Strategy

The main goal of this e-commerce website is to be a place where people who wants to buy digital art, will be able to do it. The users will also be able to comment what they think about different pieces and therefore it will create a sort of community feeling. Users will be able to add their favorite pieces to their profile if they want to save something for later.

Project goals: 

- Design a website which do not take away from the art pieces themselves, should be very simple with minimal approach
- Present an easy and smooth experience for users to buy digital art pieces, from finding a piece until paying for it
- Present a way for users to comment on and add pieces as their favorites, creating a sort of community feeling
- Give the user a simple way of registering, logging in and logging out

### Scope

The features of this website will let the users:

- Search for pieces in the search bar they would be interested in buying
- Register an user account to make the shopping experience more smooth
- Add favourites to your own user profile
- Comment on pieces in order to share opinions and read other comments
- Smoothly and safely purchase their piece with credit card
- Filter pieces based on categories
- Sort pieces based on price, name or category
- Have the detailed order history saved on the profile page
- Save user details on user profile page which will be automatically filled in when checking out

### Structure

The design and layout on this website will be very minimal with very little color and mostly black and white. The reason for this is because we do not want to take away from the digital art by putting too much focus on the websites own design. It will look modern, clean and inviting in combination with the different art pieces.

### Skeleton

[Wireframe](https://github.com/rudberga/CI-MS4-nft/blob/master/static/docs/ci-ms4-nft.pdf)

8 pages included in the wireframe which are:
- Landing page
- Marketplace page
- Product page
- Shopping cart page
- Checkout page
- About page
- FAQ page
- Profile page

### Surface

#### Main inspiration
 
I took my main inspiration for the design of this website from how art galleries usually looks. The approach is very often less is more and that really works in this e-commerce website. I focused very much on black and white as well as using horizontal lines to create borders and lines to make divisions in the page. The way that the website comes alive is through the different art pieces on the website, therefore creating a "gallery-like" feeling.

#### Fonts

I have used one font in this project but I played with strong, italic and regular to make it read differently.

#### Rubik

This font has a sort of playful future looks to it and I believe it fits my website as it does not look stiff and fits the digital art image.

![RUBIK](https://github.com/rudberga/CI-MS4-nft/blob/master/static/img/rubik_font.png?raw=true)

#### Emojis

I have chosen to implement a couple of emojis in this project to make it pop. As I am approaching the design in a very minimalistic matter, I believe it adds that extra feeling of fun to it when you browse the different pages.

:v: :smiley: :wave: :star2: :hushed: :chart_with_upwards_trend: :lock_with_ink_pen:

#### Colors

The color theme is solely focused on black, white and grey. The reason for this is, as written above, I do not wanna take away from the art pieces.

I have therefore focused on below palette

![Color palette](https://github.com/rudberga/CI-MS4-nft/blob/master/static/img/color_palette.png?raw=true)

## Features

 
### Existing Features

- **User account**: user can create account where they see order history, favourites and personal info
- **Marketplace**: page where all the pieces are collected
- **Search bar**: search bar where users are able to search for pieces they want to buy
- **Filtering**: ability to filter on the marketplace by price, name or category
- **Category**: ability to view pieces by category on the marketplace
- **Order History**: users can see their order history on their profile
- **Commenting**: users can comment on pieces on the marketplace
- **Favourite list**: ability to add pieces to own favourite list which shows on your profile
- **Secure payment**: pay securely with credit card through Stripe 
- **Shopping cart**: where users can see what they added and adjust amount or remove
- **Newsletter**: visitors can sign up to a newsletter 
- **Social links**: in the footer you will find the icons for Inspiry's different social platforms

### Features Left to Implement

- **My collection**: page under user profile where your own collection is displayed
- **Rating system**: where users can rate each piece
- **For sale**: users add their own pieces for sale
- **Forum**: to open up the community part of the website

## Technologies Used 

**Languages** 

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - Markup language

- [CSS](https://en.wikipedia.org/wiki/CSS)
    - Main programming language
    
- [Python](https://www.python.org/)
    - Main programming language
    
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - Main programming language
    
**Database**

- [PostgreSQL](https://www.postgresql.org/)
    - Database used in deployment

- [SQLite3](https://www.sqlite.org/index.html)
    - Database used in development

- [AWS S3](https://aws.amazon.com/)
    - Database used in deployment for static and media files

**Frameworks**

- [Django](https://www.djangoproject.com/)
    - Framework used with python to create the whole application

- [Bootstrap](https://getbootstrap.com/)
    - Framework used in order to improve the structure and design of the website. Imported via CDN

- [jQuery](https://jquery.com/)
    - Framework used with JavaScript in order to simplify the code. Imported via CDN

**Version control**

- [GitHub](https://github.com/)
    - Used for version control of the project
    
**Cloud platform**

- [Heroku](https://heroku.com/)
    - Used for deploying and running application

**Other**

- [Gitpod](https://gitpod.io/)
   - IDE which was used for the project. Directly linked to repository through GitHub

- [Google Fonts](https://fonts.google.com/)
   - Used for all the fonts in the project. Connected to CSS via @import
   
- [Font Awesome](https://fontawesome.com/)
   - Used for all the icons in the project. Connected to HTML via CDN

- [Unsplash](https://unsplash.com/)
   - Used for images in the project. Imported locally through assets/img

- [Stripe](https://stripe.com/)
   - Used for payments in the application

- [Balsamiq](https://balsamiq.com/)
   - Used for creating wireframes for the project
   

## Testing 

I have done a lot of testing throughout the project and below you will find it in a more structured manner. I have made sure that the user stories are tested and works well, also focused on responsiveness where I have used resources online as well as the physical devices I had access to. Whenever a new functionality of the site was implemented, I tested it. At the end of the development journey, I had a big testing day where I went through the sites full functionality again.

### Tests done in order to secure UI components
(Forms are not incluced in the table as they have a separate section below)

| Test | Objective/Expected | Method | Result |
| ---- | ------ | -------- | ------ |
| General Testing | ------ | -------- | ------ |
| 1. Navigation | Verify that the user is able to navigate through all the navbar links | Opened up website and tested to click on the different navbar links | PASS |
| 2. Navigation | Verify that the user is able to navigate through all the products across the different categories | Opened up marketplace and tested to click on the different categories | PASS |
| 3. Links and Banners | Verify that all the links and banners throughout the website are redirecting to correct pages and none of the links are broken. | By opening all the pages on the website and test to click all links and banners | PASS |
| 4. Company logo | Verify that the company logo is clearly visible | Check if visible on all the pages | PASS |
| 5. Text visibility | Verify that all the text on website are clearly visible | Opening every page on website and going through all text | PASS |
| 6. Explore button | Verify that the explore button on the home page takes you to the marketplace | By clicking on the explore button | PASS |
| Filters - Marketplace | ------ | -------- | ------ |
| 1. "Sort by" button | Verify that Sort by filtering dropdown button correctly responds when used | By clicking and switching sort by on marketplace page | PASS |
| 2. "Sort by" button low to high  | Verify that Sort by filtering functionality correctly filters products based on the Price low to high and high to low | Applying sort by filter on the marketplace page | PASS |
| 3. "Sort by" button A to Z | Verify that Sort by filtering functionality correctly filters products based on the name A-Z and Z-A | Applying sort by filter on the marketplace page | PASS |
| 4. "Sort by" button category | Verify that Sort by filtering functionality correctly filters products based on the category A-Z and Z-A | Applying sort by filter on the marketplace page | PASS |
| 5. Number of items  | Verify that piece count remains intact irrespective of sorting option applied | Applying sort by filter on the marketplace page and counting the items | PASS |
| Search bar | ------ | -------- | ------ |
| 1. Search | Verify search bars result | By trying different search terms such as name and category | PASS |
| 2. Search | Verify results are all pieces matching search term | By comparing all pieces with the search term and the result it gives | PASS |
| Purchase flow | ------ | -------- | ------ |
| 1. Add to cart | Verify that the user can add to cart with one or more pieces | By adding the pieces to the cart | PASS |
| 2. Add to cart | Verify that the user cannot add more than the max amount of the piece, should cause an error | Adding 100 items of a piece | PASS |
| 3. Cart toast | Verify that the toast that pops up when piece added to cart is showing correct info | By adding different pieces with different amounts to the cart | PASS |
| 4. Cart toast | Verify that the checkout button inside the toast leads to the shopping cart page | By clicking the checkout button after adding pieces | PASS |
| 5. Shopping cart | Verify that all pieces that were added from marketplace stays in shopping cart when pressing checkout | By clicking the checkout button after adding pieces and controlling the shopping cart page | PASS |
| 6. Shopping cart | Verify that the user can delete a piece completely or update quantity by pressing the two buttons | Updated quantity and pressed update, then pressed delete button | PASS |
| 7. Shopping cart | Verify that the correct total amount always appear and updates if you update quantity | By adding different amounts to shopping cart and changing quantity within shopping cart | PASS |
| 8. Shopping cart | Verify that the checkout button leads to checkout page with all correct pieces still in the cart | By pressing checkout button inside shopping cart and check pieces | PASS |
| 9. Checkout | Verify that the order summary shows correct pieces and correct grand total | By comparing pieces in shopping cart when proceeding over to checkout with order summary and its total amount | PASS |
| 10. Checkout | Verify that payment goes through correctly and order confirmation page generates when using Stripes test card | By adding all info correctly in form and adding Stripe test card number then press complete order | PASS |
| 11. Checkout | Verify that order goes through if payment is accepted, even if website do not load correctly | By removing the form function in JS code to and check admin if the order is stored in DB and order email is sent | PASS |
| 12. Checkout | Verify that the order confirmation is sent and that the information on order confirmation page is correct | By making multiple purchases with different e-mails and pieces, also as logged in and logget out | PASS |
| Sign up | ------ | -------- | ------ |
| 1. Sign up buttons | Verify that clicking cancels/reset button after entering all the required fields, cancels the submit request, and reset all the fields | Clicking on back to login button | PASS |
| 2. Sign up link | Verify that sign up link in navbar leads to sign up form | By clicking the sign up link | PASS |
| Sign in | ------ | -------- | ------ |
| 1. Sign in button | Verify that button initiates sign in after filling out form correctly | By filling in correct info and click log in | PASS |
| 2. Sign in link | Verify that link to forgot password takes user to forgot password page | By clicking the link in the sign in form | PASS |
| Log out | ------ | -------- | ------ |
| 1. Button | Verify that it works to log out via the log out button | By clicking log out when logged in | PASS |
| Logged in user functionalities | ------ | -------- | ------ |
| 1. Favourite list | Verify that users can add products to the favourite list which appear on profile | By pressing heart icon on piece and checking account page | PASS |
| 2. Favourite list | Verify that users can remove products from the favourite list both on the piece itself | By pressing broken heart icon, but also remove directly from account page | PASS |
| 4. Comments | Verify that a logged in user can see and create own comments on piece detail page | By logging in and trying to submit a comment | PASS |
| Logged out user functionalities | ------ | -------- | ------ |
| 1. Comments | Verify that a user who is not logged in cannot create comments | By checking a piece detail page without being logged in | PASS |
| 2. Favourite list | Verify that a user who is not logged in cannot add favourites | By checking a piece detail page without being logged in | PASS |
| Profile | ------ | -------- | ------ |
| 1. Favourites | Verify that favourites are showing on the account page which was added | By clicking on favourite icon on piece detail page and checking account page | PASS |
| 2. Favourites | Verify that it is possible to remove favourite directly | By clicking "x" next to a favourite in account page | PASS |
| 3. Favourites | Verify that the name of the piece is a link which leads to the specific piece | By clicking the name of piece in favourite link | PASS |
| 4. Order history | Verify that order history is correctly saved in account and shows correct information about the order | By clicking on link for order number and comparing information with the actual purchase | PASS |
| 5. Account info | Verify that it is possible to update account information and it shows up on checkout page | By updating account info and check info on checkout page | PASS |
| FAQ | ------ | -------- | PASS |
| 1. FAQ page | Verify that the about page is working fine and displays text correctly | By entering the FAQ page | PASS |
| About | ------ | -------- | ------ |
| 1. About page | Verify that the about page is working fine and displays text correctly | By entering the about page | PASS |
| Social links | ------ | -------- | ------ |
| 1. Links | Verify that the social links opens up a new tab to the correct social media platform | By clicking the different icons in the footer | PASS |


### Tests done in order to secure structural integrity

#### Modals

Planned to implement modal for each authorization step but manage to finish sign up so far. The modal was tested on several screen sizes and confirmed that it kept its responsive design.

This includes the modal for:

- Log in

#### Fonts

Fonts are consistent throughout the website, this was checked by simply controlling each part of the website with chrome dev tools.

### Testing forms + Post & Get to/from DB

As the website rely heavily on its forms for user authentication, payment process as well as adding and editing pieces, extensive testing on them was made. 

#### Login 
Tested by:
- entering correct login info and logging in, got the data correctly from DB everytime
- entering incorrect login info and trying to login, form security stopped it from happen
- entering required fields in wrong format (e.g. password length), form security stopped it from happen
- entering nothing and trying to login, form security stopped it from happen

#### Forgot password 
Tested by:
- entering correct e-mail info and press reset my password, e-mail sent to user with recovery link
- entering incorrect e-mail info and press reset my password, form security stopped it from happen
- entering e-mail with incorrect format and press reset my password, form security stopped it from happen

#### Sign Up
Tested by:
- entering new user information and click sign up, posted the information correctly to DB everytime
- entering parts of form and click sign up, form security stopped it from happen
- entering required fields in wrong format (e.g. e-mail), form security stopped it from happen
- entering already existing user information, got the already registered user information everytime
- entering nothing and trying to sign up, form security stopped it from happen


#### Add/update piece 
Tested by:
- entering new piece information and click add, posted the information correctly to DB everytime
- entering new information on already existing piece, updated the information correctly to DB everytime
- tested leaving fields empty to see that it did not work to add, form security stopped it from happen

#### Purchase piece 
Tested by:
- entering all the information in address and contact form correctly and used Stripe test card which should work, purchase went through everytime as well as the order got posted to DB correctly, it also showed up on users account if user was logged in
- entering something wrong in the form and try to process payment, form security stopped it from happen
- tested leaving fields empty to see that it did not work to go through with order, form security stopped it from happen

#### Update account info 
Tested by:
- entering account information in the form and click update, posted the information correctly to DB everytime
- entering new information on checkout and tick save box to see if it updates correctly on account page, updated the information correctly to DB and account everytime
- tested leaving fields empty to see that it did not work to update, form security stopped it from happen

### Bugs

| Bug | Solution | Current status |
| --- | -------- | -------------- |
| Remove button do not remove item from cart | Solved by adding a slash after 'itemId' in JS code on cart.html | Solved |
| Webhook error 401 when testing webhooks via Stripe | Solved by making the workspace and port public | Solved |
| Webhook error 400 when testing webhooks via Stripe  | Solved by replacing the signing secret key and restarting workspace | Solved |
| JS error '$.Post is not a function', did not work to go through with a purchase | Solved by removing slim JS from base template and replace it with min JS | Solved |
| METADATA is not showing in console when payment goes through, it is only showing when payment fails | Solved by moving the print statement to the correct webhook which was success one and not failed one | Solved |
| CHECKOUT process as logged out user causes error when processing payment | Solved by adding a “if user is authenticated” to saving profile information | Solved |
| Navbar dropdown does not work | Solved by removing “bs” from data-toggle as it was a different version of Bootstrap | Solved |
| Comments do not show up on website but get posted to db | Solved by correcting the view of piece_detail so it is possible to display data in front end | Solved |
| Video on index page not showing in deployed website | Solved by linking to the video directly from the S3 bucket in AWS | Solved |


### Browser and screen size responsiveness testing

Have done extensive testing in Chrome DevTools, different browsers as well as on physical devices I had access to. The website is responsive and it acts as it is supposed to when changing between devices, browsers and screen sizes.

**Websites used for testing on different screen sizes (other than what is mentioned above):**

- [whatismyscreenresolution.net](http://whatismyscreenresolution.net/multi-screen-test)
- [responsivetesttool.com](http://responsivetesttool.com/)

### HTML Validator (W3C Markup) - [Link](https://validator.w3.org)

Pushed my HTML code through the validator and got following messages which I corrected:

| Message | Solution |
| ------- | -------- |
| The align attribute on the div element is obsolete. Use CSS instead. | Solved by removing align and positioning it in CSS |
| The element button must not appear as a descendant of the a element. | Solved by creating a btn class with bootstrap |

**IMPORTANT!** Because I am using the django templating language in this app, there is bound to show a lot of warnings and errors connected to that. These warnings and errors have been checked and controlled and are deemed to be safe to disregard as they are not true errors for the application.

### CSS Validator (W3C CSS) - [Link](https://jigsaw.w3.org/css-validator)

Pushed my CSS code through the validator and got following messages:

| Message | Solution |
| ------- | -------- |
| No relevant warnings and no errors showing. | - |

### JSHint - [Link](https://jshint.com/)

Pushed my JavaScript code through JSHint where no major issues showed up.

| Message | Solution |
| ------- | -------- |
| Missing semicolon | Added semicolon where needed |

The report shows that there are several undefined variables '$', this is caused by using jQuery and therefore we can disregard them.

### PEP8 - [Link](http://pep8online.com/)

Pushed my Python code through PEP8 where only a few minor issues showed up, such as whitespace where it should not be and line too long. Code which is imported via Django will not be edited and might therefore give off a PEP8 error. Everything relevant is now solved and it does not show any issues anymore. 

| Message | Solution |
| ------- | -------- |
| Line too long | Found a way to split the line |

I have actively chosen to ignore two "line too long" pep8 issues which is found in the webhook_handler, this is because I cannot shorten it without making it very unclear for readers.

### User stories result

All of the testing and debugging above have left us with the result below on achieving the goal of our user stories listed in the top of this readme:

| User story | Result |
| ---------- | ------ |
| User stories as a new visitor | PASS |
| User stories as a shopper | PASS |
| User stories as a registered user | PASS |
| User stories as an admin | PASS |

## Deployment

In order to deploy my website I used Heroku. The deployment was made from the master branch and I did it through below steps:

### Running my project locally

In order to run this project locally you will be needing some pre-requisites, which are:

- **IDE** - of your choice (e.g. Gitpod) where you can write Python

- **GIT** - for version control

- **PIP** - to install packages

- **STRIPE Account** - to handle the payments

#### Steps

1. Go to the project repository which is here: [https://github.com/rudberga/CI-MS4-nft](https://github.com/rudberga/CI-MS4-nft)

2. You can download the repository code by either:
   - Clicking the "Code"- button up on the right in the repository and download code as a ZIP
   - Clone the repository directly in your IDE by running the command: 
   
    `gh repo clone rudberga/CI-MS3-calm`

3. Inside of your IDE, navigate to the directory where you have the repository locally, you do this by the command:

   `cd folder/folder/code` you replace "folder" with your own path
   
4. Time for you to activate your virtual environment. You will be doing this by using Python's venv.

   Enter the following into the CLI:

   MAC: `source .venv/bin/activate`
   
   PC: `.venv\Scripts\activate.bat`
   
5. Install all requirements that you need for the project to work properly. Do this by the following command:

   `pip3 install -r requirements.txt`
   
   This will install all the requirements from the [requirements.txt](https://github.com/rudberga/CI-MS4-nft/blob/master/requirements.txt) file.

6. Migrate models with the command:

   `python3 manage.py migrate`
   
7. Create the superuser in order to handle admin tasks:

   `python3 manage.py createsuperuser`
   
8. Now we need to upload data to the database locally which you will do with the command:

   `python3 manage.py loaddata db.json`

9. In order to make the project work correctly, we need a env.py file to enter all the environmental variables. You could either set this up straight in the IDE variables but the settings are differente depending on which IDE you use, therefore, in this guide we will create a separate file for it. 

10. Create a file called:

    `env.py`

    This is where we will store the variables. Make sure to add this file to your .gitignore in order to not show the variables publicly.
  
11. Inside the `env.py` file, enter the following variables:

    `os.environ.setdefault('SECRET_KEY', '<your variable>')`

    `os.environ.setdefault('DEVELOPMENT', '1')`

    `os.environ.setdefault('ALLOWED_HOSTS', '<your variable>')`

    `os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your variable>')`

    `os.environ.setdefault('STRIPE_SECRET_KEY', '<your variable>')`

    `os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your variable>')`

    `os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your variable>')`

     What these variables come from:

     - `SECRET_KEY` is set freely by yourself, recommended to be done with the help of a Django secret key generator
     - `STRIPE` is found in your Stripe account under API values (Overview > Get your test API keys) 

12. Time to run the application. You will do this by using the command:

   `python3 manage.py runserver`
   
13. Application port 8000 should now be open and you should be able to open it and see the website running.
   
### Heroku deployment

In order to deploy this project to Heroku you will be needing some pre-requisites (other than mentioned earlier), which are:

- **AWS** - account with [Amazon Web Services](https://aws.amazon.com/)
- **S3 bucket** - create a [S3 bucket](https://aws.amazon.com/s3/) on AWS to hold Static and media files
- **Heroku** - create an Heroku account where you will deploy your application

#### Steps

1. Log in to Heroku website

2. Create a new app by clicking **New** then **Create new app**

3. Choose name that is corresponding to the name of your application

4. Pick server closest to where you are located

5. In order to deploy to Heroku, we need to move our database from SQLite to **Heroku Postgres**. 
   Go to resources on Heroku and search for **Heroku Postgres**.

6. Add **Heroku Postgres** to the application and select **Hobby dev - free** when being asked

7. In order for this move from SQLite database to Heroku Postgres, we need to make sure that the libraries below are installed:

   - Gunicorn
   - dj-database-url
   - Psycopg
   
   They should already be installed as you installed the requirements.txt, however, please make sure they are before proceeding to next step.
   
   If not installed, please install them by command:
   
   `pip3 install Gunicorn (replace Gunicorn the library that needs to be installed)`

8. In `settings.py` comment out the database configuration. Add this instead:

   `DATABASES = { 'default': dj_database_url.parse(os.environ.get('< Your DATABASE_URL here >')) }`
   
   You will find your DATABASE_URL in Heroku under **Settings** and click **Reveal config vars**.
 
9. Migrate with the command:

   `python3 manage.py migrate`
   
10. After migrations are done, update your `settings.py` to look like below.
    The reason for this is for using Postgres in deployment and SQLite in development.

    ```
        if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.sqlite3',
                 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             }
         }
    ```
    
11. Go to Heroku settings and **reveal config vars**, in there you will need to fill in your variables. 
    These are the ones you need to fill in:
    
    | KEY        | VALUE           |
    | ------------- |:-------------:| 
    | AWS_ACCESS_KEY_ID | your own AWS_ACCESS_KEY_ID | 
    | AWS_SECRET_ACCESS_KEY	| your own AWS_SECRET_ACCESS_KEY | 
    | DATABASE_URL	| Heroku generates this | 
    | EMAIL_HOST_PASS	| your own EMAIL_HOST_PASS | 
    | EMAIL_HOST_USER	| your own EMAIL_HOST_USER | 
    | SECRET_KEY | your own SECRET_KEY | 
    | STRIPE_PUBLIC_KEY	| your own STRIPE_PUBLIC_KEY | 
    | STRIPE_SECRET_KEY | your own STRIPE_SECRET_KEY |
    | STRIPE_WH_SECRET_CH	| your own STRIPE_WH_SECRET_CH |
    | STRIPE_WH_SECRET_SUB | your own STRIPE_WH_SECRET_SUB |
    | USE_AWS	| True |
    | ALLOWED_HOSTS	| your own ALLOWED_HOSTS |

12. Create a Procfile and fill in this into the file:
    
    `$ web: gunicorn web: gunicorn nft.wsgi:application`

13. Freeze your requirements:

    `pip3 freeze > requirements.txt`
    
14. **Add**, **Commit** and **Push** all of this to Github.

15. Add this code to `settings.py` in order to config the AWS settings
    ```
    if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your-project'
    AWS_S3_REGION_NAME = 'your-server'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files storage
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
    
16. Go to Heroku website and connect the app with your GitHub repository. 
    This is done via clicking **Deploy** on dashboard, then next to **Deployment Method** connect your GitHub repository.
    
17. You may now do the first push to Heroku with the command:
    
    `git push heroku master`
    
18. The app should now build and be deployed via Heroku on a link like [https://rudberga-nft.herokuapp.com/](https://rudberga-nft.herokuapp.com/)

## Credits

### Content

- Text on FAQ-page was imported from [Morningbrew](https://www.morningbrew.com/daily/stories/2021/02/24/nft-frequently-asked-questions)
- Rest of text on all the pages of the website was written by myself

### Media
- Images and videos on this website was imported from [Unsplash](https://unsplash.com/) & [Pexels](https://www.pexels.com/)
- GIF files were imported from [Giphy](https://giphy.com/)
- Artist credits are found [here](static/docs/credit.md).

### Code

I have modified these code snippets in order for them to work in my project.
- Hovering over social links and icons: [Ian Lunn](https://ianlunn.github.io/Hover/#effects)
- Video responsiveness on home page: [W3 Schools](https://www.w3schools.com/html/html5_video.asp)
- Responsive button over video on home page [StackOverflow](https://stackoverflow.com/questions/35647044/boostrap-how-to-stick-a-button-over-an-image-when-re-sizing/35676474)
- Documentations for Bootstrap and jQuery
- Parts of code, although adjusted, imported from the Boutique Ado project created by Code Institute

### Disclaimer

This is a project for the course Full Stack Web Development diploma with Code Institute, it is not for commercial use. If you find any of your content that you want removed, please contact me directly via my e-mail rudberg@pm.me.
