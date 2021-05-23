# from django.test import TestCase
# import json
# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from .views.serializerView import CustomerSerializer
# from customers.models import Customer
#
# # class RegistrationTestCase(APITestCase):
# #
# #     def test_registration(self):
# #         data = {
# #             "username": "Test1","email":"test1@gmail.com","password1":"Test1@Strong","password2":"Test1@Strong"
# #         }
# #         response = self.client.post("/api/rst-auth/registration/",data)
# #         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#
# class CustomerViewSetTestCase(APITestCase):
#     list_url = reverse("customer-list")
#
#     def setUp(self):
#         self.user = User.objects.create_user(username="Zama",email="Zama@gmail.com",password="Zama@#$21")
#
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
#
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
#
#     def test_customer_list_authenticated(self):
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
#
#     def test_customer_list_unauthenticated(self):
#         self.client.force_authenticate(user=None)
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
#
#
