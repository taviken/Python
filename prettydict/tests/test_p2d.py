import pytest
from ..p2d import dict_to_html_manual, dict_to_html_list, generate_html_table

exp1 = """<ul>
  <li>**Name**: Alice</li>
  <li>**Age**: 30</li>
  <li>**City**: New York</li>
</ul>"""
exp2 = "<ul><li><strong>person:</strong> <ul><li><strong>name:</strong> Alice</li><li><strong>age:</strong> 30</li><li><strong>contact:</strong> <ul><li><strong>email:</strong> alice@example.com</li><li><strong>phone:</strong> 123-456-7890</li></ul></li><li><strong>is_active:</strong> True</li></ul></li><li><strong>location:</strong> New York</li></ul>"
exp3 = "<html><table border='1'>\n  <tr><th>Child ID</th><th>name</th><th>year</th></tr>\n  <tr><td>child1</td><td>Emil</td><td>2004</td></tr>\n  <tr><td>child2</td><td>Tobias</td><td>2007</td></tr>\n  <tr><td>child3</td><td>Linus</td><td>2011</td></tr>\n</table></html>"


def test_dict_to_html_manual():
    my_dict = {"Name": "Alice", "Age": 30, "City": "New York"}
    html_result = dict_to_html_manual(my_dict)
    print(html_result)
    assert html_result == exp1


def test_dict_to_html_list():
    nested_dict = {
        "person": {
            "name": "Alice",
            "age": 30,
            "contact": {"email": "alice@example.com", "phone": "123-456-7890"},
            "is_active": True,
        },
        "location": "New York",
    }
    html_output = dict_to_html_list(nested_dict)
    assert html_output == exp2


def test_generate_html_table():
    data = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus", "year": 2011},
    }
    html_output = generate_html_table(data)
    assert html_output == exp3
