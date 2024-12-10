from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {
            'httpMethod': 'GET',
            'path': '/hello'
        }
        expected_response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)

    def test_unsupported_endpoint(self):
        # Simulate a GET request to an unsupported endpoint
        event = {
            'httpMethod': 'GET',
            'path': '/student_id'
        }
        expected_response = {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: /student_id. HTTP method: GET"
        }

        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)

    def test_unsupported_method(self):
        # Simulate a POST request to the /hello endpoint
        event = {
            'httpMethod': 'POST',
            'path': '/hello'
        }
        expected_response = {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: /hello. HTTP method: POST"
        }

        actual_response = self.HANDLER.lambda_handler(event, {})
        self.assertEqual(actual_response, expected_response)
