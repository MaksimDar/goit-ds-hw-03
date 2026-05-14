from pymongo import MongoClient
from pymongo.server_api import ServerApi

mongo_connection = MongoClient('mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/', server_api=ServerApi('1'))
db = mongo_connection.cats_db
collection_name = db.cats

command = 'poetry run python3 main.py'

#Розробіть Python скрипт, який використовує бібліотеку PyMongo для реалізації основних CRUD (Create, Read, Update, Delete) операцій у MongoDB.

# 1. Create one cat

def create_one_cat(name: str, age: int, features: list) -> None:
    message = 'SUCCESS! A cat was added to the database'
    if type(name) == str and type(age) == int and type(features) == list:
        collection_name.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
    else:
        message = 'ERROR! Types of input are invalid. A cat was not added to the database'
    print(message)

# 2. Create many cats

def create_many_cats(*lists):
    success = 0
    error = 0
    success_message = "SUCCESS! Cat was added to the database"
    error_message = 'ERROR! Cat was not added to the database'
    for cat in lists:
        if len(cat) != 3:
            error+=1
            print(error_message)
            continue
        if isinstance(cat[0], str) and isinstance(cat[1], int) and isinstance(cat[2], list):
            collection_name.insert_one({
                "name": cat[0],
                "age": cat[1],
                "features": cat[2]
            })
            print(success_message)
            success+=1
        else:
            syntax_message = 'ERROR! Types of input are invalid. Cats were notadded to the database'
            print(syntax_message)
            error+=1
        
    print(f'{success} cats were added, and {error} cats were not added')

# Читання (Read). 
# 3. Функція для виведення всіх записів із колекції.

def show_all_cats():
    all_cats = collection_name.find({})
    for cat in all_cats:
        print(cat)

# 4. Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.

def show_cat_info(name):
    found_cat = collection_name.find_one({'name': name})
    print(found_cat)

# Оновлення (Update)

# 5. Функція, яка дозволяє користувачеві оновити вік кота за ім'ям.

def update_cat_age(name,age):
    message = "SUCCESS! Cat's age was changed"
    if isinstance(name, str) and isinstance(age,int):
        updated_age = collection_name.update_one({"name": name}, {'$set': {'age': age} })
        if updated_age.matched_count > 0:
            print(message)
            show_cat_info(name)
        else:
            print(f"{name} cat was not found")

    else:
        message = "ERROR! Cat's age was not changed"
        print(message)

# 6. Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям.

def add_feature(name, feature):
    message = "SUCCESS! Cat's features was changed"
    if isinstance(name, str) and isinstance(feature, str):
        updated_feature = collection_name.update_one({"name": name}, {'$push': {'features': feature}})
        if updated_feature.matched_count > 0:
            print(message)
            show_cat_info(name)
        else:
            print(f"{name} cat was not found")
    else:
        message = "ERROR! Cat's feature was not added"
        print(message)

# Видалення (Delete)

# 7. Функція для видалення запису з колекції за ім'ям тварини.

def delete_cat(name):
    message = "SUCCESS! Cat was deleted"
    if isinstance(name, str):
        deleted_cat = collection_name.delete_one({"name": name})
        if deleted_cat.deleted_count > 0:
            print(message)
        else:
            print(f"{name} cat was not found")
    else:
        message = "ERROR! Cat was not deleted"
        print(message)

# 8. Функція видалення всіх записів із колекції.

def delete_all_cats():
    message = "SUCCESS! All cats are deleted"
    deleted_cats = collection_name.delete_many({})
    if deleted_cats.deleted_count > 0:
        print(message)
    else:
        message = 'Collection is already empty'
        print(message)


if __name__ == '__main__':

    # 1. Function create_one_cat() is used

    # create_one_cat('Barkis', 4, ['Plays with the ball', 'Eats fish'])
    # create_one_cat('Boris', 5, ['Plays with the cat', 'Swims'])
    # create_one_cat('Stepan', 4, ['Plays with the ball', 'Eats fish'])
    # create_one_cat('Stepan', '4', ['Plays with the ball', 'Eats fish'])


    # 2. Function create_many_cats() is used

    # create_many_cats(
    # ["Barsik", 3, ["red", "kind"]],
    # ["Boris", '8', ["red", "kind"]],
    # ["Oscar", 12],
    # ["Luna", 2, ["white", "smart"]],
    # ["Tom", 5, ["lazy", "big"]],
    # ["Murka", 1, ["playful", "small"]],
    # )


    # 3. Function show_all_cats() is used

    # show_all_cats()


    # 4. Function show_cat_info() is used

    # show_cat_info("Tom")


    # 5. Function update_cat_age() is used

    # update_cat_age('Tom',23)


    # 6. Function add_feature() is used

    # add_feature('Tom', 'Drinks water')


    # 7. Function delete_cat() is used

    # delete_cat('Tom')
    # delete_cat('ToM')

    # 8. Function delete_all_cats() is used
    
    # delete_all_cats()
    ...
    