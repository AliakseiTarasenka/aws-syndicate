from tests.test_hello_world import HelloWorldLambdaTestCase
import json


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {
            'requestContext': {
                'http': {
                    'method': 'GET',
                    'path': '/hello'
                }
            }
        }
        expected_response = {
            "statusCode": 200,
            "body": json.dumps({"statusCode": 200, "message": "Hello from Lambda"})
        }
        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)

    def test_unsupported_endpoint(self):
        # Simulate a GET request to an unsupported endpoint
        event = {
            'requestContext': {
                'http': {
                    'method': 'GET',
                    'path': '/student_id'
                }
            }
        }
        expected_response = {
            "statusCode": 400,
            "body": json.dumps(
                {"statusCode": 400, "message": f"Bad request syntax or unsupported method. Request path: /student_id. "
                                               f"HTTP method: GET"})
        }

        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)

    def test_unsupported_method(self):
        # Simulate a POST request to the /hello endpoint
        event = {
            'requestContext': {
                'http': {
                    'method': 'POST',
                    'path': '/hello'
                }
            }
        }
        expected_response = {
            "statusCode": 400,
            "body": json.dumps(
                {"statusCode": 400, "message": f"Bad request syntax or unsupported method. Request path: /hello. "
                                               f"HTTP method: POST"})
        }

        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)
