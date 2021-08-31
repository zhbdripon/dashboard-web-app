
# Dashboard-Web-Application API Documentation

A brief description of what this DRF app does

## Create user accounts
Endpoint: `/auth/users/`

Request Body : 
```
{
    "email": "",
    "password": ""
}
```

## Login user
Endpoint: `[POST] /auth/token/login/`

Request Body : 
```
{
    "email": "",
    "password": ""
}
```
Response Body : 
```
{
    "auth_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"             
}
```

## Logout user
Endpoint: `[POST] /auth/token/logout/`

Request header : 
```
{
    "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```


## Create Profile
Endpoint: `[POST] /profile/`

Request Body : 
```
Form Data:
    name
    gender
    dob
    address
    mobile
    blood_group
    avatar
```

## Profile Details
Endpoint: `[GET] /profile/:id/`

Request header : 
```
{
    "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

## Profile List [Admin]
Endpoint: `[GET] /profile/`

Request header : 
```
{
    "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

## Update Profile
Endpoint: `[PUT] /profile/:id/`

Request header : 
```
{
    "Authorization": "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```
Request Body : 
```
Form Data:
    name
    gender
    dob
    address
    mobile
    blood_group
    avatar
```