import logging
import didkit


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def generator():
    """_summary_
    This function generate a W3C Decentralized Identifier.
    """
    jwk = didkit.generate_ed25519_key()
    try:
        did = didkit.key_to_did("key", jwk)
        logging.info("Output: %s", did)
    except Exception as exc:
        print("Failed to generate DID:", str(exc))
