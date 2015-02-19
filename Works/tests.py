# -*- encoding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Work
from django.utils.text import slugify

class WorkTets(TestCase):

	def setUp(self):
		self.test_user = User.objects.create_user(username = 'username', password = 'password')	

	def test_model_work(self):
		test_work = Work.objects.create(user = self.test_user,title = 'Los Patitos', description = 'Los Patitos Son Bonitos', category = "dibujo-pintura", date = '2015-02-16', cover = 'Cover de la Obra', archive = 'Imagen de la Obra', slug = 'los-patitos')

	# def test_model_work_2(self):
	# 	test_work = Work.objects.create(user = self.test_user,title = '', description = '', category = '', date = '', cover = '', archive = '', slug = '')

	# def test_model_work_3(self):
	# 	test_work = Work.objects.create(user = self.test_user,title = None, description = None, category = None, date = None, cover = None, archive = None, slug = None)
	# def test_model_work_4(self):
	# 	test_work = Work.objects.create(user = self.test_user,title = 1321, description = '{}', category = '', date = None, cover = '73612', archive = 14453, slug = '<html></html>')


	# Pruebas Para las vistas
	def test_views(self):

		# Subir Una Obra
		estatus = self.client.get(reverse_lazy('create_work'))
		self.assertEqual(estatus.status_code, 200)

		# Explorar Obras
		estatus = self.client.get(reverse_lazy('index'))
		self.assertEqual(estatus.status_code, 200)

		# Lista De Obras
		estatus = self.client.get(reverse_lazy('work_list'))
		self.assertEqual(estatus.status_code,200)

