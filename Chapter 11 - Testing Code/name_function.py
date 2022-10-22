def get_formatted_name(first, last, middle=''):
    """Generate a nearly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_name_and_middle(first, last, middle):
    """Generate a nearly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()