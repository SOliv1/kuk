  ##    Add Products to Product App
        `jsonformatter.org`

        python3 manage.py startapp products

            Add to installed apps in settings.py mkdir products/fixtures

            Add categories and products json https://jsonformatter.org/ to validate
            -Required fields are name; description; price.  Everything else is optional.
            -Go to models.py and add code There - python3 manage.py makemigrations --dry-run

            pip3 install pillow or 
            python -m pip install pillow

            dry run again...

            python3 manage.py migrate --plan

            python3 manage.py makemigrations

            `python3 manage.py migrate`
             then... -
            `python3 manage.py loaddata categories`
            `python3 manage.py loaddata products`

            check it out - python3 manage.py runserver - go to admin


  1.  1.          copy our project-level urls.py
                        Create new file in the *home app*, called *urls.py*
                        And paste it in to use as a shell
                        take out 'include' here.
                        And add one empty path to indicate that this is the route URL.
                        to render views.index. With the name of 'home'
                        then 'import views' from the current directory here at the top.
                        save that.
1.          go back to the *project level URLs file* and include the *home URLs*
                        The very last thing we need to do is add the 'home app' to installed apps in 'settings.py'
                        And then wire up our template directories.
                                Add home to installed apps
                                And then add both the route templates directory.
                                And  custom allauth directory to the template dirs setting
                                With that finished save and test it out
                                start up the development server.
                                Open the project.
                                And we land on our home page with it works, rendered in the correct bootstrap styles.
                                Stop server and commit the changes "add home app and templates"
1.          set up the *products app* - load in some products.
                                start by copying in the collection of product images.
                                Pruned these from a data set at `kaggle.com` which is a great provider of
                                free sample data for use in all sorts of industries.
                                create the products app using python3 manage.py *startapp products^
                                *python3 manage.py startapp products*
                                add this app to installed apps in settings.py
                                make a folder called fixtures inside the products app
                                drag and drop a couple of JSON fixture files in there,
                                one for categories and one for products
            python3 manage.py startapp products
## Add Products and fixtures

1.          Add to installed apps in settings.py mkdir products/fixtures

                                Add categories and products json https://jsonformatter.org/ to validate

                                Go to models.py and add code There - python3 manage.py makemigrations --dry run

                                pip3 install pillow
                                `python -m pip install Pillow`

                                dry run again...

                                python3 manage.py migrate --plan

                                python3 manage.py makemigrations

                                python3 manage.py migrate then... -python3 manage.py loaddata categories python3 manage.py loaddata products

                                check it out - python3 manage.py runserver - go to admin

## products admin
                                mkdir -p products/templates/products

                                file = products.html

1.          we're creating that inner products directory to make
                                sure that django knows which app these templates belong to.
                                In case any of them end up having the same names as other templates.
                                And let's now create a products.html inside that directory.
                                And copy the content of the home template in as a shell.
                                The products template will still extend base.html
                                And will still require static files as well as the page header
                                python3 manage.py runserver 

##  Product Details
1.                  starting with main nav.html let's add url products for this link. And then we'll add the same here on the shop now button in index.html. To create the product details page we need a new view which will take the product id as a parameter and return the template including the product, this will be almost identical to the all products view so I'll copy that as a base.
                    Shopping cart
                    python3 manage.py startapp bag

                    add to settings: installed apps bag

                    add views.py by copying and pasting the views from home and changing the wording to the appropriate views.

                    create urls.py and add to the bag directory - copy and paste from home urls and add as appropriate urls code.

                    And then include the bag URLs in the project level URLs file.

                    head over to base template Add the link to view the bag.

                    head over to mobile-top-header Add the link to view the bag in there too.

                    python3 manage.py runserver

                    add contexts.py

                    commit changes

                    alt + click to select mutltiple regions
                    when making changes to the model make sure you do the following to check all is correct: python3 manage.py makemigrations --dry-run
## Add sizes to products via shell:

                    **products/migrations/0002_auto_20200605_0009.py**

                    Change Meta options on category
                    Add field has_sizes to product The above report is technically a bug in django but because it is not critical developers have chosen not to fix it as it could cause other issues along the way. So it is ok to go ahead and make migrations
                    python3 manage.py migrate --plan to verify the migrations we are making

                    and then python3 manage.py migrate
