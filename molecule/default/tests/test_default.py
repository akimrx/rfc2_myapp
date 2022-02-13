import pytest
import requests


@pytest.fixture
def role_vars(host):
    """Loading standard role variables."""
    defaults_files = "file=./defaults/main.yml name=role_defaults"
    vars_files = "file=./vars/main.yml name=role_vars"

    ansible_vars = host.ansible("include_vars", defaults_files)["ansible_facts"]["role_defaults"]
    ansible_vars.update(
        host.ansible("include_vars", vars_files)["ansible_facts"]["role_vars"]
    )
    return ansible_vars


def test_nginx_dependency(host):
    """Check requirement nginx role."""
    nginx = host.package("nginx")
    nginx_service = host.service("nginx")
    nginx_port = host.socket("tcp://0.0.0.0:80")
    nginx_port.is_listening, "NGINX port is not listening"
    assert nginx.is_installed, "NGINX is not installed"
    assert nginx_service.is_running, "NGINX service is not running"
    assert nginx_service.is_enabled, "NGINX service is not enabled"


def test_application_service(host):
    """Checking the installation of the MyApp service."""
    myapp_service = host.service("myapp")
    assert myapp_service.is_running, "MyApp service is not running"
    assert myapp_service.is_enabled, "MyApp service is not enabled"


def test_application_is_work(host, role_vars):
    """Check that the application really works."""
    expected_port = role_vars.get("myapp_port")
    app_http = host.socket(f"tcp://0.0.0.0:{expected_port}")
    assert app_http.is_listening, "App HTTP port is not listening"

    http_response = host.check_output("curl http://localhost:8080")
    assert http_response == "Hello, World!", "Invalid HTTP response"
