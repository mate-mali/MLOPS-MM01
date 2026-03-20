import os
import pytest
from settings import Settings
from main import run_app


def test_run_dev(monkeypatch):
    """Test that run_app works with dev environment."""
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    
    result = run_app("dev")
    
    assert result["ENVIRONMENT"] == "dev"
    assert result["APP_NAME"] == "main-dev"
    assert type(result["secrets"]) == dict

def test_run_prod(monkeypatch):
    """Test that run_app works with prod environment."""
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    
    result = run_app("prod")
    
    assert result["ENVIRONMENT"] == "prod"
    assert result["APP_NAME"] == "main-prod"
    assert type(result["secrets"]) == dict

def test_run_test(monkeypatch):
    """Test that run_app works with test environment."""
    monkeypatch.setenv("SECRETS_FILE", "secrets.yaml")
    
    result = run_app("test")
    
    assert result["ENVIRONMENT"] == "prod"
    assert result["APP_NAME"] == "main-prod (but test)"
    assert type(result["secrets"]) == dict


def test_settings_invalid_environment(monkeypatch):
    """Test that settings raises error with invalid environment."""
    monkeypatch.setenv("ENVIRONMENT", "invalid")
    monkeypatch.setenv("APP_NAME", "test-app")