#!/usr/bin/env python3
"""Demo script to test username enumeration across platforms."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.username_enum.platforms import check_all_platforms, check_github, check_reddit

def test_username_enumeration():
    """Test username enumeration with real examples."""
    print("OSINT-Master Username Enumeration Demo")
    print("=" * 50)
    
    # Test with common usernames (safe examples)
    test_usernames = ["github", "admin", "test", "user"]
    
    for username in test_usernames:
        print(f"\nTesting username: {username}")
        print("-" * 30)
        
        results = check_all_platforms(username)
        
        for platform, found in results.items():
            status = "Found" if found else "Not Found"
            print(f"  {platform.title()}: {status}")

def test_specific_platforms():
    """Test specific platforms with known usernames."""
    print("\n" + "=" * 50)
    print("Testing Specific Platforms")
    print("=" * 50)
    
    # Test GitHub (reliable API)
    print("\nTesting GitHub API:")
    github_users = ["octocat", "torvalds", "gaearon"]
    for user in github_users:
        result = check_github(user)
        print(f"  {user}: {'Found' if result else 'Not Found'}")
    
    # Test Reddit (reliable API)
    print("\nTesting Reddit API:")
    reddit_users = ["reddit", "spez", "kn0thing"]
    for user in reddit_users:
        result = check_reddit(user)
        print(f"  {user}: {'Found' if result else 'Not Found'}")

def demonstrate_techniques():
    """Demonstrate different username checking techniques."""
    print("\n" + "=" * 50)
    print("Username Checking Techniques")
    print("=" * 50)
    
    techniques = {
        "API Endpoints": [
            "GitHub: https://api.github.com/users/{username}",
            "Reddit: https://www.reddit.com/user/{username}/about.json"
        ],
        "Web Scraping": [
            "Twitter: https://twitter.com/{username}",
            "Instagram: https://www.instagram.com/{username}/",
            "LinkedIn: https://www.linkedin.com/in/{username}",
            "Facebook: https://www.facebook.com/{username}"
        ],
        "Response Analysis": [
            "Check HTTP status codes (200, 404, 403)",
            "Look for specific error messages",
            "Analyze page content for existence indicators",
            "Handle redirects and blocked requests"
        ]
    }
    
    for category, items in techniques.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item}")

def show_evasion_techniques():
    """Show techniques to avoid being blocked."""
    print("\n" + "=" * 50)
    print("Evasion Techniques")
    print("=" * 50)
    
    evasion_methods = {
        "User Agent Rotation": [
            "Use realistic browser user agents",
            "Rotate between different browsers",
            "Include proper Accept headers"
        ],
        "Rate Limiting": [
            "Add delays between requests",
            "Randomize request timing",
            "Respect robots.txt when possible"
        ],
        "Request Headers": [
            "Include Accept-Language headers",
            "Add Accept-Encoding for compression",
            "Use Connection: keep-alive"
        ],
        "Error Handling": [
            "Handle 429 (Too Many Requests) gracefully",
            "Retry with exponential backoff",
            "Fall back to alternative methods"
        ]
    }
    
    for category, methods in evasion_methods.items():
        print(f"\n{category}:")
        for method in methods:
            print(f"  - {method}")

def show_platform_specifics():
    """Show platform-specific checking methods."""
    print("\n" + "=" * 50)
    print("Platform-Specific Methods")
    print("=" * 50)
    
    platforms = {
        "GitHub": {
            "method": "API",
            "url": "https://api.github.com/users/{username}",
            "detection": "HTTP 200 = exists, 404 = not found",
            "rate_limit": "60 requests/hour (unauthenticated)"
        },
        "Reddit": {
            "method": "API",
            "url": "https://www.reddit.com/user/{username}/about.json",
            "detection": "Check 'data' field in JSON response",
            "rate_limit": "No strict limit for user lookups"
        },
        "Twitter/X": {
            "method": "Web Scraping",
            "url": "https://twitter.com/{username}",
            "detection": "Look for 'This account doesn't exist' text",
            "rate_limit": "Aggressive blocking, use carefully"
        },
        "Instagram": {
            "method": "Web Scraping",
            "url": "https://www.instagram.com/{username}/",
            "detection": "Check for 'Sorry, this page isn't available'",
            "rate_limit": "Blocks automated requests frequently"
        },
        "LinkedIn": {
            "method": "Web Scraping",
            "url": "https://www.linkedin.com/in/{username}",
            "detection": "Look for 'Page not found' or 'Member not found'",
            "rate_limit": "Requires careful handling"
        }
    }
    
    for platform, info in platforms.items():
        print(f"\n{platform}:")
        for key, value in info.items():
            print(f"  {key.title()}: {value}")

def main():
    """Run username enumeration demo."""
    try:
        test_username_enumeration()
        test_specific_platforms()
        demonstrate_techniques()
        show_evasion_techniques()
        show_platform_specifics()
        
        print("\n" + "=" * 50)
        print("Username enumeration demo completed!")
        print("\nIMPORTANT NOTES:")
        print("- Some platforms may block automated requests")
        print("- Use rate limiting to avoid being blocked")
        print("- Respect platform terms of service")
        print("- Only use for legitimate security research")
        
    except Exception as e:
        print(f"Error during testing: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())