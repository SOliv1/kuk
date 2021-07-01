# KUK Marketing

#### Table Of Contents
* General Information
* Live Demo
* UX Introduction
* User stories
* Wireframe Mockups
* Website & Database
* Accessibility
* Features
* Deployment
* Testing
* Credits
* Conclusion

###  LIVE DEMO CAN BE FOUND AT HEROKU: https://kuk-milestone-4.herokuapp.com/

### README  Further information and alternative view via LINK HERE
  README.md https://1drv.ms/w/s!AgMQTPoqZgRAjBzcw6gYVD7gImdt?e=5XbCvm
  
## UX Introduction - Platform for B2B lead - Visual appeal
I wanted to create a visually appealing website to showcase the clean and classic look to a novice customer who is thinking of 
of purchasing an initial start up project and wants something simple and straight forward without having to think too much about what they require.
(we can help here by filling out a form accessed via buttons throughout the website.)
A website where consumers can purchase with a budget in mind, either upgrading and / or investing in a website package.  
This website celebrates the user's ability to evaluate and purchase products and services with a view for them *to capture an online audience to their own website and ultimately promote and retain loyalty*.
Encourage and promote the user update / upgrade in order to captivate a target audience on desktop, mobile, and tablet. 
Drive leads to promote business awareness via website online-packages; purchase branded and non branded products to target audience.
The website is a B2C emotion driven and appeals to the benefits of users by encouraging visual interaction and engagement via website packages, products and gift or corporate brand or non branded purchases; and contact forms with requirements dropdown box.
Ideal additions to this website: a gallery; social-media; newsletters; Skype, Zoom and other live streaming for on-line interaction between consumers and marketeers.
Join a community that drives sales, marketing, and product innovation and trendsetters driving growth on the internet.  
Translate business growth into sales and loyalty.

#### Ideal Customer:
##### Target businesses:  
* *Start-Up Business* - operates on a budget and wants strategic direction.
* *Inspire An Audience* Those who want to invest in a fullstack premium package. 
* *Budget Awareness* - Those who would like to upgrade to a package without fully investing in premium package.

#### Visitors to this website are looking for:
* Ideas that can be transformed into success for their *startup business* or keep on trend with what is driving growth sales via the internet.
* This website is designed for those looking to translate their expertise into a viable proposition for their business and make it a reality.
* Visitors can contact the website to discuss their objectives whether it be to build brand awareness, generate leads, or drive website traffic. 
   The website designer aims to provide a format that is the `best fit`.
1. A new customer who wants to discover more about and potentially buy the products on offer via the website to promote their business. 
   A complete package for budget minded startup business.
1. As a new visitor to the website I want to be able to navigate quickly and easily via the search box and can look up products by category / price / rating / name of product.
1. As an interested visitor / customer I want to follow the activities of this website on social media.
1. As an engaged customers I want to return to the website and potentially purchase the products and find out what else is new and driving business success.  
   A contact form and newsletter will be set up for this. 
1. Provide *User-stories* and *example websites*, to the website to encourage new and returning customers.


## User Stories:
* As a customer, I want to be able to quickly look up the best products and services with a view to purchasing a complete website and branding startup package, so that I can order via the website from the company. 
I want to experiement with my ideas and engage with the web-company to find what suits or as they say `the best fit`: 
I want to edit / delete / and update with my own requriements by filling out the form and have them contact me with further information and ultimately purchase a suitable package to suit my budget. 
**Happy Customer**

* I love the look and feel of the website. It is clean and aesthetically simple to view and to use.  The images are glorious!
   I want to enquire and discuss my requirements with **KUKMarketing** and look forward to letting my `business shine!`
  **Satisfied Client** 
  
* I like the website packages available and the opportuntity to come up with my requriements for the `best fit` for improving my current website. 
 * **Looking to Shine**
 
* I like the idea of buying products and services directly from the website - gettting the quoted price and ordering the products and services I want.  
  I can use a simple form to convey my requirements which will then be evaluated and then open up dialogue between KUKmarketing and myself the (potential)client. 
  **Propspective Client**
  
## KUKMarketing = Wireframes and Mockups:

*Please follow the link below to view README.md /wireframes and / Mockups*:

