def pytest_make_parametrize_id(config, val, argname):  # pylint: disable=unused-argument
    """
    Custom function to generate parameter IDs for pytest.
    This function is called by pytest when generating the
    IDs for the parameters in the test functions.
    """
    return f"{{{argname}: {val}}}"
