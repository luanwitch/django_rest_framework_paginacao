import factory
from product.models import Product
from faker import Faker

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: fake.word())
    description = factory.LazyAttribute(lambda x: fake.sentence())
    price = factory.LazyAttribute(lambda x: round(fake.random_number(digits=3), 2))
