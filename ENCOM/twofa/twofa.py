# -*- coding: utf-8 -*-
import os


def check_2fa_login(password):
    # Need to get env variable
    twofa_password = os.environ["TWO_FA"]

    import hashlib
    n = hashlib.sha512()
    n.update(twofa_password.encode())
    n.update(password.encode())
    return "PUT_HASH_OF_2FA_PASSWORD_HERE" == n.hexdigest()
