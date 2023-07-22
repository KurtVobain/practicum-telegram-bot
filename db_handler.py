from vedis import Vedis

import config

def get_current_state(user_id) -> str:
    """
    :descr: Return actual status
    :param user_id: User id
    
    :return: Actual status
    """
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return config.States.S_START.value

def set_state(user_id, value) -> None:
    """
    :descr: Set new state to user and save to db
    :param user_id: User id
    :param value: Value to set
    """
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False
    