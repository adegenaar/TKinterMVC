"""
    Observer Pattern - event
"""
from typing import Any, Callable, List

subscribers: dict[str, List[Callable]] = {}


def subscribe(event_type: str, fn_handler: Callable) -> None:
    """
    subscribe Add a listener for the Event

    Args:
        event_type (str): Name of the Event
        fn (function): function to call when the event is triggered
    """
    if not event_type in subscribers:
        subscribers[event_type] = []
    else:
        subscribers[event_type].append(fn_handler)


def post_event(event_type: str, data: Any) -> None:
    """
    post_event Inform all of the registered listeners that the event has occurred

    Args:
        event_type (str): Name of the Event
        data ([type]): data to pass along with the Event
    """
    if not event_type in subscribers:
        return
    for observer in list(subscribers[event_type]):
        observer(data)
