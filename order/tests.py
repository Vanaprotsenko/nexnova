from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        # Создайте тестовые данные, которые будут использоваться в тестах
        self.product = Product.objects.create(name='Тестовый продукт', price=10.0)

    def test_product_price(self):
        # Проверьте, что цена продукта равна ожидаемой
        self.assertEqual(self.product.price, 10.0)

    def test_product_name(self):
        # Проверьте, что имя продукта соответствует ожидаемому
        self.assertEqual(self.product.name, 'Тестовый продукт')