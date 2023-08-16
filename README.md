# back-end-jeweltime 🏗️ 💎 ⚒️ 📓

## Overview

`back-end-jeweltime` is the backend component of [Jewel Time](https://jeweltime.onrender.com), a web application that serves as a digital field notebook for jewelers. Designed to support the creative process, it offers features such as project tracking and retrieval of current precious metal prices. Crafted as a capstone project for Ada Developers Academy Cohort 19, it leverages Flask and MongoDB to document metalsmithing projects.

## Collaboration

Created in collaboration with [Angie Contreras](https://github.com/AngieCCo) who built the frontend with React. Check out our [frontend repository](https://github.com/AngieCCo/front-end-jeweltime).

## Technologies Used

- Flask
- MongoDB
- Flask-PyMongo
- Marshmallow

## Base URL

- The base URL for the deployed API is: `https://jeweltime-api.onrender.com`

- For local development, you can use: `http://localhost:5000` or `http://127.0.0.1:5000`


## Endpoints for Accounts

### Create an Account

- **POST** `/accounts`    
  
- **Required fields:** `firstName`, `lastName`, `email`, `zipcode`, and `firebaseId`
- **Request Body:**
    ```json
    {
        "email": "moira.rose@sc.ca",
        "firstName": "Moira",
        "lastName": "Rose",
        "zipcode": "90210",
        "firebaseId": "FirebaseAuthenticationID12345" 
    }
    ```
- **Response Body (201 Created):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890", 
        "email": "moira.rose@sc.ca",
        "firebaseId": "FirebaseAuthenticationID12345", 
        "firstName": "Moira",
        "lastName": "Rose",
        "zipcode": "90210"
    }
    ```

### Retrieve an Account by Account ID

- **GET** `/accounts/<accountId>`
  
- **Response Body (200 OK):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890", 
        "email": "moira.rose@sc.ca",
        "firebaseId": "FirebaseAuthenticationID12345", 
        "firstName": "Moira",
        "lastName": "Rose",
        "zipcode": "90210"
    }
    ```

### Retrieve an Account by Firebase ID 

- **POST** `/signin`
  
- **Request Body:**
    ```json
    {
        "firebaseId": "FirebaseAuthenticationID12345" 
    }
    ```
- **Response Body (200 OK):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890", 
        "email": "moira.rose@sc.ca",
        "firebaseId": "FirebaseAuthenticationID12345", 
        "firstName": "Moira",
        "lastName": "Rose",
        "zipcode": "90210"
    }
    ```
### Update an Account

- **PUT/PATCH** `/accounts/<accountId>`
- **Request Body:**
    ```json
    {
        "firstName": "Moira",
        "lastName": "Cawcaw",
        "zipcode": "L0C 1A0"
    }
    ```
    **Note**: This endpoint allows for updates to the account information, including fields that do not need to be updated. If the values match the existing data, they will not be changed. Include all the fields you wish to include in the request, even if some of them may remain the same. The email field is not updated through this endpoint due to the Firebase integration on the frontend.

- **Response Body (200 OK):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890", 
        "email": "moira.rose@sc.ca",
        "firebaseId": "FirebaseAuthenticationID12345", 
        "firstName": "Moira",
        "lastName": "Cawcaw",
        "zipcode": "L0C 1A0"
    }
    ```

### Delete an Account

- **DELETE** `/accounts/<accountId>`: Delete an account

- **Response Body (200 OK):**
    ```json
    {
        "message": "Account and its projects deleted successfully"
    }
    ```


## Endpoints for Projects

### Create a Project

- **POST** `/projects`: Create a project
  
- **Required Fields:**  `accountId`, `projectName`, `description`, and `startedAt`
  
- **Request Body:**
    ```json
    {
        "projectName": "Moira's Statement Ring",
        "description": "Silver ring with a bezel set obsidian",
        "accountId": "JewelTimeAccountID67890",
        "startedAt": "2017-08-21",
        "completedAt": "2017-08-24",
        "hoursSpent": "4.0",
        "materials": "paste solder",
        "materialsCost": "190",
        "metals": "sterling silver 18ga sheet, 24K gold foil",
        "gemstones": "6x5 cm obsidian cabochon",
        "notes": "The ring band was wide and thick, had to use a ring bender.",
        "shape": "irregular",
        "jewelryType": "ring"
    }
    ```
