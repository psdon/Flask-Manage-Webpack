# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import logging

import pytest

from example.demo.app import create_app


@pytest.fixture
def app():
    """Create application for the tests."""
    config = {
        "DEBUG": True,
        "Testing": True,
        'SERVER_NAME': 'localhost:5000',
        "MANAGE_WEBPACK_MANIFEST_PATH": "./sdftatdic/manifest.json"
    }
    _app = create_app()
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()
