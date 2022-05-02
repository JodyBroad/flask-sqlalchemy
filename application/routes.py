from flask import render_template, request, flash, redirect, url_for, session
from application import app, db
from application.forms import EmailSignUpForm, CustomerRegistrationForm, StaffRegistrationForm, PlantForm,\
    NewBlogPostForm, LogInForm, AddToCartForm, DeleteBlogPostForm, SearchForm, OrderForm, UpdateEmailForm

from application.models import Person, Address, Newsletter, UserLogin, StaffInfo, Product, BlogPosts,\
    OrderHeader, OrderLine, OrderStatus, Category, PlantType, Size
from datetime import date


# newsletter sign up form for homepage
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def email_signup_form():
    error = ""
    form = EmailSignUpForm()

    if request.method == 'POST':
        email = form.email.data
        if len(email) == 0:
            error = "Please supply email address"
        else:
            news = Newsletter(newsletter_email=email)
            db.session.add(news)
            db.session.commit()
            flash(f'Success! {form.email.data} will now get our lovely email newsletter', 'success')
            return render_template('home.html', form=form, message=error, title='home')
    return render_template('home.html', form=form, message=error, title='home')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')

@app.route('/contact_us', methods=['GET'])
def contact():
    return render_template('contact_us.html', title='Contact Us')

@app.route('/plant_care', methods=['GET'])
def plant_care():
    posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
    return render_template('plant_care.html', title='Plant Care', posts=posts)

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    error = ""
    form = NewBlogPostForm()

    if form.validate_on_submit():
        flash(f' New Blog Post created called {form.title.data}!', 'success')

    if request.method == 'POST':
        title = form.title.data
        author = form.author.data
        post_content = form.post_content.data
        if len(title) == 0\
                or len(author) == 0\
                or len(post_content) == 0:
            error = "Please complete the fields"
        else:
            post = BlogPosts(title=title, author=author, post_content=post_content, date_posted=date.today())
            db.session.add(post)
            db.session.commit()
            posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
            return render_template('plant_care.html', title='Plant Care', posts=posts)

    return render_template('addpost.html', message= error, form=form)

# display specific blog post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPosts.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

# delete blog post

@app.route('/delete_blogpost', methods=['GET','POST'])
# @app.route('/delete_blogpost/<int:blogposts_id>', methods=['GET','DELETE'])
def delete_blogpost():
    error = ""
    form = DeleteBlogPostForm()

    if request.method == 'POST':
        # id_to_delete = form.id.data
        post = BlogPosts.query.get(form.id.data)
        # print(post)
        db.session.delete(post)
        db.session.commit()

        # deletion itself works but needs error handling added
        if not post:
            error = "There is no blog post with ID: " + str(form.id.data)

        posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
        flash(f' Blog post with id {form.id.data} deleted!', 'success')
        return render_template('plant_care.html', title='Plant Care', message=error, posts=posts, form=form)

    else:

        return render_template('delete_blogpost.html', title='Delete a blogpost', message= error, form=form)


# CUSTOMER RELATED ROUTES:

# REGISTERING A NEW CUSTOMER:


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = CustomerRegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
    else:
        return render_template('register.html', form=form)

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address_line_one = form.address_line_one.data
        address_line_two = form.address_line_two.data
        address_line_three = form.address_line_three.data
        postcode = form.postcode.data
        phone_number = form.phone_number.data

        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            address_line_one = form.address_line_one.data
            address_line_two = form.address_line_two.data
            address_line_three = form.address_line_three.data
            postcode = form.postcode.data
            phone_number = form.phone_number.data

        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(postcode) == 0\
                or len(password) < 4\
                or len(username) == 0:
            error = "Please complete each section of this form"
        else:
            user_login = UserLogin(username=username,
                                   password=password)
            address = Address(address_line_one=address_line_one,
                              address_line_two=address_line_two,
                              address_line_three=address_line_three,
                              postcode=postcode)
            person = Person(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            phone_number=phone_number,
                            person_type_id=2,
                            user_login=user_login)

            db.session.add(user_login)
            db.session.add(address)
            db.session.add(person)
            db.session.commit()
            return render_template('home.html', title='Home', message=error, form=form)
    return render_template('register.html', title='Register', message=error, form=form)


