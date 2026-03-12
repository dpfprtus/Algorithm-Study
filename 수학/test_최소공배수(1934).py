import importlib.util
import os

# Dynamically load the module since the filename contains parentheses
module_name = "최소공배수_1934"
file_path = os.path.join(os.path.dirname(__file__), "최소공배수(1934).py")

spec = importlib.util.spec_from_file_location(module_name, file_path)
math_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(math_module)

def test_gcd_a_greater_than_b():
    assert math_module.gcd(12, 8) == 4
    assert math_module.gcd(15, 5) == 5

def test_gcd_a_less_than_b():
    assert math_module.gcd(8, 12) == 4
    assert math_module.gcd(5, 15) == 5

def test_gcd_coprime():
    assert math_module.gcd(7, 11) == 1
    assert math_module.gcd(13, 17) == 1

def test_gcd_multiple():
    assert math_module.gcd(100, 10) == 10
    assert math_module.gcd(10, 100) == 10

def test_gcd_same_numbers():
    assert math_module.gcd(7, 7) == 7

def test_gcd_with_one():
    assert math_module.gcd(1, 10) == 1
    assert math_module.gcd(10, 1) == 1
