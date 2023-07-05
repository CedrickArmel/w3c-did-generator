import logging
import didkit


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def generator(number: int = 1):
    """
    This function generate a W3C Decentralized Identifier. \n
    Args: \n
        number (int, optional): Number of key to generate. Defaults to 1.
    """
    for _ in range(number) :
        try:
            jwk = didkit.generate_ed25519_key()
            did = didkit.key_to_did("key", jwk)
            logging.info("Output: %s", did)
        except Exception as exc:
            print("Failed to generate DID:", str(exc))
