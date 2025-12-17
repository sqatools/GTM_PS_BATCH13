from ...session_data import ENV
if ENV == 'prod':
    website_url = "https://sqatools.in/dummy-booking-website/"
elif ENV == 'TEST':
    website_url = "https://test.sqatools.in/dummy-booking-website/"
from_city_name = "Mumbai"
dest_city_name = "Pune"
billing_name = "Rahul"
billing_phone = 78979879878
user_dob = "12/11/2000"
traveller_details = "Add 2 more passenger (200%)"