# ACCESSING A LIST OF CUSTOMERS

@app.route('/customer_list', methods=['GET'])
def show_customers():
    error = ""
    customer = Person.query.filter_by(person_type_id=2)
    # if len(customer) == 0:
    #     error = "There are no people to display"
    #     print(customer)
    return render_template('customer_list.html', customer=customer, message=error)


# STAFF RELATED ROUTES

# REGISTERING A NEW MEMBER OF STAFF:


@app.route('/register_staff', methods=['GET', 'POST'])
def register_staff():
    error = ""
    form = StaffRegistrationForm()

    if form.validate_on_submit():
        flash(f' Staff account created for {form.username.data}!', 'success')
    else:
        return render_template('register_staff.html', form=form)

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address_line_one = form.address_line_one.data
        address_line_two = form.address_line_two.data
        address_line_three = form.address_line_three.data
        postcode = form.postcode.data
        phone_number = form.phone_number.data
        job_title = form.job_title.data
        date_of_birth = form.date_of_birth.data

        # if messages left in for all form routes because may need to raise error here for validations that aren't currently showing
        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(postcode) == 0\
                or len(password) < 4\
                or len(username) == 0:
            error = "Please complete each section of this form"
        else:
            user_login = UserLogin(username=username,
                                   password=password)
            address = Address(address_line_one=address_line_one,
                              address_line_two=address_line_two,
                              address_line_three=address_line_three,
                              postcode=postcode)
            staff_info = StaffInfo(job_title=job_title,
                                   date_of_birth=date_of_birth)
            person = Person(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            phone_number=phone_number,
                            person_type_id=1,
                            user_login=user_login,
                            staff_info=staff_info)
            db.session.add(user_login)
            db.session.add(address)
            db.session.add(staff_info)
            db.session.add(person)
            db.session.commit()
            return render_template('home.html', title='Home', message=error, form=form)
    return render_template('register_staff.html', title='Register New Staff', message=error, form=form)


# ACCESSING A LIST OF CURRENT STAFF

@app.route('/staff_list', methods=['GET'])
def show_staff():
    error = ""
    staff = Person.query.filter_by(person_type_id=1)
    # if len(customer) == 0:
    #     error = "There are no people to display"
    #     print(customer)
    return render_template('staff_list.html', staff=staff, message=error)

# REGISTERING A NEW PLANT:


@app.route('/plant_form', methods=['GET', 'POST'])
def plant_form():
    error = ""
    form = PlantForm()

    if form.validate_on_submit():
        flash(f' Plant added!', 'success')

    if request.method == 'POST':
        # plant_name = form.plant_name.data
        plant_category = form.plant_category.data
        plant_species = form.plant_species.data
        plant_price = form.plant_price.data
        plant_stock = form.plant_stock.data
        plant_type = form.plant_type.data
        plant_size = form.plant_size.data

        if len(plant_category) == 0 \
                or plant_species == 0\
                or plant_price == 0\
                or plant_stock == 0:
            error = "Please complete the fields"
        else:
            product = Product(species=plant_species,
                              price=plant_price,
                              stock=plant_stock,
                              category_id=plant_category,
                              plant_type_id=plant_type,
                              size_id=plant_size)
            db.session.add(product)
            db.session.commit()
            return render_template('plant_form.html', title='Register a Plant', message=error, form=form)
    return render_template('plant_form.html', title='Register a Plant', message=error, form=form)

# session variables - login

