**URL of PWS Deployment:**

http://rayienda-hasmaradana-cherrystore.pbp.cs.ui.ac.id/

<details>
<Summary><b>Assignment 2</b></Summary>

Questions and Answers
1. Explain how you implemented the checklist above step-by-step (not just following the tutorial)

**Project Implementation**

Creating a new Django project
- made a new directory `cherry-shop` for this project.
- activated virtual environment on the directory `cherry-shop` to avoid Python version conflicts with the command:

```
env\Scripts\activate
```

- made a new file `requirements.txt` and filled it with the following:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
and installed them with:
```
pip install -r requirements.txt
```

- Initialized the project with:
```
django-admin startproject cherry_shop .
```

- after the project is installed, I added `"localhost"` and `"127.0.0.1"` as a part of the list `ALLOWED_HOST` in the file `settings.py`


- Creating an application `main` in the project

- Made a new app `main` with command:
```
python manage.py startapp main
```
- Make the Template

After the app main is installed, I added `main` to the `INSTALLED_APPS` in the file `settings.py`.

- Made a new directory `template` inside the directory `main` and created a new file `main.html` as a template, and filled `main.html` with placeholder fields `{{ application_name }}`, `{{ name }}`, and `{{ class }}` where the context will be later provided by `views.py`.

- Made the model Product in `models.py` with the attributes name, price, and description.

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

- After the main HTML is done, I created a function `show_main` in `views.py` that will give back response as an HTML template that shows the name of the application, my name, and class.

```
from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'cherry-shop',
        'class': 'PBD KKI',
        'name': 'Rayienda Hasmaradana',
    }

    return render(request, "main.html", context)
```
URL Configuration
- Made the file `urls.py` on the directory `main` for routing the `show_main` function in `views.py` to `urls.py` and filled it with:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- Then configured `urls.py` on the directory `cherry_shop` and filled with:
```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

]
```
Git & PWS Deployment
- Made a new repository in github and connect it with my local repository.
- After connected, I did the command `add`, `commit` and `push` to push the changes to the remote repository.
- For deploying to PWS, I created a new PWS project named `cherrystore`, then added this to the list `ALLOWED_HOST`:
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "rayienda-hasmaradana-cherrystore.pbp.cs.ui.ac.id"]
```
and push to PWS repository for the deployment.

2. Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

![alt text](pbp_diagram.png)

3. The use of git in software development

Git works as the Version Control System that allows developers to track every changes in their code, and allows them to store their projects in remote repositores such as Github or Gitlab, developers can also collaborate with other developers as a team in the same project.

4. Why is Django used as the starting point for learning software development?

Because django supports rapid development and follows practices like the MVT architecture. It allows beginner developers to understand fundamental concepts like routin, templating, and database management without having to worrying about more codes. Django also has large and well-organized documentation, making it easier for beginners to find information and learn how to use the framework effectively. 

5. Why is the Django model called an ORM?

Because they map python objects to relational database, providing an abstraction layer that simplifies database interaction. ORM abstracts interactions with the database, making it easier to manage data and keeping code consistent and easy to understand.
</details>

<details>
<Summary><b>Assignment 3</b></Summary>

## Assignment 3 - PBD
---
 ### Explain why we need data delivery in implementing a platform.
 Data delivery is important because it supports accurate and timely information flow accross many components of the platform. This improves the platform's functionality and user experience while enabling real-time interaction and decision-making. Without it, the data needed to perform various operations can't be exchanged properly and the platform won't be able to function optimally.

 ### In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
 In my opinion, JSON is better, also it is more popular than XML because of its efficiency compared to XML. JSON also has simpler syntax, and JSON is integrated with JavaScript, making it to easier to implement on web applications.

 ### Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
 `is_valid()` in Django is used to validate data thats included in the form. This method checks if the data submitted by user is in the correct format. If it is valid it will give the result `True` and the data will be processed, if not it will give back `False` and user will get an error message. This method prevents users from submitting invalid data that might lead to errors and may result in security risks.

 ### Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
 `csrf_token` is used to protect web applications from CSRF (Cross-Site Request Forgery) attacks. CSRF tokens ensure that form submissions are made by the authenticated user and not a malicious scripts from the attacker. If we don't add `csrf_token` to the Django form, an attacker could create a malicious request in the form of script/link that automatically sends a request to our server by taking the credentials of the active user. Without this token, the server cannot verify whether the request received comes from a legitimate source, allowing the attacker to perform unwanted actions on behalf of that user, such as changing data or making unauthorized transactions.

 ### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
 

- Create a form that can receive new datas

```python
# forms.py
from django.forms import ModelForm
from main.models import Product

class ShopEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "color"]
```

Add an UUID to the model to correctly identify each `Product` model

```python
# models.py
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

- Add a URL path for Form

```python
# urls.py
from django.urls import path

urlpatterns = [
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```

- Create an HTML template to show form:
```html
<!-- create_product_entry.html -->
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
```html
<!-- main.html -->
{% if not product_entries %}
<p>There are no products in cherry store.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Color</th>
  </tr>

  {% comment %} This is how to display product
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.color}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```
```python
# views.py
def show_main(request):
    shop_entry = Product.objects.all()
    context = {
        'application_name': 'cherry-shop',
        'class': 'PBD KKI',
        'name': 'Rayienda Hasmaradana',
        'product_entries' : shop_entry
    }

    return render(request, "main.html", context)
```

Then create a View to show and process input form

```python
# views.py
def create_product_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

- Adding 4 Views Function to View Object in XML and JSON Format

View for XML:

```python
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

View for JSON:

```python
from django.http import HttpResponse
from django.core import serializers

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

View for XML by ID:

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

View for JSON by ID:

```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- Make a routing for each views:
Add a URL Routing for each views in the format JSON and XML to `urls.py`:

```python
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
app_name = 'main'

urlpatterns = [

#URL for XML and JSON
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),

#URL for XML and JSON by ID
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),

]
```

### Accessing the four URLs by using Postman:

**JSON**
 ![alt text](images/postman_json.png)

**XML**
![alt text](images/postman_xml.png)

**JSON by ID**
![alt text](images/postman_json_by_id.png)

**XML by ID**
![alt text](images/postman_xml_by_id.png)
</details>

<details>
<Summary><b>Assignment 4</b></Summary>

## Assignment 4 - PBD

### What is the difference between HttpResponseRedirect() and redirect()?
- HttpResponseRedirect() is a class that gives back response HTTP 302 (which means "Found", i.e., redirection) to redirect the user to another URL. It is lower-level and requires an explicit URL.
example:

```
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some/url/')
```
- redirect()
redirect() is a shortcut function provided by Django that makes it easier to perform redirects. It is more convenient and flexible, automatically resolving URLs. Preferred in most cases for its simplicity and ease of use. 
example: 

```
from django.shortcuts import redirect

def my_view(request):
    return redirect('/some/url/')
```

### Explain how the Product model is linked with User!
In Django, the ForeignKey relationship is usually used to link the `Product` model with the `User` model. This allows each product to be associated with a specific user.

example:
```
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model

    def __str__(self):
        return self.name
```
Every time a user made a new product entry, the following entry is linked with the logged in user. The ForeignKey relationship allows a user can have many entries.

### What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.

Authentication is the process of verifying a user's identity, usually through a username and password combination. Authorization determines what a user is allowed to do and which resources they can access once they are authenticated. 

#### What Happens When a User Logs In?
- the user submits credentials info (username and password)
- authentication: the system verifies the provided credentials against stored data
- authorization: the system checks the users permission to determine the actions they can perform and what resources they can access

#### How Django Implements Authentication and Authorization
- authentication:
1. User Model: Django includes a built-in User model that stores user information.
2. Authentication Views: Django provides views for login, logout, and password management.
3. Authentication Backends: Django uses authentication backends to handle the authentication process. The default backend checks the username and password against the User model.
4. Login: The authenticate function verifies the credentials, and the login function creates a session for the user.

- authorization
1. Permissions: Django's User model includes fields for permissions. Permissions can be assigned to users or groups.
2. Groups: Groups are a way to apply permissions to multiple users. Users in a group inherit the group's permissions.
3. Decorators and Mixins: Django provides decorators like @login_required and mixins like PermissionRequiredMixin to restrict access to views based on user authentication and permissions.

### How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

Django uses sessions to remember logged-in users. When a user logs in, Django creates a session and stores the session ID in a cookie on the user's browser. This session ID is then used to identify the user in subsequent requests.

#### Other Uses of Cookies:
Cookies can be used to track user behavior for analytics purposes, store user preferences and settings, and store information to personalize the user experience.

#### Are All Cookies Safe to Use?
Not all cookies are safe to use. Unsecure cookies may be vulnerable to Cross-Site Scripting (XSS) attacks. Security considerations include:

- Secure Cookies : use the `Secure` flag to ensure cookies are only sent over HTTPS
- HttpOnly Cookies: use the `HttpOnly` flag to prevent client-side scripts from accessing the cookie
SameSite Cookies: Use the `SameSite` attribute to prevent cross-site request forgery (CSRF) attacks

### Explain how did you implement the checklist step-by-step (apart from following the tutorial).

1. Implement the Registration, Login, and Logout Functions

##### Registration
- Create a form for new user registration using `UserCreationForm`
- Create a view that handles the registration form and saves the new user to the database
- Redirect the user to the login page after successful registration

```python
# views.py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

