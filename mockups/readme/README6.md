   
    * https://validator.w3.org/ *
  `https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template`


  1.  pip3 install django
    pip3 install autopep8 (for white space and gr8 for indentations etc)
1.  django-admin startproject kuk_marketing 
    To add a boilerplate: type html and a list and basic boilerplate for an html5 file.  gitpod shortcut or press arrow up then select ! press enter to create boilerplate.
1.  python3 manage.py migrate
1.  python3 manage.py runserver
1.  touch .gitignore
1.  python3 manage.py runserver
1.  python3 manage.py migrate
1.  python3 manage.py createsuperuser
1.  git remote -v (we are already linked to github)
1.  pip3 install django-allauth
1.  configure settings
1. install travis
    #### travis https://travis-ci.org
        which version 
        `python -V`
    ```AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

    1.  Add site_id = 1  underneath the authentication backends.
   1.  configure urls
   1.  python3 manage.py migrate
   1.  python3 manage.py runserver
   1.  navigate to accounts/login and login and add superusers and test
   1.  logout and you should be redirected to home page
   1.  set up a base template with bootstrap
   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
            
            This copies or the allauth templates in the packages so we can style them at will.
1.      Getbootstrap.com > go to documentation and copy the starter template 
    
    ### font stories  
    *About Roboto
        Roboto has a dual nature. It has a mechanical skeleton and the forms are largely geometric. At the same time, the font features friendly and open curves. While some grotesks distort their letterforms to force a rigid rhythm, Roboto doesn’t compromise, allowing letters to be settled into their natural width. This makes for a more natural reading rhythm more commonly found in humanist and serif types.

        This is the regular family, which can be used alongside the Roboto Condensed family and the Roboto Slab family.
        <addr>font-family: 'Montserrat', sans-serif;</Addr>
        <Addr>-family: 'Roboto', sans-serif;</Addr>

        To contribute, see github.com/google/roboto*
1.  
1.      <addr>The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to design this typeface and rescue the beauty of urban typography that emerged in the first half of the twentieth century. As urban development changes that place, it will never return to its original form and loses forever the designs that are so special and unique. The letters that inspired this project have work, dedication, care, color, contrast, light and life, day and night! These are the types that make the city look so beautiful. The Montserrat Project began with the idea to rescue what is in Montserrat and set it free under a libre license, the SIL Open Font License.
            This is the normal family, and it has two sister families so far, Alternates and Subrayada. Many of the letterforms are special in the Alternates family, while 'Subrayada' means 'Underlined' in Spanish and celebrates a special style of underline that is integrated into the letterforms found in the Montserrat neighborhood. Updated November 2017: The family was redrawn by Jacques Le Bailly at Baron von Fonthausen over the summer, and the full set of weights were adjusted to make the Regular lighter and better for use in longer texts. In fall, Julieta Ulanovsky, Sol Matas, and Juan Pablo del Peral, led the development of Cyrillic support, with consultation with Carolina Giovagnoli, Maria Doreuli, and Alexei Vanyashin.

            The Montserrat project is led by Julieta Ulanovsky, a type designer based in Buenos Aires, Argentina. To contribute, see github.com/JulietaUla/Montserrat
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,400;1,100;1,200;1,300;1,600&family=Roboto:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
            CSS rules to specify families

            font-family: 'Montserrat', sans-serif;
            font-family: 'Roboto', sans-serif;</addr>

## Home app
1.      `python3 manage.py startapp home`
                mkdir -p home/templates/home
1.      add the home app : `python3 manage.py startapp home`
1.      then create a templates directory in the home app > mkdir -p to create parents as required.
                    `mkdir -p home/templates/home`
                        And then right-click the inner *home directory*, new file and create *index.html*

1.          *extend the base template with extends base.html
                And load the static tag with load static, so we can use static files as needed.
                Lastly, we just need a content block with some content in it. So let's start with block content.
                And inside that, I'll just add a simple h1 with class equals display-4 and text-success
                to ensure bootstrap is working.  And I'll add the text it works.*
1.          *view* to render this template so let's head into **views.py*
                        And define an index view.
                        Which will simply render the index template.
1.          *class inheritance* = it's going to be very important as you progress
            in your understanding of python and object-oriented programming in general.
             - remember that if you need functionality *from one class to be available in another*.
            All you need to do is inherit the one you need.
            inherit all the base functionality from the built-in Django model class. 
            -  Built-in Django fields called a char field. Example below:
              name = models.Charfield() = has characters or text in it.  
              done = boolean.Field() =    true or false.    So models.boolean field
                
                 

[![Build Status](https://travis-ci.com/SOliv1/ms-4-kuk-marketing.svg?branch=master)](https://travis-ci.com/SOliv1/ms-4-kuk-marketing)