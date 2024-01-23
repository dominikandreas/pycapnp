import os
import capnp
import base64
import pytest

this_dir = os.path.dirname(__file__)


@pytest.fixture
def test_schema():
    return capnp.load(os.path.join(this_dir, "foo.capnp"))


class CustomString(str):
    pass


class CustomInt(int):
    pass


def test_custom_types_in_from_dict(test_schema):
    msg = test_schema.Foo(id=CustomInt(1), name=CustomString("foo"))
    dct = msg.to_dict()
    assert dct["id"] == 1 and dct["name"] == "foo"
    msg = test_schema.Foo.new_message()
    msg.from_dict(dct)
    assert msg.id == 1 and msg.name == "foo"


def test_bool():
    schema = capnp.load(os.path.join(this_dir, "all_types.capnp"))
    msg = schema.TestAllTypes(boolField=False)
    dct = msg.to_dict()
    assert dct["boolField"] == False
    msg = schema.TestAllTypes.new_message()
    msg.from_dict(dct)
    assert msg.boolField == False


test_bool()