import to `urls.py` and add to `urlspatterns`

```
# urls.py
from main.views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

- make the template `register.html` to display the registration form

```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
##### Login 
- Use function `login_user` to handle the login process
- add the login URL in `urls.py`

```
# urls.py
from main.views import login_user

urlpatterns = [
    path('login/', login_user, name='login'),
]
```

##### Logout
- Use function `logout_user` to handle the login process
- add the login URL in `urls.py`
```
# urls.py
from main.views import logout_user

urlpatterns = [
    path('logout/', logout_user, name='logout'),
]
```
add logout button in template

```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
##### Restricting Access to the Main Page
Make user requires to log in before accessing the web
```
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
...
```

##### Connecting `Product` with `User`

- Create a model `Product` and add ForeignKey to User

```
# models.py
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

- run the migration to apply changes
```
python manage.py makemigrations
python manage.py migrate
```

modify the function `create_product_entry` in `views.py` to modify the `user` field before saving it to the database to link product to the user that created it

```
def create_product_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

##### Show logged in user's username

get logged in user's data  in view 
```
# views.py
def show_main(request):
    shop_entry = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
    }
```

display user's information in `main.html`
```
<p>{{ name }}</p>
```

##### Apply Cookies for Last Login

Modify views.py to get last_login
```
# views.py
def show_main(request):
    context = {
        'last_login': request.COOKIES['last_login'],
    }
```
Display the last login:
main.html
```
<h5>Last login session: {{ last_login }}</h5>
```
</details>

<details>
<Summary><b>Assignment 5</b></Summary>

## Assignment 5 - PBD

### If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

When multiple CSS selectors apply to the same HTML element, the browser determines which styles to apply based on a set of rules known as specificity. The priority order of CSS selectors is determined by their specificity and the order in which they appear. Here is a detailed explanation of the priority order:

Specificity is calculated based on the types of selectors used in the CSS rule. It is represented as a four-part value: a, b, c, d.

1. Inline Styles (a): Inline styles have the highest specificity. They are applied directly to an element using the style attribute.

Example: <div style="color: red;"></div>
Specificity: 1, 0, 0, 0

2. ID Selectors (b): ID selectors have high specificity and are unique within a document.

Example: #header { color: blue; }
Specificity: 0, 1, 0, 0

3. Class, Attribute, and Pseudo-class Selectors (c): These selectors have moderate specificity.

Example: .container { color: green; }
Example: [type="text"] { color: yellow; }
Example: :hover { color: pink; }
Specificity: 0, 0, 1, 0

4. Element and Pseudo-element Selectors (d): These selectors have the lowest specificity.

Example: div { color: black; }
Example: ::before { content: ""; }
Specificity: 0, 0, 0, 1

Example:
```

<title>CSS Specificity</title>
    <style>
        div { color: black; } /* Specificity: 0, 0, 0, 1 */
        .container { color: green; } /* Specificity: 0, 0, 1, 0 */
        #header { color: blue; } /* Specificity: 0, 1, 0, 0 */
        div#header.container { color: red; } /* Specificity: 0, 1, 1, 1 */
    </style>
