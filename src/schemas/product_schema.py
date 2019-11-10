from ..app import ma


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Initialize schemas
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)
