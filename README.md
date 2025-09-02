# codestar_blog

### ERD / model plan
- Model name: About
- Fields:

1) title - CharField - for the heading
2) content -TextField - for the main text
3) updated_on - DateTimeField - to show when it was last updated

- - -

### Commands / Note, run 
- Python3 manage.py startapp about


### files in the app

- models.py - create the About model

- admin.py - register the model so admin can edit it

- views.py - add the function for About page

- urls.py - add the path for the page

- templates/about/about.html - the template file


### project changes

- settings.py - add 'about' to INSTALLED_APPS

- project urls.py - include about.urls with path("about/",)

- base.html - add a link in the navigation bar to the About page

