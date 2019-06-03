from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral

# run tests with "python manage.py test"


mineral_data = {
    "name": "Abelsonite",
    
}

mineral_data2 = {
    "name": "Abhurite",
    
}

# Create your tests here.
class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(name="Abelsonite")
        self.assertEqual(mineral.name, "Abelsonite")
        
        
class MineralViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(**mineral_data)
        self.mineral2 = Mineral.objects.create(**mineral_data2) 
        
    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list',
                                       kwargs={'letter': 'A'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral2.name)
        
        
    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral.image_caption)
        self.assertContains(resp, "Category")
        self.assertContains(resp, self.mineral.category)
        
        
    def test_group_list_view(self):
        resp = self.client.get(reverse('minerals:group_list',
                                       kwargs={'group_name': 'Organic Minerals'}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['minerals']), 7)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name + '</a>')
        
        
    def test_search_view(self):
        resp = self.client.get(reverse('minerals:search'),
                               {'q': 'abelsonite'})
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

        
        
if __name__ == '__main__':
    unittest.main()
        