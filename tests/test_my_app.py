from unittest.mock import patch
from didgen import __version__
from didgen.generator import generator


def test_version_displays_library_version():
    assert __version__ == "0.1.0", "Version number should match library version."


@patch('didgen.generator.didkit')
@patch('didgen.generator.print')
def test_generator_success(mock_print, mock_didkit):
    # Set up mock objects
    mock_didkit.key_to_did.return_value = "did:example:123456789"
    # Call the function under test
    generator(key_type="Ed25519", options=None)
    # Assert that the logging output contains the expected value
    mock_print.assert_called_with("Output: did:example:123456789")

@patch('didgen.generator.didkit')
@patch('didgen.generator.print')
def test_generator_exception(mock_print, mock_didkit):
    # Set up mock objects
    mock_didkit.key_to_did.side_effect = Exception("Failed to generate DID")
    # Call the function under test
    generator(key_type="Ed25519", options=None)
    # Assert that the exception message is printed to the console
    mock_didkit.key_to_did.assert_called_with("Ed25519", {})
    mock_print.assert_called_with("Failed to generate DID: Failed to generate DID")
