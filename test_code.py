import pytest
import requests
import random


# Test data
username = ["username", "123", " ", "{}}(", ["username"], {"username": "username"}]
post_id = ["post_id", "{}}(", ["post_id"], {"post_id": "post_id"}]


# Tests for the first method: GET /
def test_index_method():
    """Test for the first method with valid data"""
    url = "http://0.0.0.0:6000/"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "key": "value"\n}\n', "Test failed. We got: {}".format(response.text)

def test_index_method_as_post():
    """Test for the first method with invalid http method"""
    url = "http://0.0.0.0:6000/"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed"


# Tests for the second method: GET /user/<username>
def test_user_method():
    """Test for the second method with valid data"""
    url = "http://0.0.0.0:6000/user/Jake"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "User": "Jake"\n}\n', "Test failed. We got: {}".format(response.text)

def test_user_method_without_username():
    """Test for the second method without username"""
    url = "http://0.0.0.0:6000/user/"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed"

def test_user_method_with_random_string_as_username():
    """Test for the second method with random string as username"""
    test_name = random.choice(username)
    url = "http://0.0.0.0:6000/user/{}".format(test_name)
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"

def test_user_method_as_post():
    """Test for the second method with invalid http method"""
    url = "http://0.0.0.0:6000/user/Jake"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed"


# Tests for the third method: GET /post/<int:post_id>
def test_post_method():
    """Test for the third method with valid data"""
    url = "http://0.0.0.0:6000/post/1"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"
    assert response.text == '{\n  "post": 1\n}\n', "Test failed. We got: {}".format(response.text)

def test_post_method_with_too_long_post_id():
    """Test for the third method with too long post_id"""
    post_id = "10000001"*1000
    url = "http://0.0.0.0:6000/post/{}".format(post_id)
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"

def test_post_method_without_post_id():
    """Test for the third method without post_id"""
    url = "http://0.0.0.0:6000/post/"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed"

def test_post_method_with_invalid_post_id():
    """Test for the third method with invalid post_id"""
    test_post_id = random.choice(post_id)
    url = "http://0.0.0.0:6000/post/{}".format(test_post_id)
    response = requests.get(url)
    assert response.status_code == 404, "Test failed"

def test_post_method_as_post():
    """Test for the third method with invalid http method"""
    url = "http://0.0.0.0:6000/post/1"
    response = requests.post(url)
    assert response.status_code == 405, "Test failed"


# Tests for non existent endpoint
def test_for_non_existent_endpoint():
    """Test for non existent endpoint"""
    url = "http://0.0.0.0:6000/test"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed"
