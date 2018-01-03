from unittest.mock import Mock

class TestClass():
    pass

cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
print(cls.method(1,2,3))
cls.method.assert_called_once_with(1,2,3)
cls.other_method = Mock(return_value='something else')
cls.other_method.assert_not_called()