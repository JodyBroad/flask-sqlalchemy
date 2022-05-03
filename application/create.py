# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db

from application.models import BlogPosts, Newsletter, PersonType, UserLogin,  Address, StaffInfo, Person, OrderStatus, \
    Category, PlantType, Size,\
    Product, OrderHeader, OrderLine

db.drop_all()
db.create_all()

# Blogposts table
blog1 = BlogPosts(author='The Plant Doctor', date_posted='2022-01-01', title='Welcome', post_content='Hi, we are the '
                                                                'Plant Emporium, and we just want to welcome you to our shiny new website! It has taken a lot of blood, sweat and tears to get to this point and we cannot believe it is all actually working now.')
blog2 = BlogPosts(author='Master of the Retail Outlet', date_posted='2022-03-16', title='Exciting News', post_content='The shop is now officially open! We have a delightful new physical retail space, located in the heart of Sky Studios in Isleworth. After all the renovation work we have done, we cannot wait to show off the space! Come and see us to get your plant fix, we have some gorgeous stock and are happy to help you choose the perfect new planty companion.')
blog3 = BlogPosts(author='The Plant Doctor', date_posted='2022-04-30', title='Plant Clinic', post_content='We are now going to be running Sad Plant Fridays - post your ailing plants to Twitter #SadPlantFridays or email us at jody@theplantemporium.com and our resident Plant Doctor will diagnose the issue and more importantly, offer a solution! The Plant Doctor has years of experience in diagnosing and treating all manner of plant ailments, and firmly believes that we should Never Say Die! Well, unless the plant is really SUPER dead of course.')
blogs = [blog1, blog2, blog3]

# Newsletter signup table
news1 = Newsletter(newsletter_email='ted.lasso@afc_richmond.co.uk')
news2 = Newsletter(newsletter_email='rebecca_welton@gmail.com')
news3 = Newsletter(newsletter_email='keeley_jones@gmail.com')
news4 = Newsletter(newsletter_email='roy.kent@afc_richmond.co.uk')
news5 = Newsletter(newsletter_email='sam.obisanya@afc_richmond.co.uk')
news = [news1, news2, news3, news4, news5]

# PersonType table
person_type1 = PersonType(person_type_description='Staff')
person_type2 = PersonType(person_type_description='Customer')
person_types = [person_type1, person_type2]

# user login without person type
user1 = UserLogin(username='tedlikesplants', password='1buyingaPLANT!')
user2 = UserLogin(username='rebecca_w', password='Panda42')
user3 = UserLogin(username='keeley.jones', password='passworDx4')
user4 = UserLogin(username='roy.kent', password='Richmond12')
user5 = UserLogin(username='sam_obisanya', password='FootballandPlants1')
user6 = UserLogin(username='natasha', password='staffaccess4')
user7 = UserLogin(username='jodie', password='staffaccess4')
user8 = UserLogin(username='jody', password='staffaccess4')
user9 = UserLogin(username='isabel', password='staffaccess4')
users = [user1, user2, user3, user4, user5, user6, user7, user8, user9]


# address table
address1 = Address(address_line_one='AFC Richmond Club House', address_line_two='Nelson Road',
                   address_line_three='London', postcode='TW9 4RP')
address2 = Address(address_line_one='49 Kings Road', address_line_two='Chelsea', address_line_three='London',
                   postcode='SW3 5TT')
address3 = Address(address_line_one='4 Portland Terrace', address_line_two='The Green', address_line_three='Richmond',
                   postcode='TW9 1QQ')
address4 = Address(address_line_one='The Plant Emporium', address_line_two='Sky Studios', postcode='TW7 5QD')
addresses = [address1, address2, address3, address4]


# staff info table
staff1 = StaffInfo(job_title='Plant purchaser', date_of_birth='1994-06-23')
staff2 = StaffInfo(job_title='Website wrangler', date_of_birth='1998-09-12')
staff3 = StaffInfo(job_title='Plant doctor', date_of_birth='1984-05-26')
staff4 = StaffInfo(job_title='Master of the retail outlet', date_of_birth='1999-08-16')
staff = [staff1, staff2, staff3, staff4]

