from django.test import TestCase
from .models import Service


# Create your tests here.

# Проверка модели Service
class ServiceModelTestCase(TestCase):
    @staticmethod
    def print_info(message):
        count = Service.objects.count()
        print(f'{message}: #all_movies={count}')

    # Подготовка БД
    def setUp(self):
        print('-' * 20)
        self.print_info("Start setUp")
        self.service = Service.objects.create(description='Взлом', price=1000)
        Service.objects.create(description='Открытие', price=2000)
        Service.objects.create(description='пролом', price=3000)
        self.print_info("Finish setUp")

    # Проверка создания объекта Service
    def test_service_create(self):
        self.print_info('Start test_service_create')
        self.assertEqual(self.service.description, 'Взлом')
        self.assertEqual(self.service.price, 1000)
        self.print_info('Finish test_service_create')

    # Проверка получения всех записей Service
    def test_service_get_all_records(self):
        self.print_info('Start test_service_get_all_records')
        service = Service.objects.all()
        self.assertEqual(len(service), 3)
        self.print_info('Finish test_service_get_all_records')

    # Проверка получения одной записи Service
    def test_service_get_one_record(self):
        self.print_info('Start test_service_get_one_record')
        open = Service.objects.get(description='Открытие')
        self.assertEqual(open.price, 2000)
        self.print_info('Finish test_service_get_one_record')

    # Проверка метода __str__ в Service
    def test_service_str(self):
        self.print_info('Start test_service_str')
        expected = 'Взлом 1000'
        self.assertEqual(str(self.service), expected)
        self.print_info('Finish test_service_str')


# Проверка представлений
class TestMelanzh(TestCase):
    # Проверка главной страницы
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # Проверка каталога
    def test_catalog(self):
        response = self.client.get('/catalog')
        self.assertEqual(response.status_code, 200)

    # Проверка страницы сервисов
    def test_services(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Адрес: Санкт-Петербург, Беговая ул., д.5/2', response.content.decode())
        self.assertIn('8-911-288-99-11', response.content.decode())