[kuk-ms-4-marketing](http://github.com/SOliv1/ms-4-kuk-marketing/tree/master/readme)

			
## This Website & Database is heavily based on the Code Institute (C.I.) Boutique-Ado e-commerce fullstack project.
I chose **postgres** for my project, to use and demonstrate as a powerful fullstack database together with AWS bucket S3 storage facility and IAM users.  This is recommended by **C.I.** in the course. 
It features the excellent Boutique-Ado online project which I have copied and modified to suit the purposes of my own fullstack website project. My 'Services-App' on the website is mostly my own code gleaned from various C.I. projects and excercise, I have done during the course; chiefly (**C.I.**)'Thorin and Company and Bootstrap4' and my own Procol Harum project(**First Milestone**).
I figured the ideas on this website were so excellent, how can one improve! I therefore have copied most if not all except 'Services App' which is my owm but once again inspired from other projects on the course;(see credits and acknowledgements at bottom of this page) from the Boutique Ado Fullstack full-functioning website,
which I found most interesting.  The challenge for me is to be able to build the website exactly as it is done in the videos.  It is tricky but satisfying once I finally completed it.  I then repeated this website for my own purposes, building at each stage from conception to complettion.
My website Database consists of *Pages (to meet CRUD requirements via the Product / bag and Checkout apps - Create Read Update Delete) in a database*. A highly scalable server which stores data in a non-relational format.


#### Add products via backend admin(‘Create’, 'Read', 'Update', 'Delete')
This is how admin-users add products to the database. It contains a simple HTML form to collect the field attributes intending to store. 
The product collections are all categorised and stored in a json format and transferred to the database via `STATIC and MEDIA files` in `KUK - Settings` 
where it is stored remotely in a bucket at `AWS SERVICES`. The code is add . / commit -m "" / and push/ to GitHub and then channelled to Heroku which 
has been set up so that it automatically connects and should deploy continuously every time I push to github.  
I set up my deployment fairly early in the build process in order to give my self
less pressure and more peace of mind and watch more clearly the build process.


## Accessibility 
The pages are asscesible via buttons on the *Home page* and a menu accross the top with dropdown navigational menus.  The website is mobile friendly as well as compatible 
across ipad through to full-desktop. The about page can be accessed on the top right corner of the menu(home-page).  
The `contact page`  can be accessed via the 'Our Services' heading on the drop-down menu.  Also, from  `Get Quote` buttons throughout the website.


## Features
The main feature I am showcasing in this website is the `CRUD` Functionality. 
The `postres database` and the admin backend sections.
The E-commerce Shopping Cart with `Stripe` features.
The `Form` Pages using The *POST* request method 
    - allows user to post infomation to the server,
    - by specifying the *POST* method on the form element and handling it on the backend.
The pages consist of the following:
* List of products and services page **(‘Read’)*
* These pages display the products in the database. (this being on home-page *Product Management Section*).  
  Accessed via a superuser with staff status given credetials from the *IAM* users at *AWS* where username/ emails and passwords are verified and stored.  
  This is also accessed via the Users page on the built in *django-backend admin-pages*.
* The *add_product* *(Add a product)* page which displays the form allows the user to add a new product and service to the database together with an image field and category and sku for identification purposes. 
* The *edit_product* page *(‘Update’)* page enables the user to update the text and the image field on the database.
* A page to edit an existing and update existing products. This format is exactly the same as the *add product* page, except this time, 
  the form is pre-populated with values belonging to the product or service being edited.

Each Product or Service listed on the `home` page has an *edit button* that links to the `home` page.
Delete link for each product *(‘Delete’)*
Each product form (on the Product-Management link accessed via dropdown on the home page) has a *delete_product* button that links to the `delete view`*.

_*Please note :- In the *insert_product* function I have copied and tried to modify the *insert_product* imagefield 'custom-clearable' in order to insert and upload the images from an external computor.  
  Unfortunaley, I have not had much success as some images work on the uploading image section and others may not. I consulted tutors and they suggested I revisit the AWS section of the course. 
  Please note this issue only occurs on the deployed heroku site. Add the products and the image fields. I have since leaned that I need to check all image-names are in sync with each other from Gitpod through Github 
  and finally to Heroku and chiefly the AWS bucket which stores the image needs to be able to grab the correct URL. I still have not mastered this as reflected on the website.

-----///--- All the below code (I have selected the first sample code from the `all-products` section)from `products views` is attributed to **Boutique-Ado and its owner Chris Zielinski** -----///---

    def all_products(request):
        """ A view to show all products, including sorting and search queries """

        products = Product.objects.all()
        query = None
        categories = None
        sort = None
        direction = None

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, 
                                "Please enter search criteria!")
                    return redirect(reverse('products'))

                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
        }

        return render(request, 'products/products.html', context)


    def product_detail(request, product_id):
        """ A view to show individual product details """

        product = get_object_or_404(Product, pk=product_id)

        context = {
            'product': product,
        }

        return render(request, 'products/product_detail.html', context)

    I have attributed this in the credits section below.*_