@app.route('/login', methods=['GET', 'POST'])
@app.route('/log_in', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    error = ""
    # login_redirect = url_for('login')
    if request.method == 'POST':
        # pop previous session in case someone was already logged in
        session.pop('logged_in_username', default=None)
        session.pop('typesession', default=None)
        session.pop('logged_in', default=None)
        session.pop('id_number', default=None)
        session.pop('cart', default=None)

        # if form.validate_on_submit():

        # # taking the username and password from the form so that we can compare to the db
        form_username = request.form['username']
        form_password = request.form['password']

        db_username_password = UserLogin.query.filter_by(username=form_username, password=form_password).all()
        for user_id in db_username_password:
            user_id_for_session_variable = user_id.id

        # setting initial value of password_check to false:
        password_check = False

        if db_username_password != []:
            password_check = True
        else:
            password_check = False

        if password_check == True:

        # if validation has passed, save the username to the session object
            session['logged_in_username'] = request.form['username']
            session['logged_in'] = True
            session['id_number'] = user_id_for_session_variable

        # also need to check if they are a customer or staff, so need a another session variable
        # some sort of if statement needed here to check db and then:

        # this query gives you all the staff id numbers, can we then filter this based on username/id?
        # user_and_persontype = db.session.query(UserLogin, Person, StaffInfo).select_from(UserLogin).join(Person).join(StaffInfo).all()
        # print(user_and_persontype)


            # assigning type log in based on db not the dropdown:

            login_type = Person.query.filter_by(id=user_id_for_session_variable).all()
            for person in login_type:
                login_type_staff = person.person_type_id

            # print(login_type_staff)

            if login_type_staff == 1:
                # if person_type = 1 then:
                session['typesession'] = 'staff'
            else:
                session['typesession'] = 'customer'

            # not currently checking db, but will take the form input instead as a starting point:
            # if request.form['type'] == '1':
            #     # if person_type = 1 then:
            #     session['typesession'] = 'staff'
            # else:
            #     session['typesession'] = 'customer'

            # will then return different nav/functionality depending on which type of log in it is - this works

            # will show shop page plus session variable specific text
                return redirect(url_for('shop'))

        else:
            flash(f' Login failed, please try again', 'danger')
            # will just show basic shop page, no session data
            return redirect(url_for('shop'))
        # will display welcome message/session data and also navigation will change
        return redirect(url_for('shop'))

    #     if validation fails, return to log in page and flash message that it has failed
    #     return redirect(url_for('login'))

    return render_template('login.html', message= error, form=form)

# session variables - log out

@app.route('/log_out')
@app.route('/logout')
def delete_session():
    error = ""
    form = EmailSignUpForm()
    # Clear the username stored in the session object
    session.pop('logged_in_username', default=None)
    session.pop('typesession', default=None)
    session.pop('logged_in', default=None)
    session.pop('id_number', default=None)
    session.pop('cart', default=None)

    flash(f' You have logged out!', 'success')
    return render_template('home.html', title='Home', form=form, message=error,)

# session variables - shopping cart

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():

    error = ""
    form = AddToCartForm()

    # error message if user tries to press add to cart when not logged in
    if 'logged_in' not in session:

        flash(' Please Login to make a purchase', 'danger')
        return redirect(url_for('login'))
        # return render_template('login.html', title='Home', form=form, message=error)
        # return render_template('add_to_cart.html', form=form, message=error, title='home')

    headings = ('Image', 'Plant Name', 'Species', 'Price', 'Quantity', 'Sub-Total')

    # if request.method == 'POST':

    plant_id = int(request.referrer.split('/')[4])
    plant = Product.query.filter_by(id=plant_id).one()
    # product = form.product.data
    # quantity = form.quantity.data

    # price = [Product.query.filter_by(product).first()]
    # price = form.price.data
    # attributes = Product.query.filter_by(id=product).all()

    #
    # productAttributes = []

    # what if we nested dictionaries not lists?
    # productAttributes = {}
    attributeObject = {}
    # for attribute in plant:

    attributeObject['id'] = plant.id
    attributeObject['species'] = plant.species
    attributeObject['price'] = plant.price
    attributeObject['plant_nickname'] = plant.plant_nickname
    attributeObject['quantity'] = form.quantity.data
    attributeObject['sub_total'] = (plant.price * form.quantity.data)
    if 'cart' in session:
        # session['cart'].append(attributeObject)
        # below for loop merges duplicates when item added to the cart twice
        plantInCart = False
        for idx, cart_item in enumerate(session['cart']):
            if plant.id == cart_item['id']:
                session['cart'][idx]['quantity'] += form.quantity.data
                session['cart'][idx]['sub_total'] += plant.price * form.quantity.data
                plantInCart = True
        if not plantInCart:
            session['cart'].append(attributeObject)
        session.modified = True
    else:
        session['cart'] = [attributeObject]

    return render_template('cart_success.html', title='Cart', form=form, message=error, attributeObject=attributeObject, cart_contents=session['cart'], headings=headings, scroll='cart_top')
    # return render_template('cart.html', title='Cart', form=form, message=error, cart_contents=session['cart'], headings=headings)

# view cart
@app.route('/cart', methods=['GET', 'POST'])
def view_cart():
    error = ""
    # form was set to AddToCart() but trying to get ordering working
    form = OrderForm()
    if 'cart' in session:
        cart_contents = session['cart']
    else:
        cart_contents = []

    headings = ('Image', 'Plant Name', 'Species', 'Price', 'Quantity', 'Sub-Total')


    return render_template('cart.html', title='Cart', form=form, message=error, cart_contents=cart_contents, headings=headings)
    # return render_template('add_to_cart.html', form=form, message=error, title='home')

# empty cart (but will stay logged in)
@app.route('/clear_cart')
def clear_cart():
    error = ""
    form = EmailSignUpForm()
    # Clear the shopping cart in the session object
    session.pop('cart', default=None)

    flash(f' You have emptied your cart!', 'success')
    return render_template('home.html', title='Home', form=form, message=error,)


# error handling - custom 404 page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# order history - not quite working yet
@app.route('/customer_order_history', methods=['GET'])
def customer_order_history():
    error = ""
    person_id = session['id_number']
    headings = ('Order ID number', 'Order Status', 'Date of Order', 'Species', 'Quantity', 'Total Price')
    customer_order_history = db.session.query(OrderHeader, OrderStatus, OrderLine, Product).select_from(OrderHeader). \
        join(OrderStatus).join(OrderLine).join(Product).filter(OrderHeader.person_id == person_id).all()

    return render_template('order_history.html', title='Order History', customer_order_history=customer_order_history, message=error, headings=headings)


# Pass Stuff to Nav
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# create search function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = BlogPosts.query
    if form.validate_on_submit():

        # get data from submitted form
        post.searched = form.searched.data
        # Query the database
        posts = posts.filter(BlogPosts.post_content.like('%' + post.searched + '%'))
        posts = posts.order_by(BlogPosts.title).all()

        return render_template("search.html", form=form, searched=post.searched, posts=posts)


@app.route('/plant/<int:plant_id>')
def plant(plant_id):

    # form = AddToCartForm()

    plant = Product.query.filter_by(id=plant_id).one()

    return render_template('plant.html', title="Plant", plant=plant)


# STAFF ACCESS QUERIES

# QUERY - staff and corresponding job titles
# Gives list of staff members and their job titles
@app.route('/staff_jobs', methods=['GET'])
def staff_jobs():
    error = ""
    staff_and_jobs = db.session.query(StaffInfo, Person).join(Person).all()
    headings = ('Job Title', 'First Name', 'Last Name', 'Email')

    return render_template('staff_jobs.html', staff_and_jobs=staff_and_jobs, message=error, headings=headings)


# QUERY: customers and their orders
# Gives list of customer names, their order id and order date, the products ordered and the quantity
@app.route('/customer_orders', methods=['GET'])
def show_customer_orders():
    error = ""
    headings = ('Order ID number', 'Customer First Name', 'Customer Last Name', 'Date of Order', 'Order Status', 'Species', 'Quantity')
    customer_orders = db.session.query(Person, OrderHeader, OrderStatus, OrderLine, Product).select_from(Person).join(
        OrderHeader).join(OrderStatus).join(OrderLine).join(Product).all()

    return render_template('customer_orders.html', customer_orders=customer_orders, message=error, headings=headings)

# QUERY: Outstanding orders
@app.route('/outstanding_orders', methods=['GET'])
def show_outstanding_orders():
    error = ""
    headings = ('Order ID', 'Order Date', 'Order Status', 'Species', 'Quantity')
    outstanding_orders = db.session.query(OrderHeader, OrderStatus, OrderLine, Product).select_from(OrderHeader). \
        join(OrderStatus).join(OrderLine).join(Product).filter(OrderStatus.id == 1).all()
    return render_template('outstanding_orders.html', outstanding_orders=outstanding_orders, message=error, headings=headings)

# current stock list for staff query
@app.route('/stock_list', methods=['GET'])
def stock_list():
    headings = ('Species', 'Environment', 'Size', 'Plant Type', 'Price', 'In Stock')
    plant_shop_plant = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).order_by(Product.species.asc()).all()
    return render_template('stock_list.html', title='Stock List', plant_shop_plant=plant_shop_plant, headings=headings)