- **Response Body (201 Created):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890",
        "completedAt": "2017-08-24",
        "description": "Silver ring with a bezel set obsidian",
        "gemstones": "6x5 cm obsidian cabochon",
        "hoursSpent": "4.0",
        "jewelryType": "ring",
        "materials": "paste solder",
        "materialsCost": "190",
        "metals": "sterling silver 18ga sheet, 24K gold foil",
        "notes": "The ring band was wide and thick, had to use a ring bender.",
        "projectId": "JewelTimeProjectID12345",
        "projectName": "Moira's Statement Ring",
        "shape": "irregular",
        "startedAt": "2017-08-21"
    }
    ```
  
### Retrieve a Project

- **GET** `/projects/<projectId>`: Retrieve a project 

- **Response Body (200 OK):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890",
        "completedAt": "2017-08-24",
        "description": "Silver ring with a bezel set obsidian",
        "gemstones": "6x5 cm obsidian cabochon",
        "hoursSpent": "4.0",
        "jewelryType": "ring",
        "materials": "paste solder",
        "materialsCost": "190",
        "metals": "sterling silver 18ga sheet, 24K gold foil",
        "notes": "The ring band was wide and thick, had to use a ring bender.",
        "projectId": "JewelTimeProjectID12345",
        "projectName": "Moira's Statement Ring",
        "shape": "irregular",
        "startedAt": "2017-08-21"
    }
    ```

### Retrieve All Projects for an Account

- **GET** `/accounts/<accountId>/projects`: Retrieve all projects for an account

- **Response Body (200 OK):**
    ```json
    [
        {
            "accountId": "JewelTimeAccountID67890",
            "completedAt": "2017-08-24",
            "description": "Silver ring with a bezel set obsidian",
            "gemstones": "6x5 cm obsidian cabochon",
            "hoursSpent": "4.0",
            "jewelryType": "ring",
            "materials": "paste solder",
            "materialsCost": "190",
            "metals": "sterling silver 18ga sheet, 24K gold foil",
            "notes": "The ring band was wide and thick, had to use a ring bender.",
            "projectId": "JewelTimeProjectID12345",
            "projectName": "Moira's Statement Ring",
            "shape": "irregular",
            "startedAt": "2017-08-21"
        },
        {
            "accountId": "JewelTimeAccountID67890",
            "completedAt": "2021-02-24",
            "description": "Gold pendant with diamonds and freehand knit chain",
            "gemstones": "pave set 2mm brilliant cut diamonds",
            "hoursSpent": "150",
            "jewelryType": "necklace",
            "materials": "paste solder",
            "materialsCost": "2500",
            "metals": "18K gold 20ga sheet, 22K gold 24ga dead **soft** wire",
            "notes": "Handmade chain",
            "projectId": "JewelTimeProjectID6789",
            "projectName": "Moira's Statement Necklace",
            "shape": "round",
            "startedAt": "2020-01-05"
        }
    ]
    ```

### Update a Project

- **PUT/PATCH** `/projects/<projectId>`: Update a project

- **Request Body:**
    ```json
    {
        "hoursSpent": "15.5",
        "jewelryType": "ring",
        "materials": "paste solder, enamel",
        "materialsCost": "305.99",
        "metals": "sterling silver 18ga sheet, 24K gold foil"
    }
    ```

    **Note**: This endpoint allows for updates to the project information, including fields that do not need to be updated. If the values match the existing data, they will not be changed. Include all the fields you wish to include in the request, even if some of them may remain the same. 

- **Response Body (200 OK):**
    ```json
    {
        "accountId": "JewelTimeAccountID67890",
        "completedAt": "2017-08-24",
        "description": "Silver ring with a bezel set obsidian",
        "gemstones": "6x5 cm obsidian cabochon",
        "hoursSpent": "15.5",
        "jewelryType": "ring",
        "materials": "paste solder, enamel",
        "materialsCost": "305.99",
        "metals": "sterling silver 18ga sheet, 24K gold foil",
        "notes": "The ring band was wide and thick, had to use a ring bender.",
        "projectId": "JewelTimeProjectID12345",
        "projectName": "Moira's Statement Ring",
        "shape": "irregular",
        "startedAt": "2017-08-21"
    }
    ```

