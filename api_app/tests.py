from django.test import TestCase
import requests

# Create your tests here.
def test_post():
    print('Testing...')
    send_data = {'id': '77',}
    r = requests.post('http://127.0.0.1:8000/upload/', data=send_data)
    print('Test completed.')
    #print(r.text[:])

    #This data can be retrieved from the POST request using:
    #   request.POST['id']
    #   which will yield a value of '77'
    #
    #   this is not necessarily compatible with the current method of using json.loads

test_post()