# CUSTOMER ACCESS QUERIES

# PLANT SHOP PAGE

# MAIN SHOP PAGE
@app.route('/shop', methods=['GET'])
def shop():
    plant_shop_plant = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).all()
    return render_template('shop.html', title='Plant Shop', plant_shop_plant=plant_shop_plant)

@app.route('/plant/<int:product_id>')
def product_store(product_id):
    plant = Product.query.filter_by(id=product_id).one()

    return render_template('plant.html', plant=plant)

# QUERY: Indoor plants
@app.route('/indoor_plants', methods=['GET'])
def show_indoor_plants():
    error = ""
    display_indoor_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Category.id == 1).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_indoor_plants=display_indoor_plants, message=error, scroll='filters')

# QUERY: Outdoor plants
@app.route('/outdoor_plants', methods=['GET'])
def show_outdoor_plants():
    error = ""
    display_outdoor_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Category.id == 2).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_outdoor_plants=display_outdoor_plants, message=error, scroll='filters')

# QUERY: filter by height - tiny
@app.route('/tiny_plants', methods=['GET'])
def show_tiny_plants():
    error = ""
    display_tiny_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Size.id == 1).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_tiny_plants=display_tiny_plants, message=error, scroll='filters')

# QUERY: filter by height - small
@app.route('/small_plants', methods=['GET'])
def show_small_plants():
    error = ""
    display_small_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Size.id == 2).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_small_plants=display_small_plants, message=error, scroll='filters')

