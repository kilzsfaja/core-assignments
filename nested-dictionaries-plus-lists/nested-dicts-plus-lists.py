# # 1 - Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"

# Change the value 20 in z to 30
z[0]["y"] = 30

# 2 - Iterate Through a List of Dictionaries

students = [
    {
    'first_name':  'Michael',
    'last_name' : 'Jordan'
    },
    {
    'first_name' : 'John',
    'last_name' : 'Rosales'
    },
    {
    'first_name' : 'Mark',
    'last_name' : 'Guillen'
    },
    {'first_name' : 'KB',
    'last_name' : 'Tonel'
    }
    ]

def iterateDictionary(lst):
    for student in lst:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students)


# 3 - Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name, lst):
    for student in students:
        print(student["last_name"]) # switch "last_name" to "first_name" for part 1

iterateDictionary2("last_name", students) # switch "last_name" to "first_name" for part 1

# 4 - Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = { #           0           1         2           3        4       5       6
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], # key 'locations'
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'] # key 'instructors'
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{key}: {len(some_dict[key])}")
        for value in some_dict[key]:
            print(value)

printInfo(dojo)