# Testing

## Table of Contents

1. [Code Validation](#code-validation)

    - [HTML](#html)

    - [CSS](#css)

    - [JS](#js)

    - [PEP8](#pep8)

2. [Browser compatibility and responsiveness](#browser-compatibility-and-responsiveness)

    - [Testing on Different Browsers](#testing-on-different-browsers)

    - [Testing on Different Devices](#testing-on-different-devices)

3. [Testing User Stories](#testing-user-stories)

4. [Manual testing](#manual-testing)

5. [Bugs and Fixs](#bugs-and-fixs)

-----

- ### Code Validation  

    - #### HTML 
    
        HTML checked was done with [The W3C Markup Validation Service](https://validator.w3.org/)
        
         - All Pages 
         
            ![](static/readme/index-page-test.png)

    - #### CSS 
    
        CSS checked was done with [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    
        - CSS - style.css
        
            ![](static/readme/w3c-css-validator-style-css.jpg)

            - The warnings were for:

                The value break-word is deprecated.

                Same color for background-color and border color on pagination links

                And the rest for unknown vendor extension

        - CSS - recipe.css

            ![](static/readme/w3c-css-validator-recipe-css.jpg)

            - The warnings were for:

                The value break-word is deprecated.

                And the rest for unknown vendor extension

        - CSS - forms.css

            ![](static/readme/w3c-css-validator-forms-css.jpg)

            - The warnings were for:

                The value break-word is deprecated.

                And the rest for unknown vendor extension
        

    - #### JS 
    
        JS checked was done with [JSHint, a JavaScript Code Quality Tool](https://jshint.com/)

        - script.js

            - 21 warnings: 
                
                'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). 

            - Unused variable:

                $ - jquery function.

        - recipe.js

            - 15 warnings:

                'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). 

                'template literal syntax' is only available in ES6 (use 'esversion: 6').

            - Unused variable:

                $ - jquery function.

        - jquery_validate_forms.js

            - 30 warnings:

                'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). 

                'computed property names' is only available in ES6 (use 'esversion: 6').

            - Unused variable:

                $ - jquery function.

                sendMail - function that it's call with onsubmit attribute when the contact form is submitted with emailjs

        - emailjs.js

            - The three undefined variable are:

                emailJS - is a service that allows us to send emails directly from your client-side JavaScript code.

                $ - jquery function.

                Swal - sweetalert2 library that acts as a replacement for the JavaScript’s alert() function.

            - Unused variable:

                sendMail - function that it's call with onsubmit attribute when the contact form is submitted with emailjs

        - add_recipe.js

            - 21 warnings

                'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). 

                'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

                'template literal syntax' is only available in ES6 (use 'esversion: 6').

                Missing semicolon

            - Unused variable:

                $ - jquery function.

    - #### PEP8 
    
        [PEP8 Validator](http://pep8online.com/) was used to validate Python code

        - app.py - All right

        - helpers.py - All right

[Back to Top](#table-of-contents)

-----
       
- ### Browser compatibility and responsiveness

  - #### Testing on Different Browsers

    - The following web browsers were used for testing the browser compatibility and responsiveness (System: Windows 10 64-bit).

        1. Chrome - Version 89.0.4389.90 (Official Build) (64-bit)

        2. Firefox - 87.0 (64-bit)

        3. Edge - Version 89.0.774.57 (Official build) (64-bit)

        4. Opera - Version:74.0.3911.232

        All test was good. 

        Note: No test was perform for Internet Explorer.

  - #### Testing on Different Devices

    1. iPhone 11 - IOS 14.0.1

    2. Ipad Mini 2 - IOS 12.4.8 

    3. Huawei P Smart

    4. iPhone 5S - IOS 10.2.1

    All test was good with some exceptions from IOS (see Bugs and Fixs).

  - A large amount of testing was done to ensure that all pages were linked correctly.

[Back to Top](#table-of-contents)

-----

- ### Testing User Stories

    I. First Time Visitor Goals

    - To be able to quickly understand the purpose of the website. 

        - When the user enters the site he can easily understand the purpose of the website from the hero image, the welcome text and the easy-to-read-navigation menu 

    - To be able to search recipes uploaded by other users

        - On Recipes Page / Search Page the users can search any recipes uploaded by each user

    - To be able to find recipe from different categories like: appetizer, breakfast, lunch etc.

        - On Recipes Page / Search Page users can search recipes from different categories

        - On Category Page users can search recipes within the specific category

    II.	Returning User Goals:

    - When I return to the website, I wanna be able to register to website.

        - The app was build with the register/login functionality 

    - I wanna be able to share my recipe thru the website to other users, by uploading my own recipes.
    
        - After register on navigation page the user can use the link to "Add recipe page" and on profile page the user have a button which will take him on "Add recipe page" 

    - I wanna be able to edit/delete the recipes the was uploaded by me.  

        - When user is login and access his recipes from profile page / recipes page / category page all individual recipes will display an "Edit" link on the top left side of the recipe

    III. Site Owner Goals:

    - To be able to add, edit and delete my own recipes

        - The site Owner, as well as the users, can add, edit or delete his own recipes

    - To be able to add, edit and delete recipe categories.

        - The site his the only on who can add, edit or delete recipe categories.

    - Be able to receive feedback from user.

        - The owner of the website can receive any message/feedback from register users or first time users thru the contact form 

    - To promote my brand of cooking tools

        - The purpose of the website it's for the owner to promote his brand of kitchen tools.

[Back to Top](#table-of-contents)

-----

- ### Manual testing

    - Testing all links from the navigation bar on the index page

        - Expected: 

        - Result: 

    - 404 page

        - Expected: if the user redirects to a page that does not exist a custom 404 page will display a message with a button to redirect to the home page.

        - Testing: Different page was trying to access from URL 

        - Result: the user's redirecting to 404 page.

[Back to Top](#table-of-contents)

-----

- ### Bugs and Fixs

    - 

        - 

        - 


Return to [README.md](README.md)