# QUERY: filter by height - medium
@app.route('/medium_plants', methods=['GET'])
def show_medium_plants():
    error = ""
    display_medium_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Size.id == 3).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_medium_plants=display_medium_plants, message=error, scroll='filters')


# QUERY: filter by height - tall
@app.route('/tall_plants', methods=['GET'])
def show_tall_plants():
    error = ""
    display_tall_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Size.id == 4).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_tall_plants=display_tall_plants, message=error, scroll='filters')


# QUERY: filter by type - cactus / succulent
@app.route('/cacti_succulent_plants', methods=['GET'])
def show_cacti_succulent_plants():
    error = ""
    display_cacti_succulent_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(PlantType.id == 1).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_cacti_succulent_plants=display_cacti_succulent_plants, message=error, scroll='filters')


# QUERY: filter by type - hanging
@app.route('/hanging_plants', methods=['GET'])
def show_hanging_plants():
    error = ""
    display_hanging_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(PlantType.id == 2).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_hanging_plants=display_hanging_plants, message=error, scroll='filters')


# QUERY: filter by type - flowering
@app.route('/flowering_plants', methods=['GET'])
def show_flowering_plants():
    error = ""
    display_flowering_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(PlantType.id == 3).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_flowering_plants=display_flowering_plants, message=error, scroll='filters')


# QUERY: filter by type - palm
@app.route('/palm_plants', methods=['GET'])
def show_palm_plants():
    error = ""
    display_palm_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(PlantType.id == 4).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_palm_plants=display_palm_plants, message=error, scroll='filters')


