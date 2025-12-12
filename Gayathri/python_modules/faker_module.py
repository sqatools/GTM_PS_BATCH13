#generate data for testing - generating test data
#need to install faker module first - pip install faker

from faker import Faker

import openpyxl
#here Faker is the class
fake = Faker() #here creating the object of the Faker Class

#now lets say we need some details of the user
print("First Name:", fake.first_name()) #First Name: Emma
print("Last Name:", fake.last_name()) #Last Name: Brown
print("Email ID:", fake.email()) #Email ID: geraldhughes@example.org
print("Phone:", fake.phone_number()) #Phone: (556)554-9724x08622
print("Date of Birth:", fake.date_of_birth())  #Date of Birth: 2017-10-26
#print("Age:", fake.age()) #getting erorr -  # return getattr(self._factories[0], attr)
#AttributeError: 'Generator' object has no attribute 'age'
#print("Gender:", fake.gender()) # File "C:\Users\Sriram\AppData\Roaming\Python\Python313\site-packages\faker\proxy.py", line 130, in __getattr__
    #return getattr(self._factories[0], attr)
#AttributeError: 'Generator' object has no attribute 'gender'

print("*"*50)
#above data is for one user. every time we run we get differnt data
#but we want say for 50 users, so lets add this n for loop
def create_user_data_in_text():
    for i in range(1,50):
        print("count of users:", i)
        print("Name:", fake.name())
        print("Address:", fake.address())
        print("Email:", fake.email())
        print("Phone:", fake.phone_number())
        print("*"*50)

        # let the data be created in a single line - slets give teh format
        user_data = f"{fake.name()},{fake.address()},{fake.email()},{fake.phone_number()}\n"
        # \n - so that each data set goes to next line

        # now lets add these details in a text file with comma seperated values
        with open("user_details.txt", "a") as file:  # a - append mode
            file.write(user_data)  # here we are writing the user data to teh file

create_user_data_in_text()
"""
count of users: 1
Name: Dean Hampton
Address: 67194 Fowler Burg Suite 789
Lisamouth, IN 58600
Email: allenjennifer@example.com
Phone: 531-272-4286
"""

#to write to an execl file -import openpyxl first
def create_users_data_in_excel(file_path):
    cell_no = 1
    for i in range(1,100):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb["Test_Data"]
        cell1= sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]
        cell1.value = fake.name()
        cell2.value = fake.address()
        cell3.value = fake.email()
        cell4.value = fake.phone_number()
        wb.save(file_path)
        cell_no += 1
#above we created teh file in the path along with the sheet name and the dta got added
create_users_data_in_excel("user_details.xlsx")
#to know what all data faker can add
print(dir(fake))
"""
'aba', 'add_provider', 'address', 'administrative_unit', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 
'ascii_free_email', 'ascii_safe_email', 'bank_country', 'basic_phone_number', 'bban', 'binary', 'boolean', 'bothify', 'bs',
 'building_number', 'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 
 'color_hsl', 'color_hsv', 'color_name', 'color_rgb', 'color_rgb_float', 'company', 'company_email', 'company_suffix', 
 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 
 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 
 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name', 'currency_symbol', 'current_country', 
 'current_country_code', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century',
 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 
 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 
 'date_time_this_year', 'day_of_month', 'day_of_week', 'del_arguments', 'dga', 'doi', 'domain_name', 'domain_word',
  'dsv', 'ean', 'ean13', 'ean8', 'ein', 'email', 'emoji', 'enum', 'factories', 'file_extension', 'file_name', 'file_path', 
  'firefox', 'first_name', 'first_name_female', 'first_name_male', 'first_name_nonbinary', 'fixed_width', 'format', 
  'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'generator_attrs', 'get_arguments', 'get_formatter',
   'get_providers', 'get_words_list', 'hex_color', 'hexify', 'hostname', 'http_method', 'http_status_code', 'iana_id', 'iban', 
   'image', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 
   'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'items', 'itin', 'job', 'job_female', 'job_male', 
   'json', 'json_bytes', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', 
   'last_name_nonbinary', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 
   'local_latlng', 'locale', 'locales', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 
   'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 
   'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 
   'name_male', 'name_nonbinary', 'nic_handle', 'nic_handles', 'null_boolean', 'numerify', 'opera', 'optional',
    'paragraph', 'paragraphs', 'parse', 'passport_dates', 'passport_dob', 'passport_full', 'passport_gender', 
    'passport_number', 'passport_owner', 'password', 'past_date', 'past_datetime', 'phone_number', 'port_number', 
    'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode', 'postcode_in_state', 'prefix', 
    'prefix_female', 'prefix_male', 'prefix_nonbinary', 'pricetag', 'profile', 'provider', 'providers', 'psv', 'pybool', 
    'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyobject', 'pyset', 'pystr', 'pystr_format', 'pystruct',
     'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 'random_digit_above_two', 'random_digit_not_null',
      'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 
      'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 
      'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'ripe_id', 'safari', 'safe_color_name', 'safe_domain_name',
       'safe_email', 'safe_hex_color', 'sbn9', 'secondary_address', 'seed', 'seed_instance', 'seed_locale', 'sentence', 
       'sentences', 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 
       'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 
       'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 
       'unique', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page', 'uri_path', 
       'url', 'user_agent', 'user_name', 'uuid4', 'vin', 'weights', 'windows_platform_token', 'word', 'words', 'xml', 'year',
        'zip', 'zipcode', 'zipcode_in_state', 'zipcode_plus4'
"""