### Delete an Account

- **DELETE** `/projects/<projectId>`: Delete a project
  
- **Response Body (200 OK):**
    ```json
    {
        "message": "Project deleted successfully"
    }
    ```

### Metals

- **GET** `/prices`: Get current prices per troy ounce for four precious metals (gold, silver, platinum, and palladium)

- **Response Body (200 OK):**
    ```json
    [
        {
            "gold": "1903.85"
        },
        {
            "silver": "22.546"
        },
        {
            "platinum": "892.01"
        },
        {
            "palladium": "1238.44"
        },
        {
            "timestamp": 1692118415786
        }
    ]
    ```
    **Note:** This endpoint acts as a proxy to the [Metals Live API](https://api.metals.live/v1/spot) and fetches the current spot prices for these metals. Due to the reliance on this external API, it may take a while to receive a response.

    Users are free to utilize a different external API to fetch precious metal prices if they desire a faster or alternative source.

## Validation Schemas

- Account Schema
- Project Schema

### Accounts

An account within Jewel Time has the following fields:

- `accountId`: The unique account ID generated by MongoDB when a new account document is inserted into the database. It's a stringified copy of the ObjectId object created by MongoDB for internal use. (Read-only)
- `firebaseId`: The Firebase ID associated with the account, a string (Required)
- `firstName`: The first name of the account holder, a string (Required)
- `lastName`: The last name of the account holder, a string(Required)
- `email`: The email address associated with the account, a string (Required)
- `zipcode`: The zip code, a string of 3-10 characters, suitable for international users (Required)

These fields are validated to ensure proper formatting, such as email validation and zip code length.

### Projects

A project within Jewel Time can have the following fields, which can be added and modified:

- `accountId`: The account ID associated with the project, a string (Required)
- `projectId`: The unique project ID generated by MongoDB when a new project document is inserted into the database. It's a stringified copy of the ObjectId object created by MongoDB for internal use. (Read-only)
- `projectName`: The name of the project, a string (Required)
- `description`: A description of the project, a string of max 300 characters (Required)
- `startedAt`: The start date of the project in ISO format "YYYY-MM-DD", a string (Required)
- `completedAt`: The completion date of the project in ISO format "YYYY-MM-DD", a string (Optional)
- `hoursSpent`: The number of hours spent on the project, a string (Optional)
- `materialsCost`: The cost of materials used in the project, a string (Optional)
- `materials`: The materials used in the project, a string(Optional)
- `metals`: The metals used in the project, a string (Optional)
- `gemstones`: The gemstones used in the project, a string (Optional)
- `notes`: Additional notes related to the project, a string(Optional)
- `shape`: The shape of the jewelry, a string (Optional)
- `jewelryType`: The type of jewelry being crafted, a string(Optional)

These fields are validated according to specific requirements, such as the description length and the completion date must not be earlier than the start date.

## Installation

Fork, clone the repository, create and activate a virtual environment, then install dependencies:

```bash
git clone https://github.com/lyudarkim/back-end-jeweltime.git
cd back-end-jeweltime
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

To run the application locally, follow these steps:

1. Navigate to the project root directory in your terminal.

2. Execute the following command to start the Flask application:
   
   ```bash
   python3 run.py
    ```

Once the application is running, you can access it using a web browser or API testing tool.

**Local Development:** Visit `http://localhost:5000` or `http://127.0.0.1:5000` and append the desired endpoint to access the application.

**Deployed Version:** If you want to access the deployed version of the API, use the base URL instead: `https://jeweltime-api.onrender.com`. 

Please note that you should have the necessary dependencies installed and a functional MongoDB connection to run the application successfully.

## Testing MongoDB Connection

To test the connection to the MongoDB database, you can use the `connection.py` file in the project root.

## Contributing 

If you are interested in contributing to this project, please follow these steps:

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch
4. Make your changes and commit them
5. Push the changes to your fork
6. Submit a pull request with a description of the changes

For bug reports or feature requests, please open an issue on GitHub.

## License

This project is licensed under the MIT License.

