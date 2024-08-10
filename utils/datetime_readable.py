import datetime


def format_timestamp(current_time: datetime.datetime) -> str:
    """
    Formats a given datetime object into a human-readable string.

    Parameters:
        current_time (datetime.datetime): The datetime object to be formatted.

    Returns:
        str: A string representing the formatted date and time. The format is "Month Day, Year at Hour:Minute AM/PM".

    Example:
        >>> now = datetime.datetime(2024, 8, 10, 14, 30)
        >>> format_timestamp(now)
        'August 10, 2024 at 02:30 PM'
    """
    return current_time.strftime("%B %d, %Y at %I:%M %p")
