from uuid import uuid4
import pytest

# --------
# Fixtures
# --------


@pytest.fixture
def f():
    def work(prefix: str = ''):
        return f'{prefix}{uuid4().hex}'

    return work


@pytest.fixture
def micro():
    import micro

    return micro


@pytest.fixture
def service(micro):
    return micro.Service(name='service')


# -----
# Tests
# -----


def test_basic_service_registation(f, service):
    service.register(f=f)

    assert 'work' in service.services


def test_named_service_registation(f, service):
    service.register(f=f, name='test')

    assert 'test' in service.services


def test_custom_uri_service_registation(f, service):
    service.register(f=f, name='test', uri='/not-test')

    assert 'test' in service.services
    assert service.services['test']['uri'] == '/not-test'


def test_argument_detection(f, service):
    service.register(f=f)

    assert 'work' in service.services
    assert 'prefix' in service.services['work']['args']
