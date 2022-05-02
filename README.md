# Welcome to our Final Project for Sky's Get Into Tech Program
This application is a Python Flask web app that uses Jinja templates and SQLAlchemy to create a website for a fictional houseplant retail company.

## Key Functionality
- Register as a new Customer
- Log in as Staff or Customer
- A basic dynamically generated Blog
- Staff can add new Staff, Customers, Plants or Blogposts
- Staff can delete Blogposts
- Staff can run queries on Staff, Customer Orders, Stock and Orders to be Shipped
- Customers can view their Order History
- Customers can also update their Email Address
- Dynamically rendered Shop that can be Filtered on several criteria
- Fully functional Shopping Basket 
- Can add multiple items, clear cart etc
- Customer can then Checkout to make a purchase and complete an Order 
- This is then written to the DB for staff to pick and ship.

## Setup
Open MySQL Workbench and create a new database, called for example _team_yellow_.

```sql
create database team_yellow;
```

Edit the following line of code in **__init__.py** to the _user_, _password_ and _database_ you wish to use:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/team_yellow"
```

Run **create.py** to drop, create and populate the database tables with initial data.

## Run
To start the Flask app, run **app.py**.