# person table
person1 = Person(first_name='Ted', last_name='Lasso', email='ted.lasso@afc_richmond.co.uk', address_id=1,
                     phone_number='07384957162', user_login_id=1, person_type_id=2)
person2 = Person(first_name='Rebecca', last_name='Welton', email='rebecca_welton@gmail.com', address_id=1,
                     phone_number='07492750173', user_login_id=2, person_type_id=2)
person3 = Person(first_name='Keeley', last_name='Jones', email='keeley_jones@gmail.com', address_id=2,
                     phone_number='07553630090', user_login_id=3, person_type_id=2)
person4 = Person(first_name='Roy', last_name='Kent', email='roy.kent@afc_richmond.co.uk', address_id=3,
                     phone_number='07554124856', user_login_id=4, person_type_id=2)
person5 = Person(first_name='Sam', last_name='Obisanya', email='sam.obisanya@afc_richmond.co.uk', address_id=1,
                     phone_number='07889578112', user_login_id=5, person_type_id=2)
person6 = Person(first_name='Natasha', last_name='Edun', email='natasha@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=6, person_type_id=1, staff_info_id=1)
person7 = Person(first_name='Jodie', last_name='Smith', email='jodie@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=7, person_type_id=1, staff_info_id=2)
person8 = Person(first_name='Jody', last_name='Broad', email='jody@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=8, person_type_id=1, staff_info_id=3)
person9 = Person(first_name='Isabel', last_name='Tulloch', email='isabel@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=9, person_type_id=1, staff_info_id=4)
persons = [person1, person2, person3, person4, person5, person6, person7, person8, person9]

# order status
status1 = OrderStatus(status_description='Ordered')
status2 = OrderStatus(status_description='Processing')
status3 = OrderStatus(status_description='Shipped')
status4 = OrderStatus(status_description='Collected')
status5 = OrderStatus(status_description='Returned')
status = [status1, status2, status3, status4, status5]

# category
category1 = Category(category_description='Indoor')
category2 = Category(category_description='Outdoor')
categories = [category1, category2]

# plant type table
plant1 = PlantType(plant_type_description='Cacti/Succulent')
plant2 = PlantType(plant_type_description='Hanging')
plant3 = PlantType(plant_type_description='Flowering')
plant4 = PlantType(plant_type_description='Palms')
plant5 = PlantType(plant_type_description='Ferns')
plant_types = [plant1, plant2, plant3, plant4, plant5]

# size
size1 = Size(size_description='Tiny')
size2 = Size(size_description='Small')
size3 = Size(size_description='Medium')
size4 = Size(size_description='Tall')
sizes = [size1, size2, size3, size4]

# product table
product1 = Product(species='Boston Fern', price=12, stock=8, category_id=1, plant_type_id=5, size_id=1, plant_nickname="Wendy", general_info="Sword fern - Nephrolepis exaltata", care_tip1="Frequent watering", care_tip2="Most light conditions", care_tip3="Humidity", img_link1="images/boston_fern_bush.jpg", img_link2="images/boston_fern_single.jpg", img_link3="", tech_description="Dame Wendy Hall is a British computer scientist, well known for her development of the Microcosm hypermedia systenm in the mid-1980's, which was a forerunner ot the World Wide Web.")
product2 = Product(species='Aloe Vera', price=4, stock=10, category_id=1, plant_type_id=1, size_id=2, plant_nickname="Annie", general_info="Aloe barbadensis", care_tip1="Light watering", care_tip2="Bright light", care_tip3="Warmth", img_link1="images/aloe_vera.jpg", img_link2="images/aloe_vera_hand.jpg", img_link3="images/aloe_vera_pot.jpg", tech_description="Annie Easley was an American computer scientist, mathematician, and rocket scientist. She was a leading member of the team which developed software for the Centaur rocket stage, and was one of the first African-Americans to work at NASA.")
product3 = Product(species='Parlour Palm', price=8.99, stock=3, category_id=1, plant_type_id=4, size_id=2, plant_nickname="Hedy", general_info="Chamaedorea elegans; Neanthe bella palm", care_tip1="Frequent watering", care_tip2="Medium light", care_tip3="Humidity", img_link1="images/parlour_palm.jpg", img_link2="images/parlour_palm_close.jpg", img_link3="images/parlour_palm_zoomout.jpg", tech_description="Hedy LaMarr patented frequency-hopping technology in 1941 that became a precursor to the secure wi-fi, GPS and Bluetooth now used by billions of people around the world.")
product4 = Product(species='Anthurium', price=20, stock=5, category_id=1, plant_type_id=3, size_id=3, plant_nickname="Grace", general_info="Tail flower; Flamingo flower; Laceleaf; Anthurium Andraeanum", care_tip1="Light watering", care_tip2="Medium light", care_tip3="Humidity", img_link1="images/anthurium.jpg", img_link2="images/anthurium_pot.jpg", img_link3="images/anthurium_white.jpg'", tech_description="Grace Hopper was a well known pioneer of computer programming. She was the first to devise the theory of machine-independent programming languages, and the FLOW-MATIC programming language she created using this theory was later extended to create COBOL - an early high-level programming language still in use today.")
product5 = Product(species='Swiss Cheese Plant', price=85.5, stock=1, category_id=1, plant_type_id=4, size_id=4, plant_nickname="Ada", general_info="Monstera Deliciosa; Ceriman; Custard plant; Indian ivy; Fruit salad plant; Mexican breadfruit; Cheese plant", care_tip1="Light watering", care_tip2="Medium light", care_tip3="Humidity", img_link1="images/swiss_cheese_plant.jpg", img_link2="images/swiss_cheese_plant_close.jpg", img_link3="images/swiss_cheese_plant_small.jpg", tech_description="Ada Lovelace was an English mathematician and writer, chiefly known for her work on Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine. She was the first to recognise that the machine had applications beyond pure calculation, and to have published the first algorithm intended to be carried out by such a machine.")
product6 = Product(species='Sweet Orange Tree', price=65, stock=4, category_id=2, plant_type_id=3, size_id=4, plant_nickname="Roberta", general_info="Citrus Sinensis", care_tip1="Light watering", care_tip2="Bright light", care_tip3="Moist Soil", img_link1="images/sweet_orange_tree_1.jpg", img_link2="images/sweet_orange_tree_2.jpg", img_link3="images/sweet_orange_tree_3.jpg", tech_description="Roberta Williams is an American video game designer and writer, who co-founded Sierra On-Line, and became credited as the first graphic adventure game.")
product7 = Product(species='Climbing Rose', price=30, stock=3, category_id=2, plant_type_id=3, size_id=3, plant_nickname="Elizabeth", general_info="Rosa", care_tip1="Frequent watering", care_tip2="Partial sun", care_tip3="Moist Soil", img_link1="images/climbing_rose_1.jpg", img_link2="images/climbing_rose_2.jpg", img_link3="images/climbing_rose_3.jpg", tech_description="Elizabeth J Feinler is an information scientist who laid the foundations for how the internet is structured, including the Domain Name System (DNS).")
product8 = Product(species='Fatsia Japonica', price=55, stock=2, category_id=2, plant_type_id=5, size_id=3, plant_nickname="Valerie", general_info="Glossy-leaf paper plant; Fatsi; Paperplant; Japanese aralia", care_tip1="Medium watering", care_tip2="Partial sun", care_tip3="Moist Soil", img_link1="images/fatsia_japonica_berry.jpg", img_link2="images/fatsia_japonica_leaf.jpg", img_link3="", tech_description="Valerie Thomas is the inventor of the illusion transmitter. Valerie changed the way we consume content as she managed the development of NASA’s image-processing system for Landsat, the first satellite to send images from outer space. This is widely considered to be the basis for 3D technology.")
product9 = Product(species='Hydrangea Macrophylla', price=29.99, stock=5, category_id=2, plant_type_id=3, size_id=2, plant_nickname="Shirley", general_info="Mophead Hydrangea, French Hydrangea, Hortensia", care_tip1="Frequent watering", care_tip2="Partial sun", care_tip3="Moist Soil", img_link1="images/hydrangea_dusky_pink.jpg'", img_link2="images/hydrangea_hot_pink.jpg'", img_link3="images/hydrangea_white.jpg", tech_description="Dr Shirley Jackson was the first African American woman to earn a doctorate in nuclear physics at MIT. Her experiments led the way for numerous developments in the telecommunication space, including the invention of fibre-optic cables that link the world’s communication system.")
product10 = Product(species='Alstroemeria', price=27, stock=8, category_id=2, plant_type_id=3, size_id=1, plant_nickname="Victoria", general_info="Lily of the Incas", care_tip1="Light watering", care_tip2="Bright light", care_tip3="Warmth", img_link1="images/alstromeria_pink.jpg", img_link2="images/alstromeria_purple.jpg", img_link3="images/alstromeria_yellow.jpg", tech_description="Victoria Lloyd is a leading coding instructor, currently teaching women from across the UK how to code. She leads numerous cohorts of women looking to career switch, upskill and kickstart their coding journey, mentoring and advising on how to access the technology and software development fields.")
products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

# OrderHeader linking to person only (as customer)
order1 = OrderHeader(person_id=1, order_date='2022-04-09', status_id=1, total_cost=54.00)  # staff_id=1)
order2 = OrderHeader(person_id=2, order_date='2022-04-10', status_id=4, total_cost=26.97)  # staff_id=2)
order3 = OrderHeader(person_id=3, order_date='2022-04-12', status_id=3, total_cost=197.97)  # staff_id=3)
order4 = OrderHeader(person_id=4, order_date='2022-04-16', status_id=4, total_cost=20.00)  # staff_id=4)
order5 = OrderHeader(person_id=1, order_date='2022-04-19', status_id=4, total_cost=195.00)  # staff_id=1)
order6 = OrderHeader(person_id=4, order_date='2022-04-18', status_id=5, total_cost=105.00)  # staff_id=1)
order7 = OrderHeader(person_id=4, order_date='2022-04-21', status_id=3, total_cost=172.48)  # staff_id=1)
order8 = OrderHeader(person_id=4, order_date='2022-04-30', status_id=1, total_cost=12)  # staff_id=1)
plant_orders = [order1, order2, order3, order4, order5, order6, order7, order8]

# orderLine
order_line1 = OrderLine(order_header_id=1, product_id=10, quantity=2, price_paid=54.00)
order_line2 = OrderLine(order_header_id=2, product_id=3, quantity=1, price_paid=26.97)
order_line3 = OrderLine(order_header_id=3, product_id=5, quantity=2, price_paid=171.00)
order_line4 = OrderLine(order_header_id=3, product_id=4, quantity=4, price_paid=80.00)
order_line5 = OrderLine(order_header_id=4, product_id=2, quantity=2, price_paid=8.00)
order_line6 = OrderLine(order_header_id=4, product_id=1, quantity=1, price_paid=12.00)
order_line7 = OrderLine(order_header_id=5, product_id=6, quantity=3, price_paid=195.00)
order_line8 = OrderLine(order_header_id=6, product_id=8, quantity=1, price_paid=55.00)
order_line9 = OrderLine(order_header_id=6, product_id=7, quantity=2, price_paid=60.00)
order_line10 = OrderLine(order_header_id=7, product_id=10, quantity=1, price_paid=27.00)
order_line11 = OrderLine(order_header_id=7, product_id=9, quantity=2, price_paid=59.98)
order_line12 = OrderLine(order_header_id=7, product_id=5, quantity=1, price_paid=85.50)
order_line13 = OrderLine(order_header_id=8, product_id=2, quantity=3, price_paid=12.00)
order_lines = [order_line1, order_line2, order_line3, order_line4, order_line5, order_line6, order_line7, order_line8, order_line9, order_line10, order_line11, order_line12, order_line13]

db.session.add_all(blogs)
db.session.add_all(news)
db.session.add_all(person_types)
db.session.add_all(users)
db.session.add_all(addresses)
db.session.add_all(staff)
db.session.add_all(persons)
db.session.add_all(status)
db.session.add_all(categories)
db.session.add_all(plant_types)
db.session.add_all(sizes)
db.session.add_all(products)
db.session.add_all(plant_orders)
db.session.add_all(order_lines)

db.session.commit()