## Deployment

#### Github commands used in this project:
```
git add .
git commit -m "final commit"
git push
git log
git reset

To revert to a previous commit - example below:

 commit ab202accf6e25351084a8a05b3d70a1ac71cd5f7 (HEAD -> master, origin/master, origin/HEAD)
 Author: Sara Oliver <s.oliver1@icloud.com>
 Date:   Wed Sep 30 23:12:48 2020 +0000

```

#### Deployment to Github
* Make sure the branch or folder as a publishing source exists in the repository. Example, before  publishing project site from the /docs folder on the master branch of that repository, 
  Collaborator must create a /docs folder on the *master* branch of that repository.
* On GitHub, navigate to site's repository.
* Under repository name, click  Settings.
* Under "GitHub Pages", use Source drop-down menu and select a publishing source.
* More information found on Github:
  https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

#### Cloning a repository to GitHub Desktop
I clone one of my Boutique Ado to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  

###  Basic set up for my project and libraries
*(see *CRUD functionality notes further down page*)

 * https://validator.w3.org/ *

  `https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template`

```
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

    AUTHENTICATION_BACKENDS = [
```
##### Need to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

##### `allauth` specific authentication methods, such as login by e-mail
 ```   
    ['allauth.account.auth_backends.AuthenticationBackend',
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
            -This copies or the allauth templates in the packages so they can be styled.
          
   1.   Getbootstrap.com > go to documentation and copy the starter template 
```    
#### Font stories  
        *About Montsaratt and Roboto*

        <addr> **Montsaratt** copied from Googlefonts: https://fonts.google.com/specimen/Montserrat#about

        Old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to design this typeface and rescue the beauty 
        of urban typography that emerged in the first half of the twentieth century. 
        As urban development changes that place, it will never return to its original form and loses forever the designs that are so special and unique. 
        The letters that inspired this project have work, dedication, care, color, contrast, light and life, day and night! 
        These are the types that make the city look so beautiful.
        The Montserrat Project began with the idea to rescue what is in Montserrat and set it free under a libre license, the SIL Open Font License.

        This is the normal family, and it has two sister families so far, Alternates and Subrayada. Many of the letterforms are special in the Alternates family, while 'Subrayada' means 'Underlined' in Spanish and celebrates a special style of underline that is integrated into the letterforms found in the Montserrat neighborhood.
        </Addr>
        *Roboto* has a dual nature. It has a mechanical skeleton and the forms are largely geometric. At the same time, the font features friendly and open curves. While some grotesks distort their letterforms to force a rigid rhythm, Roboto doesn’t compromise, allowing letters to be settled into their natural width. 
        This makes for a more natural reading rhythm more commonly found in humanist and serif types.

        This is the regular family, which can be used alongside the Roboto Condensed family and the Roboto Slab family.
        <addr>font-family: 'Montserrat', sans-serif;</Addr>
        <Addr>-family: 'Roboto', sans-serif;</Addr>

        To contribute, see github.com/google/roboto*
