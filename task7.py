# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):

    def test_find_by_category(self):
        # Create and save multiple products with a known category
        known_category = fake.word()
        products = []
        for _ in range(5):
            product = Product(name=fake.company(),
                              description=fake.text(max_nb_chars=200),
                              price=99.99,
                              sku=fake.uuid4(),
                              category=known_category)
            product.save()  # Assuming the 'save' method persists the product
            products.append(product)

        # Create and save products with different categories
        for _ in range(5):
            product = Product(name=fake.company(),
                              description=fake.text(max_nb_chars=200),
                              price=99.99,
                              sku=fake.uuid4(),
                              category=fake.word())
            product.save()

        # Simulate the "find by category" operation
        found_products = Product.find_by_category(known_category)  # Assuming 'find_by_category' method fetches products by category

        # Check that the correct number of products are found
        self.assertEqual(len(found_products), len(products))

        # Check that each found product has the correct category
        for product in found_products:
            self.assertEqual(product.category, known_category)

if __name__ == '__main__':
    unittest.main()
