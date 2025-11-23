# Utility functions for LogCutter

def format_data(data):
    """Format data for processing."""
    if isinstance(data, str):
        return data.strip().upper()
    elif isinstance(data, dict):
        return {k: format_data(v) for k, v in data.items()}
    return data

def validate_input(value, min_length=0, max_length=None):
    """Validate input value."""
    if value is None:
        raise ValueError("Value cannot be None")
    if isinstance(value, str):
        if len(value) < min_length:
            raise ValueError(f"Value too short (min {min_length})")
        if max_length and len(value) > max_length:
            raise ValueError(f"Value too long (max {max_length})")
    return True

def process_item(item):
    """Process a single item."""
    validate_input(item)
    return format_data(item)

# Update 11
def helper_11(x):
    return x * 11
