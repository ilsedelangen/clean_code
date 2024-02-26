from datetime import datetime

from ...examples.testing_mess import ConfigContainer


def test_is_valid_if_all_set():
    assert _create_valid_instance().is_valid()


def test_is_valid_if_all_set_and_approved():
    config = _create_valid_instance()
    config.approved = True
    assert config.is_valid()


def test_is_not_valid_with_none_name():
    config = _create_valid_instance()
    config.name = None
    assert not config.is_valid()


def test_is_not_valid_with_empty_name():
    config = _create_valid_instance()
    config.name = '  '
    assert not config.is_valid()


def test_is_not_valid_with_none_target():
    config = _create_valid_instance()
    config.target = None
    assert not config.is_valid()


def test_is_not_valid_with_empty_target():
    config = _create_valid_instance()
    config.target = '  '
    assert not config.is_valid()


def test_is_not_valid_with_none_comment():
    config = _create_valid_instance()
    config.comment = None
    assert not config.is_valid()


def test_is_not_valid_with_empty_comment():
    config = _create_valid_instance()
    config.comment = '  '
    assert not config.is_valid()


def test_is_not_valid_with_none_version():
    config = _create_valid_instance()
    config.version = None
    assert not config.is_valid()


def test_is_not_valid_with_wrong_version_format():
    config = _create_valid_instance()
    config.version = 'a.b.c'
    assert not config.is_valid()


def test_is_not_valid_without_creation_date():
    config = _create_valid_instance()
    config.creation_date = None
    assert not config.is_valid()


def test_is_not_valid_without_body():
    config = _create_valid_instance()
    config.body = None
    assert not config.is_valid()


def test_is_not_valid_without_anything():
    assert not ConfigContainer().is_valid()


def _create_valid_instance() -> ConfigContainer:
    config = ConfigContainer()
    config.name = 'Test Config'
    config.target = '192.168.0.1'
    config.version = '1.2.42.1337'
    config.creation_date = datetime.now()
    config.comment = 'Config for testing'
    config.body = [1, 2, 3]
    return config