1.  <addr>  The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to design this typeface and rescue the beauty of urban typography that emerged in the first half of the twentieth century. 
            As urban development changes that place, it will never return to its original form and loses forever the designs that are so special and unique. The letters that inspired this project have work, dedication, care, color, contrast, light and life, day and night! These are the types that make the city look so beautiful. 
            The Montserrat Project began with the idea to rescue what is in Montserrat and set it free under a libre license, the SIL Open Font License.
            This is the normal family, and it has two sister families so far, Alternates and Subrayada. Many of the letterforms are special in the Alternates family, 
            while 'Subrayada' means 'Underlined' in Spanish and celebrates a special style of underline that is integrated into the letterforms found in the Montserrat neighborhood. 
            Updated November 2017: The family was redrawn by Jacques Le Bailly at Baron von Fonthausen over the summer, and the full set of weights were adjusted to make the Regular lighter and better for use in longer texts. In fall, Julieta Ulanovsky, Sol Matas, and Juan Pablo del Peral, led the development of Cyrillic support, with consultation with Carolina Giovagnoli, Maria Doreuli, and Alexei Vanyashin.

            The Montserrat project is led by Julieta Ulanovsky, a type designer based in Buenos Aires, Argentina. To contribute, see github.com/JulietaUla/Montserrat
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,400;1,100;1,200;1,300;1,600&family=Roboto:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
            CSS rules to specify families

            font-family: 'Montserrat', sans-serif;
            font-family: 'Roboto', sans-serif;</addr>
            python3 manage.py runserver to run the django server and test
    </addr>
#### Deployment to Heroku
Kindly given to me via Anna Greaves(tutor)as I had trouble logging in with previous commands.

#### First we:
 npm install -g heroku

Then, to login, use the command:
heroku login -i * 

#### Clone the repository
Use Git to source code from local browser.
(e.g. GitHub Pages or Heroku).
When trying to deploy my project to Heroku I hit a bug *- AttributeError
AttributeError: 'NoneType' object has no attribute 'categories'*

To resolve this I ...
Different values for environment variables (Heroku Config Vars)?
Different configuration files?

$ heroku git:clone 
Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

#### Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
```
$ git add .
$ git commit -am ""
$ git push heroku master

```

**Template Inheritance** I use the *Inherits* code, creating *base-template and using {% extends "base.html" %} to pass to a child template*.
 also {% load static %} to load static variables and {% block content %}{endblock} 
>(1) Static data items:
>Those data items whose extents lasts as long as the program execution time; such data items have manifest constant Lvalues. Every static data item must have been declared either in a function or routine definition, in a global declaration or as a label set by colon.
>— The BCPL Reference Manual, 7.2 Space Allocation and Extent of Data Items
>     https://en.wikipedia.org/


**Passing Data from View to Template**  A very useful feature of using frameworks to actually set data on the server side and get it coming through to the client.
Benefits of using frameworks is the fact that we can actually get server-side code to provide the frontend with data. 
Example:- Go to *apps.py*. Then add argument page_title=

```from django.apps import AppConfig

class HomeConfig(AppConfig):
    name = 'home'

    ** Views return in services app: **

def our_services(request):
    """ A view to our services page """

    return render(request, 'services/our_services.html')


def brands(request):
    """ A view to brands page """

    return render(request, 'services/brands.html')


def about(request):
    """ view to return the about page """

    return render(request, 'services/about.html')
```

**Reducing repetition**  using the *{% %} notation* template tags for statements (not for expressions).
allowing us to use a *for loop* inside our HTML.  Standard Python *for loop* for number in list_of_numbers.
and then need to supply an {%end for%} so that the templating language knows where the *for loop* stops.
Example:- 
{% for number in list_of_numbers %}
    <p>{{ number }}</p> 
{% endfor %}

**The if template tag**
I use `if` statements inside my template. By using the example here:
 {% if some_condition %} tag and the closing {% endif %} tag. 
See this in action by going to *About* section of website.

**Getting Themes**  I have chosen **Bootstrap4** as the main theme for my project together with **Start bootstrap theme *Clean Blog* as featured in *CI lessons on Flask Framework* in my *Services App* for a multi-page website. 
I download the theme by copying the link then go to terminal and mkdir, then cd into it and wget the https://startbootstrap.com/themes/clean-blog/
I then style accordingly.   Unzip package with the *unzip gh-pages.zip* command.

## Existing Features - C.R.U.D. - allows users to add all_products to store in database, by having them fill out the form.
*CREATE - Add the product by following the instructions to *CHECKOUT* store.  Details can be inserted and stored in a form (which can also be accessed via admin) to my *Profile* for convenience and to view purchase history.
	   Form includes: Name , description of products/service, address, purchases history.  All this useful data is being populated on the database backend for admin.

READ -    Read through and view all the the products in the category as a collection or view each product individually by clicking buttons. 
Administrator - log in required - sample code used in my project views copied and slightly modified from the excellent *Boutique Ado* project.
```@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 
                       'Sorry not allowed - authorised personel only.')
        return redirect(reverse('home'))
```


