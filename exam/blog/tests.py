from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import Post

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='aiman', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Content here', author=self.user)

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_get_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Post')