### python shell
                    python3 manage.py shell

                    input into the shell for quick 'on the fly' without having to resort to your views.py

                    python3 manage.py shell

                    input into the shell for quick 'on the fly' without having to resort to your views.py

                    from products.models import Product

            kdbb = ['kitchen_dining', 'bed_bath'] clothes = Product.objects.exclude(category__name__in=kdbb) clothes.count() 
            for item in clothes: 
            item.has_sizes = True 
            item.save()
            press enter again
            Product.objects.filter(has_sizes = True)

            Product.objects.filter(has_sizes = True).count()

            130

            exit()

## Adding Products part5

1.          Attach some plus and minus buttons to this input to make it easier to use on mobile.
            JavaScript handles updating the input box itself. Since these buttons won't do anything by default.
            write that JavaScript right now. do it in an include since we'll also use it on the shopping bag page in the next video.
            Create an includes directory in the products template folder.
            And then an html file which I'll call quantity_input_script.html I'm doing this as an HTML file since it'll just be a script element we include at the end of the product detail template And this avoids having to deal with additional static files just for a single JavaScript file.
            Let's begin script to increment the quantity.
            Adding Products part6
                add the *quantity selector box* to the shopping bag pages quantity column.

                replace this quantity in the *table with a form with a method of post*.
                It won't have an action yet since we haven't created the *proper URLs or views*
                but we'll get to that soon.
                I'll give it a *class of update form and attach the csrf token since it'll be posting data*.
                And from here it's as simple as copying the form group from the product detail
                page and pasting it in.
                And now we'll make a few changes to it.
                -   First I'll get rid of the 50% width class.
                -   Add some classes to make the icons buttons and input boxes a bit smaller.
                -   And I'll remove the icon class here in the span element
                -   which will allow Font awesomes fa-small class to handle the sizing.
                -  nstead of the icon class we copied from Bulma in the beginning of this project.
                -   need to update all the template variables that contain product.id to item.item_id
                    Also, let's change the value of the input box
                    to reflect the number of this item currently in the shopping bag.
                    Finally because there's no size selector box on this page.
                    We'll need to submit the size of the item the user wants to update or remove in a hidden input field.
                    If the product does in fact have sizes.
## Adjusting and Removing Products Part 1

1.      go to bag views and copy and paste for views in bag dir.  Adjust as required for the adjustment & removal of products
            -   views.py
            -   add URL for it
            -`  shopping bag template submit item to the adjust bag view
            Adjusting and Removing Products Part 2
            -   get jquery code  in minified form here from codejquery.com
            `       'https://code.jquery.com/'

            -   *new folder in bag directory called templatetags/bags_tools.py*
            -   
            -  *new __init__.py new file to accompany the template/bags_too
            ## Checkout

            python3 manage.py startapp checkout Add to the models.py in the checkout app and then dry run the applications to be created. python3 manage.py makemigrations --dry-run then python3 manage.py makemigrations then python3 manage.py migrate --plan to make sure we are not missing anything then finally actually run them: python3 manage.py migrate
            Let's commit these changes with git add . git commit -m "created check out app and models" git push
## Create models

            > https://github.com/django/django/tree/master/django/db/models
            Create Forms django documentation:
             https://docs.djangoproject.com/en/dev/ref/forms/fields/#django.forms.ImageField
            >
#### Create models.py

            https://github.com/django/django/tree/master/django/db/models

            Admin, Signals & Forms Part 1
            Add to admin.py first import the order and OrderLineItem models - check it out in the admin on site. Create signals.py in the same level as models.py in checkout. Update the apps.py in checkout. Then add . and commit changes.

            views and templates
            create views and save then create a new urls file by copying from home app and modifying it. go to product level urls and include check_out.urls. -create new templates folder and checkout folder inside it and check_out.html inside that. -then create css. Add static folder inside checkout app then check_out folder inside that then finally a check_out.css inside that. install django crispy forms to format forms using bootstrap styling forms automatically.

            pip3 install django-crispy-forms
        

            then add `crispy forms`, to our installed apps in 
            `settings.py`, and tell it what template pack it is bootstratp4 in this case.
            add a list called built-ins which will contain all
            the tags we want available in all our templates by default.
            from crispy_forms.template_tags we want to add both crispy_forms_tags
            And crispy_forms_field.
            Which will give us access to everything we need from crispy forms across all templates by default.
            Then update `requriements.txt`
            `pip3 freeze > requirements.txt`
            Now with that done, render the form in the checkout template.
    1.  