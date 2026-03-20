import os
import pytest
from settings import Settings
from main import run_app


def test_run_dev(monkeypatch):
    #Test that run_app works with dev environment.
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    monkeypatch.setenv("ENVIRONMENT", "dev")  #apparently i need to manually set this for the test to work, even though it should be set by the .env file
    monkeypatch.setenv("APP_NAME", "main-dev")
    
    result = run_app("dev")
    
    assert result["ENVIRONMENT"] == "dev"
    assert result["APP_NAME"] == "main-dev"
    assert type(result["secrets"]) == dict

def test_run_prod(monkeypatch):
    #test prod
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    monkeypatch.setenv("ENVIRONMENT", "prod")
    monkeypatch.setenv("APP_NAME", "main-prod")
    
    result = run_app("prod")
    
    assert result["ENVIRONMENT"] == "prod"
    assert result["APP_NAME"] == "main-prod"
    assert type(result["secrets"]) == dict

def test_run_test(monkeypatch):
    #test run
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    monkeypatch.setenv("ENVIRONMENT", "prod")
    result = run_app("test")
    
    assert result["ENVIRONMENT"] == "prod"
    assert result["APP_NAME"] == "main-prod (but test)"
    assert type(result["secrets"]) == dict


def test_settings_invalid_environment(monkeypatch):
    """Test that settings raises error with invalid environment."""
    monkeypatch.setenv("ENVIRONMENT", "invalid")
    monkeypatch.setenv("APP_NAME", "test-app")