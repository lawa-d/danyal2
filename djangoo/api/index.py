from vercel_python import vercel_wsgi
from mysite.wsgi import application

app = vercel_wsgi(application)
