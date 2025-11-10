#4th Nov Class
# get data from dictionary
#this is a dictionary having various key value pair
"""school = {'teacher': having 2 departments which is in list and inside list again dict key value pair
            'student': having 2 class which is in list and inside list again dict key value pair
            'admin'
            """
#import the pprint
from pprint import pprint

school = {
    'teacher': {
        'English': [
            {'name': 'Rohit', 'email': 'rohit@gmail.com', 'phone': 6546456},
            {'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 56432343}
        ],
        'Maths': [],
    },
    'student': {
        '10th': [
            {'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 8866868686},
            {'name': 'akshay', 'email': 'akshay@gmail.com', 'phone': 876766766},
        ],
        '11th': [],
    },
    'admin': {
        'account': [],
        'admission': []
    }

}

#now to print the dictionary
print(school)
#{'teacher': {'English': [{'name': 'Rohit', 'email': 'rohit@gmail.com', 'phone': 6546456}, {'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 56432343}], 'Maths': []}, 'student': {'10th': [{'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 8866868686}, {'name': 'akshay', 'email': 'akshay@gmail.com', 'phone': 876766766}], '11th': []}, 'admin': {'account': [], 'admission': []}}

#if we want the structure of dictionary in same format as defined above
#we need to import a library called pprint ->from pprint import pprint
#else if pprint not used,it wil give output in single line which is difficult to rad and understand
#after importig now do pprint
pprint(school)

#here the ouput dint follow the same order as input, as indexing doesnt apply for dict
#it could be sorted in alphabetical order or last in first out[LIFO]
"""
{'admin': {'account': [], 'admission': []},
 'student': {'10th': [{'email': 'mohit@gmail.com',
                       'name': 'mohit',
                       'phone': 8866868686},
                      {'email': 'akshay@gmail.com',
                       'name': 'akshay',
                       'phone': 876766766}],
             '11th': []},
 'teacher': {'English': [{'email': 'rohit@gmail.com',
                          'name': 'Rohit',
                          'phone': 6546456},
                         {'email': 'rahul@gmail.com',
                          'name': 'Rahul',
                          'phone': 56432343}],
             'Maths': []}}
"""

#now if we want a sepecific department say - teacher
pprint(school['teacher'])
"""
{'English': [{'email': 'rohit@gmail.com', 'name': 'Rohit', 'phone': 6546456},
             {'email': 'rahul@gmail.com', 'name': 'Rahul', 'phone': 56432343}],
 'Maths': []}
"""

#now if we want to get English department alone
pprint(school['teacher']['English'])
"""
[{'email': 'rohit@gmail.com', 'name': 'Rohit', 'phone': 6546456},
 {'email': 'rahul@gmail.com', 'name': 'Rahul', 'phone': 56432343}]
"""

#now if we see aboev result, further details are first in list and then inside list dictionary
#to retrive the data, first we need to provide the index

pprint(school['teacher']['English'][1])
#{'email': 'rahul@gmail.com', 'name': 'Rahul', 'phone': 56432343}

#now if we want the specific detail from the above result say phone
pprint(school['teacher']['English'][1]['phone'])
#56432343

#get data of 10th class student, Akshay
pprint(school['student']['10th'][1]['name']) #'akshay'