
## Image hosting api

Django API that allows any user to upload an image in
PNG or JPG format.


run application using docker
```
    $ docker-compose build
    $ docker-compose up -d   
```

add superuser
```
    $ docker-compose exec web python manage.py createsuperuser 
```

#### User Requirements
 - User must be staff ( to login using Django admin)
 - User must have subscription (add subscription using /admin/image_app/subscription/)
 
 #### API starting point
    /images/  [image_list]
    /images/<pk>/  [image_details]
