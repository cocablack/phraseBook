source myproject/bin/activate
--> activate virtual environment


python manage.py runserver
--> run application with a test server


python manage.py shell
--> insert data


>>> from tumblelog.models import *
>>> post = Post(
... title="Hello World!",
... slug="hello-world",
... body="Welcome to my new shiny Tumble log powered by MongoDB, MongoEngine, and Flask"
... )
>>> post.save()
--> save data


/var/lib/mongodb-mms-automation/mongodb-osx-x86_64-3.2.1/bin/mongo Jennyui-MacBook-Pro.local:27000
--> connect to mongod via shell