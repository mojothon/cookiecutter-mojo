from std.testing import assert_equal, TestSuite
from {{cookiecutter.project_slug}}.version import __version__

def test_version() raises:
    assert_equal(__version__, "{{cookiecutter.version}}")

def main() raises:
    TestSuite.discover_tests[__functions_in_module()]().run()
