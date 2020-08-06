import sys


def cPrint(content):
    "Print content as str to the debug console."
    print(str(content), file=sys.stderr)


def simpleMsgResp(content: str) -> dict:
    """
    Simple def to put content in following dict:
    {
        message: content,
        len: len(content)
    }
    :param content: str - the message to be inserted
    :return: dict containing the message and it's length
    :rtype: dict
    """
    return {'message': content, 'len': len(content)}


def all_as_list_of_dicts(list_of_dicts: list) -> list:
    """
    Function to convert SQLAlchemy list of objects into list of dicts.

    :param list_of_dicts: list - The list of SQLAlchemy objects
    :return: list containing all SQLAlchemy objects as dicts.
    :rtype: list
    """
    result = []
    for item in list_of_dicts:
        result.append(item.as_dict())

    return result
