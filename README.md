# GitName

GitName is a Python utility that generates GitHub-style repository names from search terms. It helps developers create consistent, well-formatted repository names following GitHub naming conventions.

## Features

- Generates repository names based on user-provided search terms
- Follows GitHub naming conventions (lowercase, hyphens, no special characters)
- Optionally adds common GitHub-style suffixes (e.g., -app, -core, -suite)
- Supports multiple name suggestions in a single run
- Clean and straightforward command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/makalin/GitName.git
cd GitName
```

2. Ensure you have Python 3.6+ installed.

3. No additional dependencies required - the script uses only Python standard library modules.

## Usage

Run the script from the command line with your desired search terms:

```bash
python gitname.py [search terms] [-n number_of_suggestions]
```

### Arguments

- `search terms`: One or more words to base the repository name on (required)
- `-n, --number`: Number of name suggestions to generate (optional, default: 3)

### Examples

Generate 3 name suggestions for a Python web scraper:
```bash
python gitname.py python web scraper
```

Generate 5 name suggestions for a machine learning project:
```bash
python gitname.py machine learning -n 5
```

## How It Works

1. The script takes input search terms and cleans them according to GitHub naming conventions:
   - Converts to lowercase
   - Replaces spaces and special characters with hyphens
   - Removes leading/trailing hyphens

2. It combines the cleaned terms with hyphens

3. Optionally adds common GitHub-style suffixes (50% chance) such as:
   - app
   - tool
   - hub
   - lab
   - core
   - pro
   - lite
   - plus
   - kit
   - suite
   - base

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest new features
3. Add more suffix options
4. Improve documentation
5. Submit pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by GitHub's repository naming conventions
- Built to help developers maintain consistent naming practices
