""" Struct utility functions, like providing all current struct instances. """

from typing import List, Tuple


def get_instances() -> List[Tuple[str, "Struct"]]:
    """ Returns a list containing all existing struct instances.

    :return: A list of tuples, each containing a struct and its name.
    """
    # this can only be imported here, else it causes a circle import
    #pylint: disable=import-outside-toplevel,cyclic-import
    from blenderproc.python.types.StructUtility import Struct
    return [
        (instance.get_name(), instance)
        for instance in Struct.__refs__
        if instance.is_valid()
    ]
