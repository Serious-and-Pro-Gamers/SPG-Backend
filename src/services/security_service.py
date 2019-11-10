import hashlib
import requests


# Use pwned password api to get the number of online breaches for the password
def get_password_breaches(password):
    # Api endpoint for pwned password api
    pwned_uri = "https://api.pwnedpasswords.com/range/"

    # Encrypt password using sha-1 (Used by the pwned password api)
    sha1_pw = hashlib.sha1(password.encode()).hexdigest()

    # Process the sha-1 hash into prefix / suffix
    # Prefix: first 5 chars
    # Suffix: everything after first 5 chars
    sha1_pw_prefix = sha1_pw[:5].upper()
    sha1_pw_suffix = sha1_pw[5:].upper()

    # Send a get request to the pwned password api with the sha-1 prefix
    pwned_response = requests.get(pwned_uri + sha1_pw_prefix).text
    # Split the response into multiple lines containing suffix hashes
    pwned_hashes = pwned_response.splitlines()
    # Find the suffix hash that corresponds to the user's password suffix
    hash_list = [pwned_hash[pwned_hash.find(":") + 1:] for pwned_hash in pwned_hashes if sha1_pw_suffix in pwned_hash]
    # get first elemnt of the hash list (should be one since there should only be one record of the hash suffix in the hash list)
    breaches = hash_list[0] if len(hash_list) > 0 else 0

    # Return number of password breaches as an integer
    return int(breaches)


def process_password(password):
    # Get number of online breaches using pwned api
    password_breaches = get_password_breaches(password)

    # TODO: Finish encrypting password and send to the database

    return password_breaches
