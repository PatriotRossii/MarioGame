from src.test.test import TestResult, Test


class AbstractStorage:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(getattr(cls, "__class__"), cls).__new__(cls)
            cls.instance._init_default()
        return cls.instance

    @classmethod
    def _init_default(cls):
        pass

    @classmethod
    def set_value(cls, key, value):
        setattr(cls.instance, key, value)

    @classmethod
    def value(cls, key):
        return getattr(cls.instance, key)


if __name__ == "__main__":
    def test_persistance():
        AbstractStorage().set_value("key", 80)
        return TestResult(AbstractStorage().value("key") == 80)

    test = Test()
    test.add_test(test_persistance)
    test.run()
