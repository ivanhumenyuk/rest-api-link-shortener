# Link Shortener
Project that shortens links and redirects from short links to a resource.
## Instolation
Clone this repository to your local repository:<br/> 
```
git clone https://github.com/ivanhumenyuk/rest-api-link-shortener
```
First of all you have ro install all dependencies.
Just write in your console:
```
pip install requirements.txt
```
## Run api server
To run REST api server open the path to the Link Shortener repository in the console and write:
```
python manage.py runserver
```
## REST Api
### Shorten link
- ####Request
   - method: `PUT`
   - endpoint: `/shorten`
   - content-type: `application/json`
   - required `link=[str]`, `lifetime=[int]`<br/>
   
Example: 
```
{
    "link": "https://developer.mozilla.org/ru/docs/Web/HTTP/Status/401",
    "lifetime": 30
}
```

- ####Success Response
Code 201 OK <br/>
Example: <br/>
```
{
    "message": "Already shortened.",
    "short_link": "http://localhost:5000/2g3I3aE"
}
```

- ####Error Response


- ####Redirection