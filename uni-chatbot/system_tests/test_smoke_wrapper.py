import pytest

from system_tests import e2e_tests


@pytest.mark.smoke
def test_smoke_features():
    """
    Wrapper that calls the existing e2e test and lets pytest run it.
    """
    success, created_users, feedback_content = e2e_tests.test_features()
    # Optionally clean up or assert on side effects; here we assert the run succeeded.
    assert success, "Smoke E2E test failed"
