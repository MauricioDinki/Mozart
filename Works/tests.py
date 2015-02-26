# -*- encoding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Work
from django.utils.text import slugify
from Profiles.models import Adress,Date_of_Birth,Contact
from django.utils.text import slugify

class WorkTets(TestCase):

	def setUp(self):
		self.test_user = User.objects.create_user(username = 'paquito', password = 'hola')

	def test_adress(self):
		test_adress = Adress.objects.create(
			user = self.test_user, 
			adress = "hola", 
			city = "Hola mama", 
			zip_code = 'hola mama', 
			neighborhood = 'jajaja',
		)

	def test_date_of_birth(self):
		self.test_date_of_birth = Date_of_Birth.objects.create(
			user = self.test_user, 
			day = 21, 
			month = 'agosto', 
			year = 1971,
		)

	def test_contact(self):
		self.test_contact = Contact.objects.create(
			user = self.test_user, 
			personal_homepage = 'http://mauricio.me',
			phone_number = 58855907,
		)

	def test_works(self):
		test_work = Work.objects.create(
			user = self.test_user,
			title = 'title',
			description = 'Obra mas Chida',
			category = 'dibujo-pintura',
			archive = 'archivo.jpg',
			cover = 'cover.jpg',
		)

	def test_views(self):
		estatus = self.client.get(reverse_lazy('index'))
		self.assertEqual(estatus.status_code, 200)

		estatus = self.client.get(reverse_lazy('work_list'))
		self.assertEqual(estatus.status_code,200)

