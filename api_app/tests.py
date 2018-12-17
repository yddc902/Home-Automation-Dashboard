from django.test import TestCase
import requests

# Create your tests here.
def test_post():
    print('Testing...')
    send_data = {'id': '77',}
    r = requests.post('http://127.0.0.1:8000/upload/', data=send_data)
    print('Test completed.')
    #print(r.text[:])

test_post()
