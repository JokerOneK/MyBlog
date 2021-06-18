<h2>**Personal WebBlog application**</h2>

Personal WebBLog with the features of users' authentication, personal web-posts creation 
and API based on Django Rest Framework. The working example you can observe, 
by following this link: https://altayblog.herokuapp.com/.

<h3>Getting Started</h3>

Initially you must clone the GitHub repository:

`$ git clone https://github.com/JokerOneK/MyBlog.git`

`$ cd MyBlog`

Moreover, you have to create a virtual environment to install dependencies in and activate it:

`$ virtualenv2 --no-site-packages env`

`$ source env/bin/activate`

After the creation of environment you should install the dependencies:

`(env)$ pip install -r requirements.txt`
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

`(env)$ cd project`

`(env)$ python manage.py runserver`

`And navigate to http://127.0.0.1:8000/.`


<h3>Features</h3>
<li>Fully constructed front-end design. (HTML, CSS< JavaScript).</li>
<li>The whole application was based on Class Based Views, except the authentication system.</li>
<li>Authentication provided by Django Framework.</li>
<li>API, based on Django Rest Framework, which provides fully access to every post of application.
In order to get the access to API you should go to <a>http://127.0.0.1:8000/api</a></li>
<li>Ready working example of the project on Heroku.</li>

<h3>How to modify the application?</h3>
<i>In order to add some modifications to the authentication system, you should work with the `accounts` folder.

If you want to modify the CSS, JavaScripts files, you must work with the `static` folder. However, all HTML files are located
in `accounts/templates` and `Blog/templates` folders.

Finally, to work with the API of application you have to go to `Blog/serializers.py` file.</i>

<h3>Credits:</h3>
<i>The HTML template for this application was obtained from </i>
<a>https://www.uipasta.com/devblog-personal-blog-template/</a>.
