my_list = ['apple', 'banana', 'mango']
my_dict = {
    0: 'apple',
    1: 'banana',
    2: 'mango'
}
# ordered
# changable
# duplicates not allowed
my_details = {
    'name':"Ram",
    'age': 12,
    'dob': 1999,
    'dob' : 1945
}
my_details['name'] = 'shyam'

# print(my_details.keys())

'''
for i in my_details.keys():
    print(f'My {i} is: ', my_details[i])
'''

my_data = {
    'basic':{
        'name':"Ram",
        'age': 12,
        'dob': 1999,
        'dob' : 1945
    },
    'education':{
        'clg':"XYZ",
        'marks':12.4,
        'year': 2029
    },
    'job':{
        'company_name':"ABC",
        'salary':12000,
        'experience': 4
    }
}
print(my_data['education'])
print(my_data['education']['clg'])


print(dict.fromkeys(('a', 'b', 'c'), 0))
print(my_details.get('name'))
print(my_details.keys())
print(my_details.values())