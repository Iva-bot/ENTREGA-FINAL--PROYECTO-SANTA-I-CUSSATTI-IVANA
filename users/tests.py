from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from AppSanta.models import Cliente
from users.utility import return_today,return_month,return_year
from datetime import datetime as dt


class EliminarProductoTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client = Client()
        self.client.login(username= 'testuser', password='12345')
        self.cliente= Cliente.objects.create (
            nombre="Teodoro",
            Apellido= "Lopez",
            email="hotmail.com"
            )
        self.url =reverse ("ClienteDelate", args=[self.cliente.id])

    def test_eliminar_cliente(self):
        response =self.client.get(self.url)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response ,"AppSanta/cliente_confirm_delete.html")
        self.client.post(self.url)
        self.assertQuerysetEqual(Cliente.objects.all(), [])                       
     

class TestUtilities(TestCase):
    def test_day(self):
        hoy =dt.now()
        self.assertEqual(hoy.day , return_today())

    def test_return_today(self):
        hoy= dt.now()
        self.assertEqual(return_today(), hoy.today)
   
    def test_return_month(self):
        month= dt.now()
        self.assertEqual(return_month(), month.month)

    def test_return_year(self):
        year= dt.now()
        self.assertEqual(return_year(), year.year)