# QUERY: filter by type - fern
@app.route('/fern_plants', methods=['GET'])
def show_fern_plants():
    error = ""
    display_fern_plants = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(PlantType.id == 5).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_fern_plants=display_fern_plants, message=error, scroll='filters')

# QUERY: filter by price
@app.route('/value_savers', methods=['GET'])
def show_value_saver():
    error = ""
    display_value_saver = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Product.price < 10).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_value_saver=display_value_saver, message=error, scroll='filters')

# QUERY: filter by price
@app.route('/modest_picks', methods=['GET'])
def show_modest_picks():
    error = ""
    display_modest_picks = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Product.price < 25).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_modest_picks=display_modest_picks, message=error, scroll='filters')

# QUERY: filter by price
@app.route('/fancy_picks', methods=['GET'])
def show_fancy_picks():
    error = ""
    display_fancy_picks = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Product.price < 55).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_fancy_picks=display_fancy_picks, message=error, scroll='filters')


# QUERY: filter by price
@app.route('/premium_range', methods=['GET'])
def show_premium_range():
    error = ""
    display_premium_range = db.session.query(Product, Category, PlantType, Size).select_from(Product). \
        join(Category).join(PlantType).join(Size).filter(Product.price > 56).order_by(Product.price.desc()).all()
    return render_template('shop.html', display_premium_range=display_premium_range, message=error, scroll='filters')


# Place an Order
@app.route('/complete_order', methods=['GET', 'POST'])
def complete_order():
    error = ""
    form = OrderForm()

    # if form.validate_on_submit():
    #     flash(f' Order placed!', 'success')
    # else:
    #     return render_template('cart.html', form=form)

    if request.method == 'POST':
        cart_contents = session['cart']
        # print("cart contents", cart_contents)
        # cart_contents is a list with multiple dictionaries in (if more than one type of item in the cart)
        total_cost = 0
        # iterate through the dictionaries to get the values needed
        for item in cart_contents:
            person_id = session['id_number']
            order_date = date.today()
            status_id = 1
            product_id = item['id']
            quantity = item['quantity']
            price_per_item= item['price']
            price_paid = price_per_item * quantity
            total_cost += price_paid # need to work out how to get this from the shopping cart is going to be sum of all subtotals


        # if messages left in for all form routes because may need to raise error here for validations that aren't currently showing
        # if len(first_name) == 0 \
        #         or len(last_name) == 0 \
        #         or len(email) == 0\
        #         or len(address_line_one) == 0\
        #         or len(postcode) == 0\
        #         or len(password) < 4\
        #         or len(username) == 0:
        #     error = "Please complete each section of this form"
        # else:


        order_header = OrderHeader(person_id=person_id, order_date=order_date, status_id=status_id,
                                   total_cost=total_cost)

        order_line = OrderLine(order_header=order_header, product_id=product_id, quantity=quantity, price_paid=price_paid)


        db.session.add(order_header)
        db.session.add(order_line)

        db.session.commit()
        #  clears the cart as transaction is complete
        session.pop('cart', default=None)
        flash(f' Order successfully placed, enjoy your new plant friends!', 'success')

        return render_template('home.html', title='Home', message=error, form=EmailSignUpForm())
    return render_template('complete_order.html', title='Complete Order', message=error, form=form)

@app.route('/update_customer_email', methods=['POST', 'GET'])
# @app.route('/customer/<int:person_id>/<string:new_email>', methods=['PUT', 'GET'])
def update_customer_email():
    error = ""
    form = UpdateEmailForm()
    person_id = session['id_number']
    new_email = form.new_email.data

    if form.validate_on_submit():
        flash(f'Email address update to {form.new_email.data}!', 'success')
    else:
        return render_template('update_email.html', form=form)

    if request.method == 'POST':
        person = Person.query.get(person_id)
        person.email = new_email
        db.session.commit()

        return redirect(url_for('shop'))
    return render_template('update_email.html', form=form, person_id=person_id, message=error, title='Update Email')
