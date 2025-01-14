import random
import re
import argparse
from typing import List, Optional

def clean_search_term(term: str) -> str:
    """Clean and format search term to GitHub naming conventions."""
    # Convert to lowercase and replace spaces with hyphens
    cleaned = term.lower().strip()
    # Replace spaces and special characters with hyphens
    cleaned = re.sub(r'[^a-z0-9]+', '-', cleaned)
    # Remove leading/trailing hyphens
    cleaned = cleaned.strip('-')
    return cleaned

def generate_repo_name(search_terms: List[str]) -> str:
    """Generate a GitHub-style repository name from search terms."""
    # Common GitHub-style suffixes
    suffixes = [
        'app', 'tool', 'hub', 'lab', 'core', 'pro', 
        'lite', 'plus', 'kit', 'suite', 'base'
    ]
    
    # Clean and combine search terms
    cleaned_terms = [clean_search_term(term) for term in search_terms]
    base_name = '-'.join(term for term in cleaned_terms if term)
    
    # If the base name is empty, use a default
    if not base_name:
        base_name = 'my-project'
    
    # 50% chance to add a suffix
    if random.random() < 0.5:
        suffix = random.choice(suffixes)
        return f"{base_name}-{suffix}"
    
    return base_name

def main():
    parser = argparse.ArgumentParser(description='Generate GitHub-style repository names.')
    parser.add_argument('terms', nargs='+', help='Search terms to base the name on')
    parser.add_argument('-n', '--number', type=int, default=3, 
                        help='Number of suggestions to generate (default: 3)')
    
    args = parser.parse_args()
    
    print("\nGenerated repository name suggestions:")
    print("-" * 40)
    
    for i in range(args.number):
        name = generate_repo_name(args.terms)
        print(f"{i+1}. {name}")
    
    print("\nNote: Names follow GitHub naming conventions:")
    print("- Lowercase letters, numbers, and hyphens only")
    print("- No special characters or spaces")

if __name__ == "__main__":
    main()
