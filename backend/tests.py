from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"email": "test@localhost.app", "username": "testcase",
                "password": "testpass", "password1": "testpass"}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.user_authentication()

    def user_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_user_login(self):
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post('/auth/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], self.token.key)

    def test_user_login_no_user(self):
        data = {"username": "badlogin", "password": "badpass"}
        response = self.client.post('/auth/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FollowedCryptoViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.user_authentication()

    def user_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_followed_crypto_by_user(self):
        followed = FollowedCrypto.objects.create(
            name='Bitcoin',
            coin_id='btc-bitcoin',
            who_follow=self.user
        )
        response = self.client.post('/api/followed/get_followed_by_user/', {"token": self.token.key})
        self.assertEqual("Bitcoin", response.data['result'][0]['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_followed_no_token(self):
        followed = FollowedCrypto.objects.create(
            name='Bitcoin',
            coin_id='btc-bitcoin',
            who_follow=self.user
        )
        response = self.client.post('/api/followed/get_followed_by_user/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_crypto_to_followed(self):
        response = self.client.post('http://127.0.0.1:8000/api/followed/', {
            'name':'testcoin',
            'coin_id': 'testcoin_id',
            'token': self.token.key
        })

        added = FollowedCrypto.objects.first()
        self.assertEqual('testcoin', added.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_crypto_to_followed_no_token(self):
        response = self.client.post('http://127.0.0.1:8000/api/followed/', {
            'name': 'testcoin',
            'coin_id': 'testcoin_id',
            'token': ''
        })
        added = FollowedCrypto.objects.first()
        self.assertEqual(None, added)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_remove_crypto_from_followed(self):
        followed = FollowedCrypto.objects.create(
            name='Bitcoin',
            coin_id='btc-bitcoin',
            who_follow=self.user
        )
        response = self.client.post('/api/followed/delete_followed_by_user/', {
            'token': self.token.key,
            'coin_id': 'btc-bitcoin'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FollowedCrypto.objects.first(), None)

    def test_remove_crypto_from_followed_no_token(self):
        response = self.client.post('/api/followed/delete_followed_by_user/', {
            'token': '',
            'coin_id': 'btc-bitcoin'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)