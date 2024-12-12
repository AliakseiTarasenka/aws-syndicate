from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        # Validate that necessary keys are present
        if 'requestContext' in event and 'http' in event['requestContext']:
            http_info = event['requestContext']['http']
            if 'method' not in http_info or 'path' not in http_info:
                return {"error": "Missing httpMethod or path in the event."}
        else:
            return {"error": "Missing requestContext or http in the event."}
        return {}

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        http_method = (event.get('requestContext', {}).get('http', {}).get('method'))
        path = (event.get('requestContext', {}).get('http', {}).get('path'))
        _LOG.info(f"Received HTTP method: {http_method}, path: {path}")

        if path == '/hello' and http_method == 'GET':
            return {"statusCode": 200, "message": "Hello from Lambda"}
        else:
            return {"statusCode": 400, "message": f"Bad request syntax or unsupported method. Request path: {path}. "
                                                  f"HTTP method: {http_method}"}


HANDLER = HelloWorld()


def lambda_handler(event, context):
    """
    Entry point for the Lambda function.

    Args:
        event: The event dictionary that Lambda receives from the trigger.
        context: The runtime context of the Lambda function.

    Returns:
        A dictionary response from handle_request method.
    """
    print(event)
    validation_errors = HANDLER.validate_request(event)
    print(validation_errors)
    if validation_errors:
        return {
            "statusCode": 400,
            "body": validation_errors.get("error", "Invalid request")
        }

    return HANDLER.handle_request(event, context)
