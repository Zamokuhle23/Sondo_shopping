# from django.contrib.auth.models import User
# import unittest
#
# from customers.models import Customer
#
#
# class TestCustomer(unittest.TestCase):
#
#     def setUp(self):
#         self.user1 = User('Zama','zama@gmail.com','Zama$2020')
#         self.customer1 = Customer(customer=self.user1,phone='12345678')
#
#     def test_name(self):
#         self.assertEqual(self.customer1.customer.username,self.user1.username)
#         self.assertEqual(self.customer1.customer.username,'Zama')
#         self.assertEqual(self.customer1.phone,'12345678')
#
#     def test_email(self):
#         self.assertNotEqual(self.customer1.customer.email.find('@'), -1)
#         self.assertNotEqual(self.customer1.customer.email.find('.'), -1)
#
#
# if __name__ == '__main__':
#     unittest.main()
