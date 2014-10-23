Flask on Rails is a project to build a Ruby on Rails style web framework
with conventions and guidelines that provide a easy to understand framework
for quickly getting started developing web applications with the Python based
Flask micro web framework and its wide ecosystem of approved extensions.

The Flask on Rails framework tries to incorporate the best concepts of Ruby on Rails while still retaining
the simplicity and low magic level of the Flask framework and also remaining true
to the Pythonic way. It is mostly about providing a well known application structure and integrating an
opinionated set of Flask extensions and other design patterns for building
large web applications, so that a developer new to the framework can jump in an be productive
right away and have a set of conventions to follow to be able to add and change features
more rapidly yet not have the application framework get in his or her own way.
The framework includes a set of sane defaults and functionality that can be removed or changed any way
the user pleases with very little effort.
It also includes a set of scripts to get the application setup and up and running with a backing
github code repo and postgres database with Heroku deployment instantly.(provided you have git hosting and have installed
git and PostGres. - I have also included helper scripts for installing git,postgres,python and virtualenv on a Mac)

Before diving into the Framework details I want to take a moment to extend my sincere appreciation
to the following people that
have made it possible for me to be able to build my first
Flask and Python project and be able to extract this framework from that work due to their contributions
to the flask ecosystem.

Michael Herman for his wonderfull series of  Real Python tutorials and free videos explore flask.
Michael Greenburg for his excellent Oreilly Flask book and Pycon tutorials
Rober Picard for his wonderfull free explore flask ebook supported by kickstarter
Armin Ronnacher for creating the Flask framework and giving us Flask blueprints and the g property!
xxxx the creator of SqlAlchemy for creating the backbone of many database driven web app in the python
ecosystem.

I also want to shout out to all those who have created the Flask extension ecosystem without whom,
more complex web app development with Flask would simply not be possible. Specifically I want to
call out xxxx developer of the PeeWee Active Record style Python ORM that is used as an alternative database
access component to the default SqlAlchemy Hibernate style data access in the framework, xxxx the developer
of flask-login extension which handles the user authentication layer not included in the core Flask framework and
that other extensions have used as the base for adding security features to Flask applications.


Finally I want to call attention to the wonderfull two part blog article by xxx that describes how to
build and deploy a flask app using the Nginx,uWsgi,supervisored stack and the numerous blog articles
by the community about Flask.

I always have had the philosophy of using the best tool for the job. This has allowed me to be technology
agnostic polyglot developer. When deciding on a database schema migration component for the Flask on Rails
framework, I came to the conclusion that the best framework to use would be the Rails active record migrations
framework and associated tools such as the Ruby Rake task runner. The Rails migrations framework has been
around for a while and has proven itself over time. I beleive it has the best API and tooling out there compared to
any of the migration frameworks in Python. Also since this is the Flask on Rails project why not pay some
homage to the Rails framework by directly using one of the best parts of it. Of course you do not have to use
the Rails migration componnet of Flask on Rails and you can easlily substitute your own Python flavor of
migrations by using the also great Alembic migrations framework.

Before extracting the Flask on Rails framework from my web project, I searched extensively for other Flask
large web app templates and boilerplates. Pretty much all large Flask applications use the Flask Blueprints
feature. The Blueprints feature was mostly meant for dividing the large web app into smaller self contained
sub application sections similar to how the django web apps are structured.
I did find some boilerplates that used
blueprints to divide larger apps into more restful resource oriented structure similar to rails resource
controllers
but almost all did not go all the way in seperating out app concerns into their own folder structure and
there was some level of Ad-hoc ness in their designs, throwing things into __init__.py methods and bunching together
unrelated components in a single file or not organizing models,forms, etc. in their own separe files and directories.
I also found none that were opinionated enough to integrate a set
of recommended extensions to provide complete application design functionality. Finally none had an lightwaight
integrated token based authentication\user account system which almost all web applications these days need.

So I came to the conslusion that extracting a framework from my real world application would be the
right thing to do, to build a framework that is more well thought out from
the alternatives. That being said, I would be remmiss to not mention the  Flask-mvc framework
that I found that looks very complete and
in some ways is closer to Ruby on Rails in philosophy then my own framework.

In the end I thought that the  Flask-mvc framework added somewhat more
complexity in order to be closer to the rails design of having controller classes with action methods where
in my case I use responder files as the encapsulating construct for responder functions that are not
contained in a Python class. I view this design as more pythonic and closer to spirit of Flask.
That being said I still
do recommed flask-view as an alternative that looks very nice with the disclamer that I
have not actually tried using it personally.

So without further ado, lets dive into the features and components of the Flask on Rails framwork.

-single configuration component for all environments, based on shell environment variable settings.
-Responder functions grouped into responder files corresponding to restful resources.(note responders are the same
as Views which handle web requests in Flask and other python web frameworks. They are the same as controller actions
in ruby on rails)
-optional centralised route maps in a single file that can be mixed with attribute routes if desired
-default sqlalchemy integration with optional peewee active record data access integration that can be mixed.
-flask-login integration for user authentication
-flask blueprints functional structure
-support for before,after,teardown request filters
-support for global and blueprint specific error handlers
-support for Flask app factory for app testing
-support for tasks running under Flask app context
-supprort for standard Flask extensions via the plugins.py file
-all empty __init__.py modules. No need to guess what app functionality is burried in some __init__.py file
-ruby on rails active record database mogrations(litterally!)
-scripts to support setting up virtual env, installing packages based on requirements.txt, setting
up postgres database and sqlalchemy connection string env variable
-scripts to support creating inital application along with initial github commit (cuz we all know that we should be using
source control from day 1)
-scripts to support auto launching the text editor, runnng the dev server and launching the web browser

The Ultimate goal is for the developer to execute a bash script have a new project running
with areal database
and integrated into source
control in under a minute. And from then on can take a quich two minute look at the
project structure and start adding responder files, responder functions
and html\jinja template files to start adding more features to the app.
Further they should be able to, if they desire, setup a Heroku account and get the app deployed in a minute.

In the future I plan to add similar convenience to deploy to AWS directly using postgres RDS and centos ami
running Nginx,uwsgi and supervisored utilizing Route53 DNS and ELB load balancing and elstic beanstalk background jobs. If anyone is interested to
script this out from A to Z including provisioning with boto\ansible\docker please contact me. some resources
to get started: aws flask app link.

Before I continue with the detailes of the features of the framework a shameless plug:
I am a developer with twenty year of software development experience from C to C++ to C# to recently Python.
I have worked for Boeing as an embedded systems engineer, America Online as a Principle software developer
and Autobytel.com as a
senior staff developer.
I have been a C# ASP.NET developer for the last 10 years. I have transistioned to
Linux, Python and Flask in the last year and am looking for paid Flask projects to work on.
I am interested in mostly backend development but I have worked quite a bit with jQuery in the past
and am excited about
React.js and kinetic.js for front end development. I am interested in devops as well especially in
AWS automation, immmutable infrastructire and Docker.
So if you have Flask projects that you are looking to staff you can contact me at xxxxxx.

---------------------
Comming features:
Mailers
Restful API support
Paging and load more support
search support
caching supports
data access query templates




