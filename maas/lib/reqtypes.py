"""
Request argument types
"""

def boolean(bool_value):
    """
    Request argument boolean type
    """
    lower = str(bool_value).lower()
    if not lower in ('true', 'false'):
        raise ValueError('Invalid value for boolean type: {}'.format(lower))
    return lower == 'true'
