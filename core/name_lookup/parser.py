"""Name parsing utilities."""

def parse_name(full_name):
    """Parse full name into components."""
    parts = full_name.strip().split()
    
    if not parts:
        return {"first_name": "", "last_name": "", "middle_name": ""}
    
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    middle_name = " ".join(parts[1:-1]) if len(parts) > 2 else ""
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name
    }