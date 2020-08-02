from django.urls import reverse, resolve

class TestUrls:

    def test_home_url(self):
        path = reverse('budget:index')
        
        assert resolve(path).view_name == 'budget:index'