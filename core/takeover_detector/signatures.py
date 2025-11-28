"""Takeover signatures for different cloud providers."""

def get_takeover_signatures():
    """Get signatures for detecting takeover vulnerabilities."""
    return {
        "aws_s3": {
            "cname_patterns": [".s3.amazonaws.com", ".s3-website"],
            "error_messages": ["NoSuchBucket", "The specified bucket does not exist"]
        },
        "azure": {
            "cname_patterns": [".azurewebsites.net", ".cloudapp.net"],
            "error_messages": ["404", "Web app does not exist"]
        },
        "netlify": {
            "cname_patterns": [".netlify.com", ".netlify.app"],
            "error_messages": ["Not Found", "Site not found"]
        },
        "vercel": {
            "cname_patterns": [".vercel.app", ".now.sh"],
            "error_messages": ["404", "The deployment could not be found"]
        },
        "github_pages": {
            "cname_patterns": [".github.io"],
            "error_messages": ["404", "There isn't a GitHub Pages site here"]
        }
    }