EDIT &
UPDATE -  Click the button to edit the page and follow the instructions there.  Then click the UPDATE button 															to save changes.  Then return to 	   Home page to add another recipe by clicking the CREATE BUTTON again.

DELETE	  Press the delete button to undo changes.  

Another great feature which I really like is the **custom clearable images** in `widgets.py in products app` for adding images to CHECKOUT and visually seeing what you are about to purchase. Removing from the bag
if buyer changes their mind.
```from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
```
					
### Features Left to Implement:
			* Search box to search the website packages and products in a more cohesive and timely manner
			* Sort code to sort through products and website categories
			* Login form with password so users sign in securely using the password to access the database.	- DONE
			* More links to other companies specialising in our products and services. 	* Links to other specialised SERVICE sites appropriate to this website.
			* Contact Forms and social media to sign up for newsletters.
            * Gallery of website examples and webpackages to view for visual impact
			* Another possible  feature to be incorporated is to be able and rate the products and services we offer. - DONE
			* Social media and blogs
			* Chat page / Forum
            * Zoom and Live Streaming for consultations with potential and existing leads / clients
            * Introduce a favicon to my website
#### Libraries / requirements used in my project:
```
asgiref==3.2.10
boto3==1.14.46
botocore==1.17.46
dj-database-url==0.5.0
Django==3.1
django-allauth==0.42.0
django-countries==6.1.2
django-crispy-forms==1.9.2
django-forms-bootstrap==3.1.0
django-storages==1.9.1
docutils==0.15.2
gunicorn==20.0.4
jmespath==0.10.0
oauthlib==3.1.0
Pillow==7.2.0
psycopg2-binary==2.8.5
python3-openid==3.2.0
pytz==2020.1
requests-oauthlib==1.3.0
s3transfer==0.3.3
sqlparse==0.3.1
stripe==2.50.0
travis==0.0.3
whitenoise==5.2.0
```

#### Links to libraries
	
*	https://pypi.org/project/Flask-Bootstrap4/

*	https://www.fullstackpython.com/flask.html

*	https://flask.palletsprojects.com/en/1.1.x/

*	https://www.mongodb.com/cloud/atlas

*	https://www.python.org/

*   https://jsonformatter.org/


 1.  ```alt + up/down arrows to move a line or block of code up or down
        alt + click` to select multiple regions
1.      
1.   pip3 install django-crispy-forms 
     pip3 install django-crispy-forms
     ```
 
##  Deploying to heroku
  
1.         ```pip3 install pip3 install whitenoise
           pip3 install gunicorn  
           ```

1. ` echo "env.py" >> .gitignore `
    ` nano .gitignore ` to check that the file is still there (then exit out) by pressing enter 
1.          `git status ` 
   1.  To check heroku logs on the gitpod terminal:
       follow these steps f you quit the server with Ctrl+C then type
    1.  `heroku login -i`
    1.  `heroku config:set DISABLE_COLLECTSTATIC=1 --app kuk-milestone-4`
        and sign in, then run:
        heroku logs --tail -a kuk-milestone-4`
        Go to AWS login and create a bucket then the bucket policy and the user'
        S3 and then to IAM 
        pip3 install django dj-database-url
        pip3 install boto3
        pip3 install django-storages
   1.  
### JQuery and Java Script 
The project uses JQuery to simplify DOM manipulation.
Java script for forms and validation. 

### Testing - see bugs and fixes below
* https://validator.w3.org/nu/#l118c6 - There is further testing wihich needs addressing. 
127.0.0.1 - - [20/Mar/2020 12:05:52] "GET /get_categories HTTP/1.1" 500 -
Encountered:
* 505 error indicates a temporary problem, and sometimes that problem is very temporary. A site might be getting overwhelmed with traffic, for example. So, refreshing the page is always worth a shot. Most browsers use the F5 key to refresh, and also provide a Refresh button somewhere on the address bar. It doesn’t fix the problem very often, but it takes just a second to try.
* Firefox / Chrome / Edge / - All appear to be working as so are the links.


