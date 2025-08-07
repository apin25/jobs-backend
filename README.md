## BACKEND APIN DOCUMENTATION

Desclaimer ini agak lama ya loadingnya maaf, tolong jangan masukkin data banyak banyak karena gratisan
### Authentikasi

#### 1. Register - POST
Endpoint  = https://jobs-backend-apin.vercel.app/api/users/register

Body
```
{
"username": "apin",
"password":"apin"
}
```

Response
```
{
    "id": "3fa58d7a-9d41-4bda-9e11-7f634f042a63",
    "username": "apin"
}
```

#### 2. Login - POST
Endpoint  = https://jobs-backend-apin.vercel.app/api/users/login

Body
```
{
"username": "apin",
"password":"apin"
}
```

Response
```
{
    "token": "b167c87bb67807aef0c7bb4875ecc345ea87d60a"
}
```

#### 3. Add Job - POST
Endpoint = https://jobs-backend-apin.vercel.app/api/job/add-job

Body dengan Bearer Token : b167c87bb67807aef0c7bb4875ecc345ea87d60a
```
{
    "job_position":"Software Engineer",
    "type_of_workplace":"On Site",
    "job_location":"Jakarta",
    "company":"ABC",
    "employment_type":"Full time",
    "description":"Dibuka untuk semua frash graduate dan upah 6juta"
}
```

Response
```
{
    "id": "228f8c35-8778-4a86-863d-fd480e7177c3",
    "job_position": "Software Engineer",
    "type_of_workplace": "On Site",
    "job_location": "Jakarta",
    "company": "ABC",
    "employment_type": "Full time",
    "description": "Dibuka untuk semua frash graduate dan upah 6juta",
    "is_deleted": false
}
```

####OPSI Employment Type sama Workplace
```
TYPE_OF_WORKPLACE = [
    ("On Site", "On Site"),
    ("Hybrid", "Hybrid"),
    ("Remote", "Remote")
]
EMPLOYMENT_TYPE = [
    ("Full time", "Full time"),
    ("Part time", "Part time"),
    ("Contract", "Contract"),
    ("Temporary", "Temporary"),
    ("Volunteer", "Volunteer"),
    ("Apprenticeship", "Apprenticeship")
]
```

#### 4. Get All Job - GET
Endpoint = https://jobs-backend-apin.vercel.app/api/job/get-list-job
Bearer Token : b167c87bb67807aef0c7bb4875ecc345ea87d60a

Response
```
[
    {
        "id": "228f8c35-8778-4a86-863d-fd480e7177c3",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    },
    {
        "id": "33a8aab4-d1ad-4f5b-a83c-6585f4e18664",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    },
    {
        "id": "f46cbb68-4188-4f19-a2eb-05128f047533",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    },
    {
        "id": "77811328-d52d-49c2-8c25-bf807dc3c3b3",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    },
    {
        "id": "cb1553e0-0288-455b-a4cc-7cd3a2ad2517",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    },
    {
        "id": "9c0ff821-a0be-4707-80b3-8bfb772fa114",
        "job_position": "Software Engineer",
        "type_of_workplace": "On Site",
        "job_location": "Jakarta",
        "company": "ABC",
        "employment_type": "Full time",
        "description": "Dibuka untuk semua frash graduate dan upah 6juta",
        "is_deleted": false
    }
]
```

#### 5. Update Job - PUT
Endpoint = https://jobs-backend-apin.vercel.app/api/job/update-job/:id

Body dengan Bearer Token : b167c87bb67807aef0c7bb4875ecc345ea87d60a

{
    "job_position":"Software Engineer",
    "type_of_workplace":"On Site",
    "job_location":"Jakarta",
    "company":"ABC",
    "employment_type":"Full time",
    "description":"Dibuka untuk semua frash graduate dan upah 6juta"
}
Response

{
    "id": "228f8c35-8778-4a86-863d-fd480e7177c3",
    "job_position": "Software Engineer",
    "type_of_workplace": "On Site",
    "job_location": "Jakarta",
    "company": "ABC",
    "employment_type": "Full time",
    "description": "Dibuka untuk semua frash graduate dan upah 6juta",
    "is_deleted": false
}
####OPSI Employment Type sama Workplace

TYPE_OF_WORKPLACE = [
    ("On Site", "On Site"),
    ("Hybrid", "Hybrid"),
    ("Remote", "Remote")
]
EMPLOYMENT_TYPE = [
    ("Full time", "Full time"),
    ("Part time", "Part time"),
    ("Contract", "Contract"),
    ("Temporary", "Temporary"),
    ("Volunteer", "Volunteer"),
    ("Apprenticeship", "Apprenticeship")
]

#### 6. Detail Job - GET
Endpoint = https://jobs-backend-apin.vercel.app/api/job/get-job-detail/:id
Bearer Token : b167c87bb67807aef0c7bb4875ecc345ea87d60a

Response
```
{
    "id": "9c0ff821-a0be-4707-80b3-8bfb772fa114",
    "job_position": "Software Engineer",
    "type_of_workplace": "On Site",
    "job_location": "Jakarta",
    "company": "ABCD",
    "employment_type": "Part time",
    "description": "Dibuka untuk semua frash graduate dan upah 6juta",
    "is_deleted": false
}
```

#### 7. Delete Job (Soft Delete) - PUT
Endpoint = https://jobs-backend-apin.vercel.app/api/job/delete-job/:id
Bearer Token : b167c87bb67807aef0c7bb4875ecc345ea87d60a

Response
```
{
    "detail": "Job successfully soft-deleted."
}
```

### 8. Me - GET
Endpoint = https://jobs-backend-apin.vercel.app/api/users/me/:token

Response
```
{
    "id": "3fa58d7a-9d41-4bda-9e11-7f634f042a63",
    "username": "apin"
}
```