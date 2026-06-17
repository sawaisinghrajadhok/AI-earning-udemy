

def method_1(name, age, gender):
    print("name of the person is: ", name)
    print("age of the person is: ", age)
    print("gender of the person is: ", gender)



person = {
    'name': 'sawai',
    'age': 30,
    'gender':'Male'
}


method_1(**person)

