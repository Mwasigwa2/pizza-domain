from app import app  
from models import Restaurant, Pizza, RestaurantPizza, db
from faker import Faker

fake = Faker()

def seed_restaurants(num_entries=20):
    for _ in range(num_entries):
        restaurant = Restaurant(
            name=fake.unique.company(),
            address=fake.address()
        )
        db.session.add(restaurant)

def seed_pizzas():
    pizza_names = ["Margherita", "Pepperoni", "Hawaiian", "BBQ Chicken", "Meat Lover", "Veggie"]
    for name in pizza_names:
        pizza = Pizza(
            name=name,
            ingredients=fake.sentence()
        )
        db.session.add(pizza)

def seed_restaurant_pizzas(num_entries=50):
    for _ in range(num_entries):
        restaurant_pizza = RestaurantPizza(
            price=fake.random_int(min=5, max=30),
            pizza_id=fake.random_int(min=1, max=6),  
            restaurant_id=fake.random_int(min=1, max=20)  
        )
        db.session.add(restaurant_pizza)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        seed_restaurants()
        seed_pizzas()
        seed_restaurant_pizzas()

        db.session.commit()

    print("Database seeded!")