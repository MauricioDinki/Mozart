# -*- encoding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy

class WorkTets(TestCase):

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

