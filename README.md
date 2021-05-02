<h1 align="center">nft. (README AND PROJECT IS CURRENTLY UNDER DEVELOPMENT)</h1> 

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

- [Stripe](https://stripe.com/)
   - Used for payments in the application

- [Balsamiq](https://balsamiq.com/)
   - Used for creating wireframes for the project
   

## Testing 

I have done a lot of testing throughout the project and below you will find it in a more structured manner. I have made sure that the user stories are tested and works well, also focused on responsiveness where I have used resources online as well as the physical devices I had access to. Whenever a new functionality of the site was implemented, I tested it. At the end of the development journey, I had a big testing day where I went through the sites full functionality again.

### Tests done in order to secure UI components

| Test | Method | Expected | Result |
| ---- | ------ | -------- | ------ |
| Log In | ------ | -------- | ------ |

### Tests done in order to secure structural integrity

#### Modals

Each modal implemented on the website was tested on several screen sizes and confirmed that it kept its responsive design.

This includes the modals for:

- Log in
- Sign up
- Add artist

#### Fonts

Fonts are consistent throughout the website, this was checked by simply controlling each part of the website with chrome dev tools.

### Testing forms + Post & Get to/from DB

As the website rely heavily on its forms for user authentication, payment process as well as adding and editing pieces, extensive testing on them was made. 

#### Login 
Tested by:
- entering correct login info and logging in, got the data correctly from DB everytime
- entering incorrect login info and trying to login, form security stopped it from happen
- entering nothing and trying to login, form security stopped it from happen

#### Sign Up
Tested by:
- entering new user information and click sign up, posted the information correctly to DB everytime
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
| Attribute a not allowed on element a at this point | Solved by removing one "a" in the tag as it accidentally was two of them |
| Character reference was not terminated by a semicolon | Solved by adding ";" to the end of the emojis |
| An img element must have an alt attribute, except under certain conditions. | Solved by adding alt that was missing |

**IMPORTANT!** Because I am using the jinja templating language in this app, there is bound to show a lot of warnings and errors connected to that. These warnings and errors have been checked and controlled and are deemed to be safe to disregard as they are not true errors for the application.

### CSS Validator (W3C CSS) - [Link](https://jigsaw.w3.org/css-validator)

Pushed my CSS code through the validator and got following messages which I corrected:

| Message | Solution |
| ------- | -------- |
| Value Error background-color 'none' is not a background-color value 'none' | Solved by adding 'transparent' instead of 'none' |

Also received a few warnings including for the variables created in CSS, I decide to disregard these warnings as I am confident that they do not pose any error for the website.

### JSHint - [Link](https://jshint.com/)

Pushed my JavaScript code through JSHint where no major issues showed up.

| Message | Solution |
| ------- | -------- |
| No relevant warnings and no errors showing. | - |

The report shows that there are several undefined variables '$', this is caused by using jQuery and therefore we can disregard them.

### PEP8 - [Link](http://pep8online.com/)

Pushed my Python code through PEP8 where only a few minor issues showed up, such as whitespace where it should not be. Everything is now solved and it does not show any issues anymore. 

| Message | Solution |
| ------- | -------- |
| No relevant warnings and no errors showing. | - |

### User stories result

All of the testing and debugging above have left us with the result below on achieving the goal of our user stories listed in the top of this readme:

| User story | Result |
| ---------- | ------ |
| User friendly layout | PASS |
| Register account, add, edit & delete artists | PASS |
| Preview of artists before signing up | PASS |
| Users posts gathered on profile page | PASS |
| Newsletter | PASS |
| Access to social links | PASS |
| Information about each artist | PASS |

## Deployment

In order to deploy my website I used Heroku. The deployment was made from the master branch and I did it through below steps:

### Running my project locally


## Credits

### Content

- Text on FAQ-page was imported from [Morningbrew](https://www.morningbrew.com/daily/stories/2021/02/24/nft-frequently-asked-questions)
- Rest of text on all the pages of the website was written by myself

### Media
- Images and videos on this website was imported from [Unsplash](https://unsplash.com/) & [Pexels](https://www.pexels.com/)
- GIF files were imported from [Giphy](https://giphy.com/)

### Code

I have modified these code snippets in order for them to work in my project.
- Hovering over social links and icons: [Ian Lunn](https://ianlunn.github.io/Hover/#effects)

### Disclaimer

This is a project for the course Full Stack Web Development diploma with Code Institute, it is not for commercial use. If you find any of your content that you want removed, please contact me directly via my e-mail rudberg@pm.me.