### BUGS  I encounted:-  
To be honest, I encountered many challenges on this coding journey, too numerous to mention here, as I have no time left.  All I can convey is that I am grateful to the 
Tutors who gave me ideas, pointers and all the trouble shooting tips included in the course as well as asking questions on Slack and looking for solutions on *Slack and https://stackoverflow.com/ . 
Although challengeing it required me to stretch my mind and I hope that I have the skills and resources to carry on with the profession in some shape or form in my business ventures.
Below are some of the challenges I encountered in my project:-

####  Export  DATABASE_URL in Gitpod - very important!
        export DATABASE_URL="Paste your PostGRES connection string in quotes"
        then make your migrations
        then loaddata
        You have to migrate *before* your load other wise the database is never created.       
    1.  I had an issue with the above not being able to deploy properly to heroku because I did not follow 
        the above procedure and therefore it did not create the database.  I tried resetting the databse and destroying it but it was a simple
        procedure above that fixed it in the end.  I consulted a tutor who made me realize the steps that I had missed.  This was
        an experience I shall not forget in future.  
        *Needed to login by username in Django admin, regardless of `allauth`*
    
#### Further info on Bugs
I have been unable to **categorise my website Packages and Products** properly hence the searches are not as effiently organised as they should be. As a result, 
I broke my website twice because of trying to completely modify and change my json codes. I aldo had to reset both my squilite and postgres databases which I now am most proficient at doing.
I have henceforth reverted back to my original products code which closely if not directly resembles the Boutique Ado products code (which I have attributed several times throughout). 
My confidence is such that I had to follow very closely the project to create a viable project of my own. I trust my confidence and proficiency levels will increase with practise over time.
I have enclosed several pages of README notes in my `Readme` folder inside my `Mockups` folder which can be accessed for future reference and for the Accessors' perusal should they so wish.


Slack community - *various borrowed code snippets* See below credits. I often change them
                     when some of the code did not work for me.  However it did
                     lead me on to thinking again about seeing a line of code highlighted in an error I had been seeing, and checking at the bottom of my jinga codes for these errors.
                     This experience gives me more confidence to debug code.
### More Bugs and Problems I encountered whilst building this website:

#### Merge isssues 

I had two websites going simultanously as I built this website mainly when one failed me I would go with the other one.  But I found out that perhaps this is not such a good idea as when it came to merging the websites
to the master, I encountered *merge issues*.  I have done this procedure on my past websites and have not had much of a problem with merging but this time I did.  This is probably due to the complexity of the 
website which I guess I shoud have realised.  I did try the following code to debug from the C. I. Troubleshooting tips:

>>If you’re stuck in an editor, don’t panic -
Less - “less” is a pager program that may automatically open on the command line whenever you ask to read a very long file or output (e.g. when using “git log” on a repository with lots of history).
You can use the arrow keys or the page up/down keys to scroll around in Less. You can also use the “/” key to search for a specific part of the text and the “n” key to go to the next match.
Use the “q” key to quit Less.
>
#### Explantion given to me when I queried steps in a procedure that I knew off by heart....
 .... 
 and still encounterd issues in my accounts login programatic error 
 
 >*ProgrammingError at /accounts/login/
relation "django_site" does not exist
LINE 1: ..."django_site"."domain", "django_site"."name" FROM "django_si...
                                                             ^
Request Method:	GET
Request URL:	https://kuk-milestone-4.herokuapp.com/accounts/login/
Django Version:	3.1
Exception Type:	ProgrammingError
Exception Value:	
relation "django_site" does not exist
>LINE 1: ..."django_site"."domain", "django_site"."name" FROM "django_si...
-----
"So the simplified explanation is that the secret key which is used the encrypt and decrypt data had been changed between migrations and the database getting updated. So data being sent to and from the database were different than expected.  Django stores a whole bunch of details about itself in the database and between the keys this ultimately got django tripping up on itself because it thought it was getting information for 2 different websites  (which can cause bigger issues, we got lucky).  
So we need to keep the secret keys the same.  The only time we should change the secret keys is once.  And that is if we are changing connecting to a different database.  
Once sorted with the issue in Django so the keys were correct, we then reset the database to a blank clean one."   Something to remember in future. 
*Credit goes to Stephen - Tutor at C. I. Thank you.*
###### Reset my squlite database
   1. I had to reset my local squlite database at one point due to migrations issues so I:
        need to delete the db.sqlite3 file locally in the root level of my project, 
        then I had to go into each of my apps that have a migrations folder, and delete all of the files inside the migrations folder, except for the __init__.py file.
            I then had to run the two commands again:
            `python3 manage.py makemigrations`
            `python3 manage.py migrate`
        This should reset my database. 

   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
         
