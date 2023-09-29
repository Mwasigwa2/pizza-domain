# Project Name: Pizza-Restaurant RESTful API

**Project Description:** 
This project is a RESTful API for managing pizza restaurants and their menus. It allows restaurant owners to add their pizzas to the system and provides users with information about restaurants and their pizzas.

## Table of Contents

- [Project Name: Pizza-Restaurant RESTful API](#project-name-pizza-restaurant-restful-api)
  - [Project Description](#project-description)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  

## Introduction

This project aims to simplify the management of pizza restaurants and their menus. It provides an API for adding, retrieving, and updating information about restaurants and the pizzas they offer. Whether you're a restaurant owner or a pizza lover, this API makes it easy to interact with pizza-related data.

## Features

- **User Authentication**: Securely create accounts and log in.
- **Restaurant Listing**: View a list of restaurants with details.
- **Pizza Menu**: Access menus of pizzas available at each restaurant.
- **Adding Restaurant Pizzas**: Allow restaurant owners to add their pizzas to the system.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Ensure you have the following software installed:

- Python 3.8+
- Flask
- SQLAlchemy

### Installation

1. Clone the repository:

```bash
        git clone https://github.com/Abogeerick/pizza-domain.git

 ```
2. Move into the repository
```bash
        cd pizza-restaurant-api
```
## Usage

1. Start the server by running python app.py.
2. Open a web browser and go to http://localhost:5555.
3. You will see the homepage of the Pizza-Restaurant RESTful API.
4. Create an account and log in to access additional features.

## Working with Routes

1. **View Home**:
    - **Endpoint**: `/`
    - **Method**: `GET`
    - **Description**: Returns a welcome message.
    - **Example**: `http://localhost:5555/`

2. **View All Restaurants**:
    - **Endpoint**: `/restaurants`
    - **Method**: `GET`
    - **Description**: Returns a list of all restaurants.
    - **Example**: `http://localhost:5555/restaurants`

3. **View Restaurant by ID**:
    - **Endpoint**: `/restaurants/<int:id>`
    - **Method**: `GET`
    - **Description**: Returns details of a specific restaurant based on ID.
    - **Example**: `http://localhost:5555/restaurants/1`

4. **Delete Restaurant by ID**:
    - **Endpoint**: `/restaurants/<int:id>`
    - **Method**: `DELETE`
    - **Description**: Deletes a specific restaurant based on ID.
    - **Example**: `http://localhost:5555/restaurants/1`

5. **View All Pizzas**:
    - **Endpoint**: `/pizzas`
    - **Method**: `GET`
    - **Description**: Returns a list of all pizzas.
    - **Example**: `http://localhost:5555/pizzas`

6. **View All Restaurant Pizzas**:
    - **Endpoint**: `/restaurant_pizzas`
    - **Method**: `GET`
    - **Description**: Returns a list of all restaurant pizzas.
    - **Example**: `http://localhost:5555/restaurant_pizzas`

7. **Add New Restaurant Pizza**:
    - **Endpoint**: `/restaurant_pizzas`
    - **Method**: `POST`
    - **Description**: Add a new restaurant pizza.
    - **Data Params**:
      - `price: [integer]`
      - `pizza_id: [integer]`
      - `restaurant_id: [integer]`
    - **Example**: `http://localhost:5555/restaurant_pizzas`

Use Postman or any API testing tool to test these routes.




## Contributing
We welcome contributions from the community. 
Please follow our contributing guidelines for more details.

## License
This project is licensed under the MIT License.
