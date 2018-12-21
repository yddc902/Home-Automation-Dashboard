from django.test import TestCase
import requests

# Create your tests here.
def test_post():
    print('Testing...')
    send_data = {'id': '77',} #Format as JSON object
    r = requests.post('http://127.0.0.1:8000/upload/', data=send_data)
    print('Test completed.')
    #print(r.text[:])

    #This data can be retrieved from the POST request using:
    #   request.POST['id']
    #   which will yield a value of '77'
    #
    #   this is not necessarily compatible with the current method of using json.loads

def test_json():
    import json

    print("Testing...")
    send_data = {'id': '123'}

    print(json.dumps(send_data)) #Return string from JSON-like object
    received_data = json.dumps(send_data)

    print(json.loads(received_data)['id']) #Use json.loads() to turn string into JSON

def test_detection():
    send_data = {'Level': 50}
    r = requests.post('http://127.0.0.1:8000/upload/waterdetected/', data=send_data)
    print('Test Completed')

test_detection()
#test_json()
#test_post()
