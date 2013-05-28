"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class PrimoTest(TestCase):
    def test_numero_2_es_primo(self):
        """
	Prueba que el numero 2 es primo
        """
        self.assertEqual( primo(2),True)

    def test_numero_5_es_primo(self):
        """
	Prueba que el numero 5 es primo
        """
        self.assertEqual( primo(5),True)

    def test_numero_9_no_es_primo(self):
        """
	Prueba que el numero 9 no es primo
        """
        self.assertEqual( primo(9),False)

    def test_factores_primos_de_30_son_2_3_5(self):
	"""
	Prueba que los factores primos de 30 sean 2,3,5
	"""
	self.asserEqueal( factores_primos(30),[2,3,5] ) 
	
    def test_mayor_factor_primo_de_30_es_5(self):
	"""
	Prueba que el mayor factor primo de 30 sea 5
	"""
	self.asserEqueal(max(factores_primos(30),5) )

