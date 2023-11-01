from django.test import SimpleTestCase

# Create your tests here.
class Testnear_100(SimpleTestCase):
    def test_near_100(self):
        response=self.client.get('/warmup-1/near-100/93')
        self.assertContains(response,True)
    def test_near_100(self):
        response=self.client.get('/warmup-1/near-100/90')
        self.assertContains(response,True)
    def test_near_100(self):
        response=self.client.get('/warmup-1/near-100/89')
        self.assertContains(response,False)

class Testwarmup_2(SimpleTestCase):
    def test_string_splosion(self):
        response=self.client.get('/warmup-2/string-splosion/Code')
        self.assertContains(response,'CCoCodCode')
    def test_string_splosion(self):
        response=self.client.get('/warmup-2/string-splosion/abc')
        self.assertContains(response,'aababc')
    def test_string_splosion(self):
        response=self.client.get('/warmup-2/string-splosion/ab')
        self.assertContains(response,'aab')

class TestString_2(SimpleTestCase):
    def test_string_2(self):
        response=self.client.get('/string-2/cat-dog/catdog')
        self.assertContains(response,True)
    def test_string_2(self):
        response=self.client.get('/string-2/cat-dog/catcat')
        self.assertContains(response,False)
    def test_string_2(self):
        response=self.client.get('/string-2/cat-dog/1cat1cadodog')
        self.assertContains(response,True)

class TestLogic_2(SimpleTestCase):
    def test_logic_2(self):
        response=self.client.get('/logic-2/lone-sum/1/2/3')
        self.assertContains(response,6)
    def test_logic_2(self):
        response=self.client.get('/logic-2/lone-sum/3/2/3')
        self.assertContains(response,2)
    def test_logic_2(self):
        response=self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response,0)