from application import db  # import the sqlalchemy object (db) created for our app

# Blog posts
class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    post_content = db.Column(db.String(1000), nullable=False)

# Newsletter signup
class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    newsletter_email = db.Column(db.String(120), nullable=False)

# PersonType linking to Person
class PersonType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_type_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but PersonType table links back to Person(can use to set permissions
    # in later iteration)
    person_type = db.relationship('Person', backref='person_type')


# UserLogin linking to Person
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # not field in table but relationship between userlogin and person
    user_login = db.relationship('Person', backref='user_login')


# address linking to person
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line_one = db.Column(db.String(50), nullable=False)
    address_line_two = db.Column(db.String(50), nullable=True)
    address_line_three = db.Column(db.String(50), nullable=True)
    address_line_four = db.Column(db.String(50), nullable=True)
    postcode = db.Column(db.String(50), nullable=False)
    # relationship between address and customer table - several people may have the same address
    address = db.relationship('Person', backref='address')


# Staff Info - allows us to record extra info about staff, but also gives them staff ID number to use to assign
# to orders for packing etc
class StaffInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    staff_info = db.relationship('Person', backref='staff_info')



# Person linking to address userlogin and orderheader
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    # address_id is the Foreign Key linking to the Address table
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    # user_login_id is linking back for username and password purposes
    user_login_id = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=False)
    person_type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)
    staff_info_id = db.Column(db.Integer, db.ForeignKey('staff_info.id'), nullable=True)
    # not a field in the table, but OrderHeader table links back to PersonID
    person_id = db.relationship('OrderHeader', backref='person')


class OrderStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but OrderStatus table links back to OrderHeader
    order_status = db.relationship('OrderHeader', backref='order_status')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but Category table links back to Product
    category = db.relationship('Product', backref='category')


class PlantType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_type_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but PlantType table links back to Product
    plant_type = db.relationship('Product', backref='plant_type')


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but Size table links back to Product
    size = db.relationship('Product', backref='size')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), nullable=False)
    # is this the right data type to store number to 2 decimal places?
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    plant_type_id = db.Column(db.Integer, db.ForeignKey('plant_type.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    plant_nickname = db.Column(db.String(50), nullable=False)
    general_info = db.Column(db.String(200), nullable=False)
    care_tip1 = db.Column(db.String(100), nullable=False)
    care_tip2 = db.Column(db.String(100), nullable=True)
    care_tip3 = db.Column(db.String(100), nullable=True)
    img_link1 = db.Column(db.String(200), nullable=False)
    img_link2 = db.Column(db.String(200), nullable=True)
    img_link3 = db.Column(db.String(200), nullable=True)
    tech_description = db.Column(db.String(400), nullable=False)
    # not a field in the table, but OrderLine table links back to Product
    product = db.relationship('OrderLine', backref='product')

class OrderHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    # not totally sure how we do dates, check this
    order_date = db.Column(db.Date, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'), nullable=False)
    # also what is best data type for price data?
    total_cost = db.Column(db.Integer)
    # staff_id = db.Column(db.Integer, db.ForeignKey('StaffInfo.id'), nullable=False)
    # staff_id = db.Column(db.Integer, db.ForeignKey('person.staff_info_id'), nullable=False)
    # not a field in the table, but OrderLine table links back to OrderHeader
    order_header = db.relationship('OrderLine', backref='order_header')


class OrderLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_header_id = db.Column(db.Integer, db.ForeignKey('order_header.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    # also what is best data type for price data?
    price_paid = db.Column(db.Integer)
