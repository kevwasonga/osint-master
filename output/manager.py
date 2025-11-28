"""Output management functionality."""

import json
import os
from datetime import datetime
from .formatters import format_txt, format_json

def save_results(data, filename):
    """Save results to file in appropriate format."""
    # Ensure output directory exists
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
    
    if filename.endswith(".json"):
        save_json(data, filename)
    else:
        save_txt(data, filename)
    
    print(f"Data saved in {filename}")

def save_json(data, filename):
    """Save data in JSON format."""
    formatted_data = format_json(data)
    with open(filename, 'w') as f:
        json.dump(formatted_data, f, indent=2)

def save_txt(data, filename):
    """Save data in TXT format."""
    formatted_data = format_txt(data)
    with open(filename, 'w') as f:
        f.write(formatted_data)