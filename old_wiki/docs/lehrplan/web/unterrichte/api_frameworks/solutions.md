# Lösungen

## 1. Flask & Django Hello World
### Flask
```python
from flask import Flask
app = Flask(__name__)

@app.route('/') # Flask URL-Endpunkt Annotation
def hello_world():
return 'Hallo Welt!'

if __name__ == '__main__':
app.run(debug=True, port=5000)
```

### Django
```python
# views.py
from django.http import HttpResponse

def hello_world(request):
return HttpResponse('Hallo Welt!')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
path('', views.hello_world),
]
```