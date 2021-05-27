# Savour

![Savour](static/readme/savour.jpg)

Savour is a web app build to attract all categories of users that are interested in cooking, eager to learn new recipes and also be able to share their own recipe from different cuisine. 

[View live project here](https://savour-food.herokuapp.com/)

## Table of Contents

1. [UX](#ux)

    - [User stories](#user-stories)

    - [Strategy](#strategy)

    - [Scope](#scope)

    - [Structure](#structure)

    - [Skeleton](#skeleton)

    - [Surface](#surface) 

2. [Technologies Used](#technologies-used)

3. [Testing](#testing)

4. [Deployment](#deployment)

    - [Inception project](#inception-project)

    - [GitHub Pages](#github-pages)

    - [Local Clone](#local-clone)

5. [Credit](#credit)

6. [Disclaimer](#disclaimer)

[Back to Top](#table-of-contents)

-----

- ### UX:

  - #### User stories

    I.	First Time Visitor Goals:

    - To be able to quickly understand the purpose of the website. 

    - To be able to find recipe from different cuisine.

    - To be able to find recipe from different categories like: appetizer, breakfast, lunch etc.

    II.	Returning User Goals:

    - When I return to the website, I wanna be able to register to website.

    - I wanna be able to share my recipe thru the website to other users, by uploading my own recipes.

    - I wanna be able to edit/delete the recipes the was uploaded by me.

    III.	Site Owner Goals:

    - To be able to add, edit and delete my own recipes

    - To be able to add, edit and delete recipe categories.

    - Be able to receive feedback from user.

    - To promote my brand of cooking tools


 - #### Strategy

    - The website was build to those users who love to cook and are eager to learn and try new recipe. The website is designed with search functionality that allow users to search recipes from different category and with different keywords. In order to attract more users and keep them on the website users can register and share their own recipe as well with other users by create/edit/delete their recipe. The purpose of all functionality it's for the owner of website to promote his brand of kitchen tools.

    | Opportunity                                 | Importance | Viability / Feasibility |
    | :------------------------------------------ | :--------: | :---------------------: |
    | Home Page                                   |     5      |            5            |
    | Recipe Page - Search Recipes By Keywords    |     5      |            5            |
    | Shop Page                                   |     5      |            5            |
    | Register Page                               |     4      |            5            |
    | Login Page                                  |     4      |            5            |
    | Manage Recipe Category Page                 |     5      |            5            |
    | Create / Edit / Delete Recipes              |     5      |            4            |


[Back to Top](#table-of-contents)

-----
    
 - #### Scope

    Based on the strategy table all the feature were implemented in order to achieve user and owner goals

    - Home page - to quickly understand the purpose of the website

    - Recipe Page - where users can view all recipes

    - Shop Page - where the owner of website can promote his brand of kitchen tools

    - Register Page - where user can create an account on the website

    - Login Page - where user can login to the his profile to add/edit/delete recipes

    - Manage Recipe Category Page - where the admin can create/edit/ delete category

[Back to Top](#table-of-contents)

-----
    
  - #### Structure

    - ##### Features: 

        Responsive on all screen devices.

      - ##### Existing Features:
    
        1. Home Page 

          - The logo of Savour

          - Navigation bar - to help user navigate between the site pages: Categories, Recipes, Shop, Register, Login
          
          - Landing section - Where the user it's welcome with a hero image and welcome text.

          - Recipe section - Where the user can see three random recipes

          - Shop section - Where the user can see the kitchen tools

          - Footer - Where user can find links to site social media pages

        2. Recipe Page 

          - Landing section - Where user can see the recipe of the day 

          - Search field - Where user can search specific recipe

        3. Shop Page

          - Where site owner promote a brand of cooking tools

        4. Register

          - Where the user can create an account.

        5. Login Page

          - Where the user can login in into their account

        6. 404 Page

          - 404 Page - was added in case users redirect to a page that does not exist.
 
      - ##### Future Features to Implement:

        - Email Verification - Before registraion is complete 

        - Reset/Forget Password - Where user can recover their password

[Back to Top](#table-of-contents)

-----

- #### Skeleton

    -  Phone Wireframes: [Home](static/wireframes/phone/index-phone.png) [Recipes](static/wireframes/phone/all-recipes-phone.png) [Category](static/wireframes/phone/category-phone.png) [Contact](static/wireframes/phone/contact-phone.png) [Add Category](static/wireframes/phone/create-category-phone.png) [Add Recipe](static/wireframes/phone/create-recipe-phone.png) [Delete Category](static/wireframes/phone/delete-category-phone.png) [Delete Recipe](static/wireframes/phone/delete-recipe-phone.png) [Edit Category](static/wireframes/phone/edit-category-phone.png) [Edit Recipe](static/wireframes/phone/edit-recipe-phone.png) [Login](static/wireframes/phone/login-phone.png) [Manage Categories](static/wireframes/phone/manage-category-phone.png) [Profile Page](static/wireframes/phone/profile-phone.png) [Recipe Page](static/wireframes/phone/recipe-phone.png) [Register](static/wireframes/phone/register-phone.png) [Shop](static/wireframes/phone/shop-phone.png) 

    -  Tablet Wireframes: [Home](static/wireframes/tablet/index-tablet.png) [Recipes](static/wireframes/tablet/all-recipes-tablet.png) [Category](static/wireframes/tablet/category-tablet.png) [Contact](static/wireframes/tablet/contact-tablet.png) [Add Category](static/wireframes/tablet/create-category-tablet.png) [Add Recipe](static/wireframes/tablet/create-recipe-tablet.png) [Delete Category](static/wireframes/tablet/delete-category-tablet.png) [Delete Recipe](static/wireframes/tablet/delete-recipe-tablet.png) [Edit Category](static/wireframes/tablet/edit-category-tablet.png) [Edit Recipe](static/wireframes/tablet/edit-recipe-tablet.png) [Login](static/wireframes/tablet/login-tablet.png) [Manage Categories](static/wireframes/tablet/manage-category-tablet.png) [Profile Page](static/wireframes/tablet/profile-tablet.png) [Recipe Page](static/wireframes/tablet/recipe-tablet.png) [Register](static/wireframes/tablet/register-tablet.png) [Shop](static/wireframes/tablet/shop-tablet.png) 

    -  Desktop Wireframes: [Home](static/wireframes/desktop/index-page.png) [Recipes](static/wireframes/desktop/all-recipes-page.png) [Category](static/wireframes/desktop/category-page.png) [Contact](static/wireframes/desktop/contact-page.png) [Add Category](static/wireframes/desktop/create-category-page.png) [Add Recipe](static/wireframes/desktop/create-recipe-page.png) [Delete Category](static/wireframes/desktop/delete-category-page.png) [Delete Recipe](static/wireframes/desktop/delete-recipe-page.png) [Edit Category](static/wireframes/desktop/edit-category-page.png) [Edit Recipe](static/wireframes/desktop/edit-recipe-page.png) [Login](static/wireframes/desktop/login-page.png) [Manage Categories](static/wireframes/desktop/manage-category-page.png) [Profile Page](static/wireframes/desktop/profile-page.png) [Recipe Page](static/wireframes/desktop/recipe-page.png) [Register](static/wireframes/desktop/register-page.png) [Shop](static/wireframes/desktop/shop-page.png) 

[Back to Top](#table-of-contents)

-----

- #### Surface

    -  ##### Colour Scheme

        - Palette:

            ![Palette Colors](static/readme/palette_coolors.png) 

    -  ##### Typography

        - For this project I choose three types of Google Fonts: 'Crete Round', 'Lato' and 'Mr Dafoe'.

          For the consistency:

            - 'Mr Dafoe' fonts were used for the welcome text on landing page when user enters the site

            - 'Crete Round' fonts were used for the recipes and products title

            - 'Lato' fonts were used for the section titles and all other paragraphs within the page.

    -  ##### Imagery

        - Because imagery is important I have carefully chosen the background hero image on landing page, as well as all others banners within the site that will reflect the site and each page purpose.

[Back to Top](#table-of-contents)

-----

- ### Technologies Used

  - #### Languages:

    - [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to structure website and its content.

    - [CSS3](https://en.wikipedia.org/wiki/CSS) - to format the contents of each webpage.

    - [JS](https://en.wikipedia.org/wiki/JavaScript) - for DOM manipulation.

    - [Pyhton3](https://www.python.org/) – to add functionalities to the server-side

    - [MongoDB Atlas](https://www.mongodb.com/) - for database

  - #### Frameworks, Libraries & Programs:

    - [Bootstrap](https://getbootstrap.com/) – CSS framework used to help with the navbar, cards, forms, modal and other classes that were used to make the app responsive.

    - [Google Fonts](https://fonts.google.com/) - to import the font-family used in the website: 'Crete Round', 'Lato' and 'Mr Dafoe'.

    - [Font Awesome](https://fontawesome.com/) - icons are a visual way to help add meaning to elements.

    - [GitHub](https://github.com/) - used to create and host the repository

    - [Git](https://git-scm.com/) - used for the version-control system for tracking changes in any set of files

    - [Gitpod](https://gitpod.io/) - IDE used to develop the project 

    - [Flask](https://flask.palletsprojects.com/en/1.1.x/) – Python micro web framework

    - [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) – Python template engine 

    - [PyMongo](https://pypi.org/project/pymongo/) to make communication between Python and MongoDB database

    - [PIP](https://pypi.org/project/pip/) for installation of tools needed in this project.

    - [JQuery](https://jquery.com/)


  - #### Additional tools:

    - [VS Code](https://code.visualstudio.com/) - IDE

    - [Autoprefixer CSS](https://autoprefixer.github.io/) - used to add prefix to css code

    - [Tinypng](https://tinypng.com/) - used to compress all image files in order to reduce loading time on each page

    - [HTML Validator](https://validator.w3.org/) - used to check HTML code for error

    - [CSS Validator](https://jigsaw.w3.org/css-validator/) - used to check CSS code for error

    - [JSHint](https://jshint.com/) - used to check JS code for error

    - [JSDoc](https://jsdoc.app/) - document the JavaScript code with JSDoc

    - [PEP8 Validator](http://pep8online.com/) - was used to validate Python

    - [I Am Responsive](http://ami.responsivedesign.is/) - for the main image in Readme to show responsive to different screen size

    - [Balsamiq](https://balsamiq.com/) - used to make the wireframes for the project

    - [Coolors](https://coolors.co/) - used for color palette

    - [Adobe Photoshop 2020](https://www.adobe.com/ie/products/photoshop.html?gclid=Cj0KCQjwrsGCBhD1ARIsALILBYpcZ9gNDfvVo1tJUaPzX_D5Bbo7kr6tDseIjZmjRTGbiBTqIURjULAaAvGnEALw_wcB&mv=search&sdid=LZ32SYVR&ef_id=Cj0KCQjwrsGCBhD1ARIsALILBYpcZ9gNDfvVo1tJUaPzX_D5Bbo7kr6tDseIjZmjRTGbiBTqIURjULAaAvGnEALw_wcB:G:s&s_kwcid=AL!3085!3!441664403997!b!!g!!%2Bphotoshop!1423510553!55397634865) - used to create the savour logo (all rights reserved) and favicon for this project

[Back to Top](#table-of-contents)

-----

- ### Testing

    - Testing documentation can be found [HERE](TESTING.md)

 [Back to Top](#table-of-contents)

-----

- ### Deployment

  - #### Inception project 

    1. This project was created from the Code Institute project template from [here](https://github.com/Code-Institute-Org/gitpod-full-template) on Github by clicking on "Use this template"

        ![](static/readme/code-institute-project-template.png)

    2. Once the project was created I rename it from the settings 

        ![](static/readme/rename-project-from-settings.png)

    3. When the repository was finally completed I open the project with [Gitpod](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en) in Chrome browser

    4. In order to push this project from Gitpod on Github a set of commands were used:

        ```
        - git status  - Check the status of the repository and see if there were any changes in files 

        - git add .  - Add the files that were modified/created, so we can commit it 

        - git commit -m "message for commit"  - Commits all the changes

        - git push  - Pushes all committed versions to Github
        ```

  - #### Heroku

    - The project was deployed to Heroku using the following steps:

        1. 

        2. 

        3. 

        4. 

        5. 

  - #### Local Clone

    1. Log in to GitHub and locate GitHub Repository

    2. At the top of the repository click on Code 

    3. From the dropdown menu under HTTPS copy the link

    4. Now on your IDE create a directory where you wanna make the clone 

    5. Type git clone and paste the link that you copy from step 3. 

[Back to Top](#table-of-contents)

-----

- ### Credit

  - #### Code

    - [Bootstrap](https://getbootstrap.com/) - 

    - [Favicon](https://favicon.io/favicon-converter/) - for the code for use in this project; the favicon was created by the developer and saved in all sizes that were needed

  - #### Content

    - 

  - #### Media

    - 

  - #### Acknowledgements

    - [Code Institute](https://codeinstitute.net/) for all course material 

    - Slack community

    - My mentor Oluwafemi Medale for his support and feedback that he has given me for this milestone project.

[Back to Top](#table-of-contents)

-----

- ### Disclaimer

  - This project is for educational purposes only.
