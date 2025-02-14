import configuration
import data
import requests


def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICES + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers ["Authorization"] = "Bearer" + auth_token
    return requests.post(configuration.URL_SERVICES + configuration.PRODUCTS_KITS_PATH,
                         json=kit_body,
                         headers=current_headers)


