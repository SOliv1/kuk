 ## Toasts 
    https://getbootstrap.com/docs/4.5/components/toasts/

 1.         Inside the main templates/includes folder let's add an additional subfolder to contain all the toasts
                    These toasts will be small HTML snippets that will pop up when a user performs an action
                    such as adding something to their shopping bag.
                    success toast inside a file called toast success.html.
                    structure for this comes from the bootstrap documentation.
                    start by just pasting it in from the completed project.
                    Almost everything here is straight from bootstrap. With the exception of our custom toast class.
                    -two divs at the top will just add a little extra visual touch to the top of the notification.
                    -toast is organized into a header and a body.
                    -header has a heading on the left and a close button on the right.
                    - data auto-hide and data dismiss attributes are required
                            to prevent auto-hiding the notification after a few seconds.
                            And instead, give the user the ability to dismiss it on their own.
                    -In the body of the toast is the message template variable.  going to be included in the message container in the base template.
                        - first copy this code and create a similar one
                        -for errors warnings and info using the standard bootstrap classes.
                        -copy the exact same code into three appropriately named files.
                        -And change the relevant classes.
                        -one toast error. And it will use the bootstrap danger class to make it red
                        -this one toasts info.  use the info class.
                        -this one toast warning. Which will use the warning class.
                        -save and head to base.html.
                        - find the message container toward the bottom of the page.
                        -inside  message container, we'll want to iterate through any messages
                        -sent back form the server and render one of these includes.
                        -(to demonstrate just include includes/toasts/toasts_success.html
                            and then go to the add to bag view in the bag app)
    1.  import the product model and also the messages framework
                        from Django.contrib here at the top.
                        - to demonstrate how these messages will work.
                        - first get the product at the top of the view here.
                        - then use the messages dot success function.
                        -to add a message to the request object.
                        -and use some string formatting to let the user know they've added this product to their bag.
                        - next piece of the puzzle is to use the bootstrap JavaScript to show the toast.
                        -which can be done in the post loadjs block of base.html.
                        -all have to be done is add a little JavaScript. To call the toast method from bootstrap. With an option of show.
                        -on any elements with the toast class.
                        -by putting this in the base HTML template will ensure that every page that loads
                            will immediately call the show option on all toasts that have been rendered in the messages container
                        -this also explains why for all this time we've been including block dot super in
                            our templates when overriding the post loadjs block.  we ensure that any JavaScript we've written in the templates that extend this one
                        -this will ensure it won't overwrite this call to show all the toasts.
                        -last - add one more setting to *settings.py* to tell it to store messages in the session this is
                                often not a required step because there is a default which falls back to this
                                storage method but *NOTE - due to the use of git pod in these recordings it's required
##  checkout                         for us*
1.  python3 manage.py startapp checkout

    1. go to models.py and add the appropriate code 
        add the app to the settings.py
        'python3 manage.py makemigrations --dry-run' 
        pip3 install django_countries to add the countries to the checkout form
    1.  python3 manage.py makemigrations
        python3 manage.py makemigrations --dry-run
    1.  python3 manage.py migrate
    1.  python3 manage.py loaddata categories
        python3 manage.py loaddata products
    1.  fill out models.py then views.py then urls.py then project level urls.py

    1.  mkdir -p products/templates/products
    1.  create a products.html inside the products directory


    
##  Shopping bag
1.      python3 manage.py startapp bag  
        and add bag app to settings as well
   1.   go to views.py and add to that
        then create urls.py in bag and add paths to that
        followed by update paths in urls.py project
        section 
        then context.py in bag app
        then in settings.py in context list of processors -  'bag.context.bag_contents',
        
   
   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
            
1.          
1.  stripe:
    export STRIPE_PUBLIC_KEY=pk_test=""
    export STRIPE_SECRET_KEY=sk_test=""

    export_STRIPE_WH_SECRET= ''

            test card no = 
            4242424242424242
    second test card no. to trigger the overlay spinner:- 
        test card spinner:- 4000002500003155
    -   to test the integrations for stripe payments and the spinner overlay.        
  
## Services app

### Contact html 
Forms to send to the backend - The GET method-used for retrieving data from the server. 
                             - The POST method used for sending data to the server.