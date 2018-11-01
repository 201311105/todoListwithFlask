#Statment for enabling the development environment
DEBUG = True

#Defube the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Define the database - skip

#Application threads. A common general assumption is
#using 2 per available processor cores - to handle
#incoming requests using one and performing background
#operaions using the other
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)* 
CSRF_ENABLED = True

#Use a secure, uniqe and absolutely secret key for
#signing the data
CSRF_SESSION_KEY = "secret"

#Secret key for signing cookies
SECRET_KEY = "secret"
