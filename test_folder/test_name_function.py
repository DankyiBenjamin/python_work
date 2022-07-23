import unittest

from numpy import full
from name_function import full_name
class NameTestCase(unittest.TestCase):
	""" Test for 'name_function.py' """
	def test_first_last_name(self,):
		""" Do names like Ben Dankyi work?"""
		formatted_name = full_name('ben','dankyi')
		self.assertEqual(formatted_name,"Ben Dankyi")

	def test_first_middle_last_name(self):
		""" Do names like Ben Kwasi Dankyi work?"""
		formatted_name = full_name('ben','dankyi','kwasi')
		self.assertEqual(formatted_name,'Ben Kwasi Dankyi')
    	
    		
    		

unittest.main()