#### Media
Some of The photos and credits obtained and used in this site were obtained from *Spectator Shop ...*
e.g. media - https://shop.spectator.co.uk ; https://Kaggle.com 
Other media images via my monthly subcription to ADOBE STOCK - https://stock.adobe.com/

#### Acknowledgements
I received inspiration for this project from:- 

- "*The Spectator* - https://shop.spectator.co.uk/ 
-  the colour of my buttons are attributed to Spectator Shop
-   Brian Machira - *CI Mentor*
- Stephen from C.I. Tutor for trouble shooting databases
- New Tutor from C. I. - Johann for trouble shooting image URLs on my website
- Slack community - *various borrowed code snippets* which I then modify to suit my purposes, although
                     some of the code did not work for me I had to rethink how to improve this.  
                     It also gives me extra confidence to debug code.  

####  Further CREDITS AND ACKNOWLEDGEMENTS

#### CREDits and  ACKNOWLEDGEMENTS  (Other website acknowledgemnts)       
1.  The whole website code was copied from conception to completion and NOT Cloned.   
Each page was copied and modified to suit the purposes of my website, 
    from the *Code Institue(C. I.) Fullstack final e-commerce website*.
    Other ideas and layouts came from my previous milestones:-
     Cook Corner(3) 
     and 
     Procol Harum(1) which in turn were also based on the excellent C. I. mini projects and websites which I acknowledge in  my previous merits and acknowledgements.
     Thorin and Company and 
     Putting it altogether mini projects.

     And product information:
     Boutique Ado and Kagglec.om
     And  `http://Spectator.co.uk` 
     and colour red touches and buttons-colour-scheme: #d30037;  

### Further ACKNOWLEDGEMENTS and all  Credits go to *ckz8780 Chris Zielinski* who created the excellent *Boutique Ado Website*.
1.      Most of the products are taken from the C.I. dataset which originates from https://www.kaggle.com/  and modified to suit the purpose of this website.  
        I do not claim to make the code from this website my own. But I did build this website from conception to completion in an effort to understand the process more clearly.
        Any intention to pass off any code as my own was and is purely unintentional.
1.      The Slack Community for any questions queries and for helping out whenever I need it.
1.      Products and fixtures credits images 'Tailor Brands https://studio.tailorbrands.com/ : 
        *Brand-book-1_VvE5VhU.webp*, *Business-deck-1-1 (1).webp*, *Business-deck-1-1 (1).webp* 
        Also branding and marketing ideas are based the Tailor Brands website.
1.      New Products all credits go to: Cool wine accesories and branding image and copied text credits from https://www.igopromo.co.uk/
1.      New Products all credits go to: https://www.igopromo.co.uk/inspiration-pages/sustainable-products/bandana-rpet-multi-functional-scarf-all-over-printing/p4348-master    
1.      Other website Ideas and inspiration - https://www.walkeragency.co.uk/workThan
1.      The fantastic tutors for their unvaluable assistance and 
1.      Student Care for being so encouraging when I felt like giving up at times.
1.      Finally my Family deserve a mention for supporting me whilst I did this course and for that I thank you for being there.       
1.  
1.    * Product app Tutor suggestions from support Tutor*
1.     *Given to me by Kevin at C.I. tutor support* 
1.      The easiest fix would be to empty your DB on Heroku: https://stackoverflow.com/questions/4820549/how-to-empty-a-heroku-database
        Then export the products from your local project to a fixtures file (Django can create the JSON files automatically for you):
        python manage.py dumpdata products.product --indent 4 
        Also django documentation:             
1.      django documentation: creating forms for the database:
        https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields
1.      
1.                     
1.      Stephen and Johann for assisting me in successfully renduring my image urls eg. 
        https://kuk-milestone-4.s3.amazonaws.com/media/image-name-here

        https://kuk-milestone-4.s3.amazonaws.com/media/image-name-here
1.          
		     
## Conclusion	     
Overall I feel satisfied with my project and enjoyed creating it despite numerous issues along the way.  
It was certainly challenging but I think the effort was worth it.  I am looking forward to the next chapter.

** Thank you to all! **
 
 *This website project is for educational purposes only*
