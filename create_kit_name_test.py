import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body ["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"] #tengo duda de esta variable si es authToken o Auth_token

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

#pruebas
def test1_create_new_kit_1_character_name_success_response():
    current_kit_body = get_kit_body("a")
    positive_assert(current_kit_body)

def test2_create_new_kit_511_character_name_success_response():
    current_kit_body = get_kit_body (data.test1_kit_name)
    positive_assert(current_kit_body)

2
def test3_create_new_kit_0_character_name_error_response():
    current_kit_body = get_kit_body("")
    negative_assert_code_400(current_kit_body)

def test4_create_new_512_character_name_error_response():
    current_kit_body = get_kit_body(data.test2_kit_name)
    negative_assert_code_400(current_kit_body)

def test5_create_user_has_number_in_first_name_success_response():
    current_kit_body = get_kit_body("%@")
    positive_assert(current_kit_body)

def test6_create_user_with_space_in_name_success_response():
    current_kit_body = get_kit_body("A aaa")
    positive_assert(current_kit_body)

def test7_create_user_number_in_name_success_response():
    current_kit_body = get_kit_body("123")
    positive_assert(current_kit_body)

def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_code_400(current_kit_body)

def test9_create_kit_number_type_name_parameter():
    current_kit_body = get_kit_body(123)
    positive_assert(current_kit_body)


