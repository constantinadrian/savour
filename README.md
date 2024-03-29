# Savour

![Savour](static/readme/savour.jpg)

Savour is a web app build to attract all categories of users that are interested in cooking, eager to learn new recipes, and also be able to share their own recipes from different cuisine. 

[View live project here](https://savour.onrender.com)

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

    - [Render](#render)

    - [Heroku](#heroku)

    - [Local Clone](#local-clone)

5. [Credit](#credit)

6. [Disclaimer](#disclaimer)

[Back to Top](#table-of-contents)

-----

- ### UX:

  - #### User stories

    I.	First Time Visitor Goals:

    - To be able to quickly understand the purpose of the website. 

    - To be able to search recipes uploaded by other users

    - To be able to find recipes from different categories like appetizer, breakfast, lunch, etc.

    II.	Returning User Goals:

    - When I return to the website, I wanna be able to register to the website.

    - I wanna be able to share my recipe thru the website to other users, by uploading my own recipes.

    - I wanna be able to edit/delete the recipes the was uploaded by me.

    III.	Site Owner Goals:

    - To be able to add, edit and delete my own recipes

    - To be able to add, edit and delete recipe categories.

    - Be able to receive feedback from users.

    - To promote my brand of cooking tools


 - #### Strategy

    - The website was build for those users who love to cook and are eager to learn and try a new recipe. The website is designed with search functionality that allows users to search recipes from different categories and with different keywords. In order to attract more users and keep them on the website, users can register and share their own recipes as well with other users by creating/edit/delete their recipes. The purpose of all functionality it's for the owner of the website to promote his brand of kitchen tools.

    | Opportunity                                 | Importance | Viability / Feasibility |
    | :------------------------------------------ | :--------: | :---------------------: |
    | Home Page                                   |     5      |            5            |
    | Recipe Page - Search Recipes By Keywords    |     5      |            5            |
    | Shop Page - Search Products By Keywords     |     5      |            5            |
    | Register Page                               |     4      |            5            |
    | Login Page                                  |     4      |            5            |
    | Manage Category Page                        |     5      |            5            |
    | Recipe Category Page                        |     5      |            5            |
    | Create / Edit / Delete Recipes              |     5      |            4            |


[Back to Top](#table-of-contents)

-----
    
 - #### Scope

    Based on the strategy table all the feature were implemented in order to achieve user and owner goals

    - Home page - to quickly understand the purpose of the website

    - Recipes Page - where users can view all recipes

    - Shop Page - where the owner of a website can promote his brand of kitchen tools

    - Register Page - where user can create an account on the website

    - Login Page - where user can log in to his profile to add/edit/delete recipes

    - Manage Category Page - where the admin can create/edit/ delete category

    - Recipe Category Page - where users can view all the recipes from a specific category and search a recipe within a category

    - Add Recipe - where users can add their own recipes

[Back to Top](#table-of-contents)

-----
    
  - #### Structure

    - ##### Features: 

        Responsive on all screen devices.

      - ##### Existing Features:
    
        1. Home Page 

            - The logo of Savour

            - Navigation bar - to help the user navigate between the site pages: Categories, Recipes, Shop, Register, Login
            
            - Landing section - Where the user it's welcome with a hero image and welcome text.

            - Recipe section - Where the user can see the most recent recipes uploaded

            - Shop section - Where the user can see the most recent kitchen tools uploaded

            - Footer - Where user can find links to site social media pages

        2. Recipes Page 

            - Landing section - Where user can see our suggestion recipe and navigate on that specific recipe page

            - Search field - Where users can search specific recipe by keywords

            - Recipe section - Where users can see all the recipes that are uploaded on the website

        3. Shop Page 

            - Where site owner promotes a brand of cooking tools

        4. Register 

            - Where the user can create an account.

        5. Login Page 

            - Where the user can log in to their account
 
        6. Category Page 

            - Where the users can view the recipes from just a category
 
        7. Recipe Page 

            - Where the users can view the recipe information. From this page, if logged in, the owner of the recipe can click on the edit link if he wants to edit his recipe

            - From this page, they can navigate to the category that the recipe is from

            - From this page, they can navigate to see all the recipes that were uploaded by the specific user

            - All users that are registered can rate on this page the recipes of other users

        8. Profile Page

            - Where the user can see all his recipes

        9. Add/Edit Recipe Page

            - Where the user can add his own recipe

        9. Manage Categories Page (Admin Only)

            - Where the Admin can add/edit/delete categories

        10. Contact Page 

            - Was added in case users wants to give any feedback or they have any comments about the website/recipes/products

        11. Terms and Conditions Page

            - Was added to state the website status, information regarding the registration, and the copyrights of some recipes

        12. 401 Page 

            - 401 Page - was added in case users wants to access the profile without being logged in

        13. 403 Page 

            - 403 Page - was added in case users wants to access other profile after they logged in

        14. 404 Page 

            - 404 Page - was added in case users redirect to a page that does not exist.
 
      - ##### Future Features to Implement:

        - To be able to find recipe from different cuisine.

        - To able to add recipes on favorites

        - Form Validation with WTForms.

        - Email Verification - Before registration is complete, in order to check the email address and so we know that the user is willingly registered and we don't have a case where users are using other person's emails for their registration.

        - Reset/Forget Password - Where user can recover their password

[Back to Top](#table-of-contents)

-----

- #### Skeleton

    -  Phone Wireframes: [Home](static/wireframes/phone/index-phone.png) [Recipes](static/wireframes/phone/all-recipes-phone.png) [Category](static/wireframes/phone/category-phone.png) [Contact](static/wireframes/phone/contact-phone.png) [Add Category](static/wireframes/phone/create-category-phone.png) [Add Recipe](static/wireframes/phone/create-recipe-phone.png) [Delete Category](static/wireframes/phone/delete-category-phone.png) [Delete Recipe](static/wireframes/phone/delete-recipe-phone.png) [Edit Category](static/wireframes/phone/edit-category-phone.png) [Edit Recipe](static/wireframes/phone/edit-recipe-phone.png) [Login](static/wireframes/phone/login-phone.png) [Manage Categories](static/wireframes/phone/manage-category-phone.png) [Profile Page](static/wireframes/phone/profile-phone.png) [Recipe Page](static/wireframes/phone/recipe-phone.png) [Register](static/wireframes/phone/register-phone.png) [Shop](static/wireframes/phone/shop-phone.png) 

    -  Tablet Wireframes: [Home](static/wireframes/tablet/index-tablet.png) [Recipes](static/wireframes/tablet/all-recipes-tablet.png) [Category](static/wireframes/tablet/category-tablet.png) [Contact](static/wireframes/tablet/contact-tablet.png) [Add Category](static/wireframes/tablet/create-category-tablet.png) [Add Recipe](static/wireframes/tablet/create-recipe-tablet.png) [Delete Category](static/wireframes/tablet/delete-category-tablet.png) [Delete Recipe](static/wireframes/tablet/delete-recipe-tablet.png) [Edit Category](static/wireframes/tablet/edit-category-tablet.png) [Edit Recipe](static/wireframes/tablet/edit-recipe-tablet.png) [Login](static/wireframes/tablet/login-tablet.png) [Manage Categories](static/wireframes/tablet/manage-category-tablet.png) [Profile Page](static/wireframes/tablet/profile-tablet.png) [Recipe Page](static/wireframes/tablet/recipe-tablet.png) [Register](static/wireframes/tablet/register-tablet.png) [Shop](static/wireframes/tablet/shop-tablet.png) 

    -  Desktop Wireframes: [Home](static/wireframes/desktop/index-page.png) [Recipes](static/wireframes/desktop/all-recipes-page.png) [Category](static/wireframes/desktop/category-page.png) [Contact](static/wireframes/desktop/contact-page.png) [Add Category](static/wireframes/desktop/create-category-page.png) [Add Recipe](static/wireframes/desktop/create-recipe-page.png) [Delete Category](static/wireframes/desktop/delete-category-page.png) [Delete Recipe](static/wireframes/desktop/delete-recipe-page.png) [Edit Category](static/wireframes/desktop/edit-category-page.png) [Edit Recipe](static/wireframes/desktop/edit-recipe-page.png) [Login](static/wireframes/desktop/login-page.png) [Manage Categories](static/wireframes/desktop/manage-category-page.png) [Profile Page](static/wireframes/desktop/profile-page.png) [Recipe Page](static/wireframes/desktop/recipe-page.png) [Register](static/wireframes/desktop/register-page.png) [Shop](static/wireframes/desktop/shop-page.png) 

    Note: A couple of pages have been slightly changed from the initial design and others like the Contact page have been added

[Back to Top](#table-of-contents)

-----

- #### Surface

    -  ##### Colour Scheme

        - Palette:

            ![Palette Colors](static/readme/palette_coolors.png) 

    -  ##### Typography

        - For this project I choose three types of Google Fonts: 'Crete Round', 'Lato' and 'Mr Dafoe'.

          For the consistency:

            - 'Mr Dafoe' fonts were used for the welcome text on the landing page when a user enters the site

            - 'Crete Round' fonts were used for the recipes and products title

            - 'Lato' fonts were used for the section titles and all other paragraphs within the page.

    -  ##### Imagery

        - Because imagery is important I have carefully chosen the background hero image on the landing page, as well as all others banners within the site that will reflect the site and each page's purpose.

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

  - #### Render

    - The project was deployed to Render using the following steps:

        1. Create ```requirements.txt``` file that contains a list of our Python dependencies by typing in the terminal 
        
            ```
            pip3 freeze --local > requirements.txt
            ```

        2. Push the ```requirements.txt``` file to GitHub with the following commands

            ```
            git add -A

            git commit -m

            git push
            ```

        3. Create an account on [render](https://dashboard.render.com/register?next=/)

        4. From the dashboard press ```New``` and can create a ```Web Service``` 

            ![](static/readme/render-new-web-service.jpg)

        5. Search for relevant repository and click “Connect”

        6. Choose a unique ```Name``` for your web service.

            Note: If the name is not unique on Render.com, a random hash with be appended to the name given, e.g. < name >-8wk9.onrender.com

        7. Choose a ```Region```

            Note: The [region](https://render.com/docs/regions) where your web service runs.

        8. Choose a ``` Branch ```

            Note: The repository branch used for your web service.

        9. Build Command

            ```
            pip install -r requirements.txt
            ```

            Note: This command runs in the root directory of your repository when a new version of your code is pushed, or when you deploy manually. It is typically a script that installs libraries, runs migrations, or compiles resources needed by your app.

        10. Start Command

            ```
            python app.py
            ```

            Note: This command runs in the root directory of your app and is responsible for starting its processes. It is typically used to start a webserver for your app. It can access environment variables defined by you in Render.

        11. Select Instance Type

            ![](static/readme/render-instance-type.jpg)

            Note: For the purpose of this project I select the free type, but feel free to explore their [pricing structure](https://render.com/pricing) and [free plan limitations](https://render.com/docs/free#free-web-services).

        12. Click on the ``` Advance ``` in order to set up the Environment variables

            ![](static/readme/render-advance-setting.jpg)

        12. Click on the ``` Add Environment Variable ``` and your variable

            ![](static/readme/render-add-environment-variable.jpg)

            | Key             | Value                                                                                                                        |
            | :---------------| :--------------------------------------------------------------------------------------------------------------------------: |
            | IP              | 0.0.0.0                                                                                                                      |
            | MONGO_DBNAME    | <your_database>                                                                                                              |
            | MONGO_URI       | mongodb+srv://<user>:<password>@<your_cluster>.ol3x3.mongodb.net/<yourdatabase>?retryWrites=true&w=majority&authSource=admin |
            | PORT            | 5000                                                                                                                         |
            | SECRET_KEY      | <your_secret_key>                                                                                                            |
        
            Note: The IP and PORT variables are used within the Flask application and should not be modified.

        13. Select option for ```Auto-Deploy```

            Note: For the purpose of this project I select ```No``` 

        14. Finally click ``` Create Web Service ```

            ![](static/readme/render-create-web-service.jpg)

  - #### Heroku

    - The project was deployed to Heroku using the following steps:

        1. Create ```requirements.txt``` file that contains a list of our Python dependencies by typing in the terminal 
        
            ```
            pip3 freeze --local > requirements.txt
            ```

        2. Create ```Procfile``` file that tells Heroku how to run our project by typing in the terminal

            ```
            echo web: python run.py > Procfile
            ```

        3. Push the ```requirements.txt``` and ```Procfile``` file to GitHub with the following commands

            ```
            git add -A

            git commit -m

            git push
            ```

        4. In order to deploy to Heroku you need an [account](https://signup.heroku.com/login?redirect-url=https%3A%2F%2Fid.heroku.com%2Foauth%2Fauthorize%3Fclient_id%3Dd2ef2b24-e72c-4adf-8506-28db2218547d%26response_type%3Dcode%26scope%3Dglobal%252Cplatform%26state%3DSFMyNTY.g2gDbQAAADFodHRwczovL2Rhc2hib2FyZC5oZXJva3UuY29tL2F1dGgvaGVyb2t1L2NhbGxiYWNrbgYAnwF4L3kBYgABUYA.q2PQc0k53ICJ0LR6VFKbOkyuEqmEtG0iuVzTM38UNAI)

        5. Now you can create a new app from the dashboard ```New``` Menu

        ![](static/readme/heroku-app.jpg)

        6. Now you need to set up a name and select a region closest to you

            NOTE: Remember the name has to be unique and generally use a dash and lowercase letters

        6. From the dashboard of your app click on the settings and go to Reveal Config variables

        ![](static/readme/heroku-settings.jpg)

        7. Set up the Config Vars 

            | Key             | Value                                                                                                       |
            | :---------------| :---------------------------------------------------------------------------------------------------------: |
            | IP              | 0.0.0.0                                                                                                     |
            | MONGO_DBNAME    | <your_database>                                                                                             |
            | MONGO_URI       | mongodb+srv://<user>:<password>@<your_cluster>.ol3x3.mongodb.net/<yourdatabase>?retryWrites=true&w=majority |
            | PORT            | 5000                                                                                                        |
            | SECRET_KEY      | <your_secret_key>                                                                                           |      

        8. Hide the Config Vars

        9. Now from the dashboard of your app click on the Deploy and from the Deployment method select ``` Github - Connect to Github```. Next on the search field type the name of the repository you want to deploy.
        
        ![](static/readme/heroku-deploy.jpg)

        10. Once it finds your repository click ```Connect``` 

        11. Next you can click ```Enable Automatic Deploys```

        ![](static/readme/heroku-enable-automatic-deploys.jpg)

        12. Now From Manual Deploy you can click ```Deploy Branch``` and once it's finished you can click ```View```

        ![](static/readme/heroku-deploy-branch-view.jpg) 

  - #### Local Clone

    ##### In order to run this project locally you should have installed these 3 requirements on your machine plus an account on [MongoDB Atlas](https://www.mongodb.com/):

    1. [VS Code](https://code.visualstudio.com/) - IDE or your personal preference

    2. [Pyhton3](https://www.python.org/) - to run the application on your local machine

    3. [PIP](https://pypi.org/project/pip/) for installation of tools needed in this project.

    Now you can create an account on [MongoDB Atlas](https://www.mongodb.com/) and follow the steps from [here](https://docs.atlas.mongodb.com/getting-started/). The MongoDB collection for this project can be found [here](static/savour_collections)
    
    Optional: you can install [Git](https://git-scm.com/)

    ##### Steps to follow

    1. At the top of the repository click on Code and click on download zip and extract the zip file to your chosen folder or keep the same name

        ![](static/readme/code-clone.jpg)

    Optional: if you have [Git](https://git-scm.com/) install on your machine you can type

    ```
    git clone https://github.com/constantinadrian/savour
    ```

    or to clone the repository into a different name on the folder you can run 

    ```
    git clone https://github.com/constantinadrian/savour folder_name
    ```

    more info about cloning with git [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository).

    2. Create a virtual environment within the project directory to keep dependencies required by the project separate from other projects by creating an isolated Python virtual environment.

    ```
    py -3 -m venv venv
    ```

    3. Activate the environment

    ```
    venv\Scripts\activate
    ```

    NOTE: If you run on Linux/maxOS more info for step 2 and 3 [here](https://flask.palletsprojects.com/en/2.0.x/installation/) 

    4. Install all dependencies from requirements.txt:

    ```
    pip3 install -r requirements.txt
    ```

    Note: For upgrade PIP type this command ```pip3 install --upgrade pip```

    5. Declare default environment variables in a file ```env.py``` 

    ```
    import os

    os.environ.setdefault("SECRET_KEY", "your_secret_key")
    os.environ.setdefault(
        "MONGO_URI", "mongodb+srv://<user>:<password>@<your_cluster>.ol3x3.mongodb.net/<yourdatabase>?retryWrites=true&w=majority")   
    os.environ.setdefault("MONGO_DBNAME", "<yourdatabase>")
    ```
    6. Add ```env.py``` to your ```.gitignore``` file.

    7. To run the project run 
    ```
    flask run
    ```

    NOTE: to run the project with ```py app.py``` on the ```app.py``` file change the code from line 1068 to

    ```
    if __name__ == "__main__":
        app.run()
    ``` 

    8. Now you can visit the website at http://127.0.0.1:5000

[Back to Top](#table-of-contents)

-----

- ### Credit

  - #### Code

    - Code for function sendMail was adapted from Full Stack Development Course - Interactive Frontend Development - Resume Project at [Code Institute](https://codeinstitute.net/)

    - [SweetAlert2](https://sweetalert2.github.io/#download) - for box alert hat was used on the contact form as a response generated on user action when the form is submitted

    - [Bootstrap](https://getbootstrap.com/) – CSS framework used to help with the navbar, cards, forms, modal and other classes that were used to make the app responsive.

    - [Bootstrap Modal JS](https://getbootstrap.com/docs/4.6/components/modal/) - Code snippet adapted for update the modal content with information that has to be edited/deleted

    - [Favicon](https://favicon.io/favicon-converter/) - for the code for use in this project; the favicon was created by the developer and saved in all sizes that were needed

    - Pagination was inspired by this two website and modified and adapted to my understanding of my project

        - [https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) 

        - [https://harishvc.com/2015/04/15/pagination-flask-mongodb/](https://harishvc.com/2015/04/15/pagination-flask-mongodb/)
    
    - [Decorate routes to require login](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/) - function adapted and used for user authentication in my project

    - [bson.errors.InvalidId](https://www.programcreek.com/python/example/87925/bson.errors.InvalidId) - used to check the ObjectId of each recipe/category before edit or delete

    - [https://jqueryvalidation.org/documentation/](https://jqueryvalidation.org/documentation/) - used for validation on Frontend

    - [w3schools](https://www.w3schools.com/jsref/event_onerror.asp) - used if an error occurs when loading an image

    - [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events) - for touch events on IOS as the navbar didn't close on click event on IOS when the click was on the document. Also used MDN Web Docs for general info

    - [Jinja Docs](https://jinja.palletsprojects.com/en/3.0.x/templates/#import) - for import and general info

    - [Email Regex](https://emailregex.com/) - used as pattern for validate email address

  - #### Content

    - [Taste Life](https://www.tasteshow.com/) - used as general inspiration

    - [Great British Chefs](https://www.greatbritishchefs.com/) - used as general inspiration

    - All Recipes uploaded on this project by admin were taken from [Great British Chefs](https://www.greatbritishchefs.com/) and they own the copyright

  - #### Media

    - All photos used on this project as a hero image, banners, default banner, and default recipe image were from:

        - [Pexels](https://www.pexels.com/)

        - [Pixabay](https://pixabay.com/)

  - #### Acknowledgements

    - [Code Institute](https://codeinstitute.net/) for all course material 

    - Slack community

    - My mentor Oluwafemi Medale for his support and feedback that he has given me for this milestone project.

[Back to Top](#table-of-contents)

-----

- ### Disclaimer

  - This project is for educational purposes only.
