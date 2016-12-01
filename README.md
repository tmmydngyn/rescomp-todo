# Simple Todo App

[For Windows Users](#windows)<br />
[For *nix Users](#unix)<br />
[Setting up your environment](#env)<br />
[Running your app](#running)<br />

# Requirements

<a name="windows"></a>
## Windows Users

Unix environments have many important advantages for developers which allow for easy development, testing and deployment of applications. For this reason, it's useful to have access to a unix-like environment. [Cygwin](https://www.cygwin.com/) provides a native unix-like environment for Windows users. For this project in particular, we require the following things:

- git: version control system for managing changes to your code
- Python

<a name="unix"></a>
## *nix Users
You'll need the same packages as above (git, Python), though many *nix flavors have some or all of these pre-installed. If you don't have them installed, you should to install them with your package manager ([Homebrew](http://brew.sh) is a good choice for Mac users).

<a name="env"></a>
# Installation

First, let's download all the files for our application and change into that directory.
```
git clone https://github.com/tmmydngyn/simple-todo
```
Now, let's create the virtual environment for our app. For simplicity, let's put it into the directory where our app lives. This isn't necessary (see details below).
```
cd simple-todo
virtualenv todo-app # makes a virtual environment called todo-app
```
Finally, we'll enter our virtual environment and install the dependencies for our app.
```
source simple-app/bin/activate
pip install -r requirements.txt
```
Check if the packages were installed correctly by running `pip freeze`. You should see the following:
```
click==6.6
Flask==0.11.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
Werkzeug==0.11.11
wheel==0.24.0
```
The names to the left of `==` are the packages that were installed and the numbers are their versions.

## More info

Why do we need virtualenvs? A robust development environment makes development of any project much simpler in the long run. Especially important is the ability to quickly prototype and test changes. It is also important for your development environment to mirror your production environment as closely as possible, so that there are no unpleasant surprises when you deploy your code.

One of the primary difficulties developers encounter when working on multiple projects is conflicting dependencies. I may have an app that depends on a legacy version of Flask, for instance, but want to start a new app with the latest version. One extremely simple solution for managing project requirements is called a virtualenv. Virtualenvs handle things like project specific packages or environment variables, so that separate apps in separate virtualenvs can run side by side.

The command `virtualenv todo-app` creates a virtual environment called `todo-app`. You may name the virtualenv whatever you want, as it has no correlation with the name of your app. This will automatically create a directory called todo-app which houses your project's dependencies. Note that while your dependencies live here, your project doesn't need to! When you enter your virtualenv your application will know to look for packages in this directory. 

`source todo-app/bin/activate` is how you enter your virtualenv (replace `todo-app` with the name of your virtualenv). All this does is modify your environment variables to point your application to the packages in `todo-app/`. 

When inside a virtualenv, `pip install` will install packages into `todo-app/` rather than your global packages.

<a name="running"></a>
# Running your app

Now that everything's installed, you can run your app. To do so, you'll need to activate your virtualenv so that Python knows to look for the dependencies in your virtualenv instead of globally on your machine.

Assuming you're still in the simple-todo directory:
```
virtualenv todo-app
python todo.py
```
You should be able to view the app by launching a web browser and navigating to `localhost:5000`.