```
the element will have the text color red because the selector div#header.container hsa the highest specificity.\

Summary
Inline Styles: Highest priority (1000 points)
ID Selectors: High priority (100 points)
Class, Attribute, and Pseudo-class Selectors: Moderate priority (10 points)
Element and Pseudo-element Selectors: Lowest priority (1 point)


### Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!

Responsive design is crucial in web application development for several reasons:

User Experience: Responsive design ensures that users have a consistent and optimal experience across different devices, including desktops, tablets, and smartphones. This adaptability enhances user satisfaction and engagement.

Increased Mobile Usage: With the rise in mobile device usage, it's essential for web applications to be accessible and functional on smaller screens. Responsive design addresses this need by adjusting the layout and content to fit various screen sizes.

SEO Benefits: Search engines like Google prioritize mobile-friendly websites in their search results. Implementing responsive design can improve a website's search engine ranking, leading to increased visibility and traffic.

Cost-Effectiveness: Developing a single responsive website is more cost-effective than creating separate versions for desktop and mobile. It reduces development and maintenance efforts.

Future-Proofing: Responsive design prepares web applications for future devices and screen sizes, ensuring long-term usability and relevance.

#### Examples of applications that have  implemented responsive design:

- X: X's web application adjusts the layout and content to different screen sizes

- Google Maps: Google Maps adapts its interface depending on screen size while keeping essential features accessible

#### Examples of applications that have not implemented responsive design:

SIAK NG: Smart interface only available on desktop mode.

### Explain the differences between margin, border, and padding, and how to implement these three things!
1. Margin: The space outside the border of an element. It creates space between the element and its neighboring elements.

2. Border: The line around an element. It creates a frame around an element.

3. Padding: The space inside the border of an element. It creates space around the content of an element.

```
.example {
    margin: 20px;          /* Space outside the border */
    border: 2px solid black; /* Border around the element */
    padding: 10px;         /* Space inside the border, around the content */
}
```

### Explain the concepts of flex box and grid layout along with their uses!

Flexbox (Flexible Box Layout) is a CSS layout module designed to provide a more efficient way to lay out, align, and distribute space among items in a container, even when their size is unknown or dynamic. It is particularly useful for creating responsive layouts.

Uses of Flexbox:
- Allows elements to expand or shrink according to the available space
- Dynamically arranges elements in a row or column
- Ideal for creating horizontal or vertical navigation bars that need to be responsive and evenly spaced

example:
```
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between; /*divides elements equally*/
    align-items: center;
}
```

Grid Layout is a CSS layout module that provides a two-dimensional grid-based layout system, optimized for responsive design. It allows you to create complex layouts with rows and columns.

Uses of Grid Layout:
- For creating complex, two-dimensional layouts (rows and columns)
- Ideal for two-dimensional layouts, such as complex web page layouts, dashboards, photo galleries, and forms.

example:
```
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Creates three equal columns */
    grid-template-rows: auto;
    grid-gap: 10px; /* Space between grid items */
}
```
### Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

- Import tailwind in `base.html`

```
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```

and add the Tailwind CSS classes to each files in main/templates directory and added a navbar

example: `main.html`

```
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Cherry Store</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen" style="background-image: url('/static/image/white-pink-bg.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <div class="p-2 mb-6 relative">
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
      {% include "card_info.html" with title='NPM' value=npm %}
      {% include "card_info.html" with title='Name' value=name %}
      {% include "card_info.html" with title='Class' value=class %}
    </div>
    <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
      <div class="w-full min-h-4 bg-[#800000]">
      </div>
    </div>
    <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
      <div class="h-full min-w-4 bg-[#800000] mx-auto">
      </div>
    </div>
  </div>

  <div class="px-3 mb-4">
    <div class="flex rounded-md items-center bg-[#800000] py-2 px-4 w-fit">
      <h1 class="text-white text-center">Last Login: {{ last_login }}</h1>
    </div>
  </div>

  <div class="flex justify-end mb-6">
    <a href="{% url 'main:create_product_entry' %}" class="bg-[#800000] hover:bg-[#660000] text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product Entry
    </a>
  </div>

  {% if not product_entries %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4" />
    <p class="text-center text-gray-600 mt-4">There is no product yet in Cherry Store.</p>
  </div>
  {% else %}
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
    {% for product_entry in product_entries %}
      {% include 'card_product.html' with product_entry=product_entry %}
    {% endfor %}
  </div>
  {% endif %}
</div>
{% endblock content %}
```
- Add edit and delete feature

```
#views.py
#edit feature
def edit_product(request, id):
    edit_product = Product.objects.get(pk = id)

    form = ShopEntryForm(request.POST or None, instance=edit_product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

#delete feature
def delete_product(request, id):
    delete_product = Product.objects.get(pk = id)
    delete_product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

```

add imports to `views.py` file

```
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
```

create an HTML file named `edit_product.html` and fill it with this code:

```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen " style="background-image: url('/static/image/flower3.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-[#800000] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#750000] transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```

add URL path to `urls.py`

```
...
from main.views import edit_product
from main.views import delete_product
app_name = 'main'

urlpatterns = [
path('edit-product/<uuid:id>', edit_product, name='edit_product'),
path('delete/<uuid:id>', delete_product, name='delete_product'),
...
]
```

modify the `main.html` to add edit and delete button
```
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
</tr>
...
```

- Adding navigation bar

create new HTML file named `navbar.html` under the folder `templates` in the main directory and fill with this code:

```
<nav class="shadow-lg fixed top-0 left-0 z-40 w-screen" style="background-color: #800000;">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-2xl font-bold text-center text-white">Cherry Store</h1>
      </div>
      <!-- Desktop Navbar -->
      <div class="hidden md:flex items-center">
        <a href="#" class="text-gray-300 hover:text-white mx-4">Home</a>
        <a href="#" class="text-gray-300 hover:text-white mx-4">Products</a>
        <a href="#" class="text-gray-300 hover:text-white mx-4">Categories</a>
        <a href="#" class="text-gray-300 hover:text-white mx-4">Cart</a>

        {% if user.is_authenticated %}
          <span class="text-gray-300 mx-4">Welcome, {{ user.username }}♥ </span>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mx-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      
      <!-- Add Mobile Hamburger Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
      <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
      <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
      <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
      {% if user.is_authenticated %}
        <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>

  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```

- Configure static files

added these codes to `settings.py`
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add it directly under SecurityMiddleware
    ...
]

...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' 
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'
...
```

- Add CSS for styling

Create a new file `global.css` under the folder `static` in the root directory
```
body {
    background-color: #800000; /* Set background color to maroon */
    color: #ffffff; /* Ensure text is white for contrast */
}

.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
    background-color: #ffffff;
    color: #000000;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #800000;
    box-shadow: 0 0 0 3px #800000;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
}
```

Add these code to `base.html` to link `global.css` and Tailwind script to `base.html`

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Styling the login, register, home, edit, and add new product page

`login.html`
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen py-12 px-4 sm:px-6 lg:px-8"
     style="background-image: url('/static/image/flower7.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">  
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#800000] hover:bg-[#750000] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

`register.html`
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen py-12 px-4 sm:px-6 lg:px-8"
     style="background-image: url('/static/image/flower7.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">  
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#800000] hover:bg-[#750000] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
`card_info.html`

```
<div class="rounded-xl overflow-hidden border-2" style="background-color: #800000; border-color: #4c0000;">
  <div class="p-4 animate-shine">
    <h5 class="text-lg font-semibold text-gray-200">{{ title }}</h5>
    <p class="text-white">{{ value }}</p>
  </div>
</div>
```

`card_product.html`

```
<div class="relative break-inside-avoid">
  <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
    <div class="w-[3rem] h-8 bg-pink-200 rounded-md opacity-80 -rotate-90"></div>
  </div>
  <div class="relative top-5 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-white-300 transform rotate-1 hover:rotate-0 transition-transform duration-300"
     style="background-image: url('/static/image/flower2.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
    <div class="p-4 rounded-t-lg border-b-2" style="background-color: #923939; border-color: #d2b7b7;">
      <h3 class="font-bold text-xl mb-2">{{ product_entry.name }}</h3>
      <p class="text-black-600">{{ product_entry.price }}</p>
    </div>
    <div class="p-4">
      <p class="font-semibold text-black mb-2">Description</p> 
      <p class="text-gray-700 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{ product_entry.description }}</span>
      </p>
      <p class="font-semibold text-black mb-2">Color</p> 
      <p class="text-gray-700 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{ product_entry.color }}</span>
      </p>
    </div>
  </div>
  <div class="absolute top-0 -right-4 flex space-x-1">
    <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</div>
```

modify `main.html`
```
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Cherry Store</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen" style="background-image: url('/static/image/white-pink-bg.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <div class="p-2 mb-6 relative">
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
      {% include "card_info.html" with title='NPM' value=npm %}
      {% include "card_info.html" with title='Name' value=name %}
      {% include "card_info.html" with title='Class' value=class %}
    </div>
    <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
      <div class="w-full min-h-4 bg-[#800000]">
      </div>
    </div>
    <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
      <div class="h-full min-w-4 bg-[#800000] mx-auto">
      </div>
    </div>
  </div>

  <div class="px-3 mb-4">
    <div class="flex rounded-md items-center bg-[#800000] py-2 px-4 w-fit">
      <h1 class="text-white text-center">Last Login: {{ last_login }}</h1>
    </div>
  </div>

  <div class="flex justify-end mb-6">
    <a href="{% url 'main:create_product_entry' %}" class="bg-[#800000] hover:bg-[#660000] text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product Entry
    </a>
  </div>

  {% if not product_entries %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4" />
    <p class="text-center text-gray-600 mt-4">There is no product yet in Cherry Store.</p>
  </div>
  {% else %}
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
    {% for product_entry in product_entries %}
      {% include 'card_product.html' with product_entry=product_entry %}
    {% endfor %}
  </div>
  {% endif %}
</div>
{% endblock content %}
```

styling `create_product_entry.html`

```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Add Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen " style="background-image: url('/static/image/flower3.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Add New Product Entry</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-[#800000] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#750000] transition duration-300 ease-in-out w-full">
            Add Product Entry
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

styling `edit_product.html`

```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen " style="background-image: url('/static/image/flower3.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-[#800000] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#750000] transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```
</details>

<details>
<Summary><b>Assignment 6</b></Summary>

## Assignment 6 - PBD

### Explain the benefits of using JavaScript in developing web applications!
- Saves time and bandwith: JavaScript will always be executed on the client environment to save lots of bandwith and make the execution process fast

- Cross-browser compatibility: It supports all modern browsers and produce an equivalent result

- Integration with HTML and CSS: Seamlessly integrates with HTML and CSS to create dynamic and visually appealing web pages

- Security: Provides mechanisms to enhance security, such as Content Security Policy (CSP) and HTTPS

- Versatility: It is possible to develop a whole JavaScript app from front to back using only JavaScript 

- Real-Time Communication: Enables real-time communication features like WebSockets for live updates and notifications. Useful for applications like chat apps, live feeds, and collaborative tools

### Explain why we need to use await when we call fetch()! What would happen if we don't use await?

It is used so the function will wait until the fetch is done, it ensures every operation completes before the next one starts. If we don't use await, the code inside the promise will still run, but nothing happen when we call resolve. But if we call reject nothing will handle the rejection, which is bad as it throws an error on most platforms.

### Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

Because it'll create security issues if we don't use it. Disabling or not using CSRF protection can expose our application to possible CSRF attacks. We use the csrf_exempt decorator on a view handling AJAX POST requests to bypass CSRF (Cross-Site Request Forgery) protection for that specific view. This is necessary when the request doesn't include a valid CSRF token, which is normally required to ensure that the request is from a trusted source. By exempting the view, we allow the request without the CSRF token, though this can reduce security if not handled properly.

### On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?
User input sanitization should not be done only in the front-end because front-end validation can easily be bypassed. Attackers can manipulate requests using tools like browser developer tools or send crafted requests directly to the server, bypassing the front-end entirely. Back-end validation ensures that all incoming data is properly sanitized and secure, regardless of what happens on the client side. This provides a critical layer of security and protects against malicious inputs, such as SQL injection or XSS (Cross-Site Scripting) attacks.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
</details>