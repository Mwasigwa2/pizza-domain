from marshmallow import Schema, fields

class RestaurantSchema(Schema):
    class Meta:
        fields = ("id", "name", "address")

class PizzaSchema(Schema):
    class Meta:
        fields = ("id", "name", "ingredients")

class RestaurantPizzaSchema(Schema):
    class Meta:
        fields = ("id", "price", "restaurant_id", "pizza_id")
