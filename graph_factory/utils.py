import random


def dilute_dict(d, num_to_keep=None):
    """
    Remove some random keys from dict
    :param d: the dict
    :param num_to_keep: None means do not dilute, negative mean number to throw
    :return: d diluted
    """
    if num_to_keep is not None:
        if num_to_keep < 0:
            num_to_keep = len(d) + num_to_keep
        keys_to_keep = random.sample(d, num_to_keep)
        d = {k: v for k, v in d.items() if k in keys_to_keep}
    return d


def new_node_name(n, l, sep=':'):
    return "{}{}{}".format(n, sep, l)
