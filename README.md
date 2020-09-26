
# The Ross Assesment
Using Flask (as the web framework) and Pymongo (as the mongo driver).

### Up and Running Instructions
*preparing the system*
```bash
    docker run --name mymongo -d mongo #in case of lacking mongo in your machine
    git clone https://github.com/m-khademloo/RossAssesment
    cd RossAssesment
    pip3 install -r requirements.txt
```
*running the web-server*
```bash
    flask run #in the case that you have flask in your machine
    python3 app.py #otherwise
```


### Sample URLs: 
* Listing the users (masked data with limitation 30): http://127.0.0.1:5000/api/v1/users
* Get page #4 of users (masked data with limitation 30): http://127.0.0.1:5000/api/v1/users?page=4
* Get page #4 of users and page_size=10 (masked data): http://127.0.0.1:5000/api/v1/users?page=4&page_size=10
* Get detail information for a specefic user: http://127.0.0.1:5000/api/v1/users/5f4d3f4735fcfebd9fe20a73
* Get users with First Name equals to John(maximum 30): http://127.0.0.1:5000/api/v1/users?First%20Name=John
* Get users with First Name equals to John and Last Name equals to Culbertson(maximum 30): http://127.0.0.1:5000/api/v1/users?First%20Name=John&last_name=Culbertson
* Listing the users (masked data with limitation 100): http://127.0.0.1:5000/api/v1/users?page_size=100

### Specifications
* Python v3.7.3
* MongoDB: v3.6.8
* Flask: v1.1.2
