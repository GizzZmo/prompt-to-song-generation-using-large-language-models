# Contributing to Prompt-to-Song Generation using LLMs

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [Issues](https://github.com/GizzZmo/prompt-to-song-generation-using-large-language-models/issues) tab
2. If not, create a new issue with a clear title and description
3. Include steps to reproduce the bug (if applicable)
4. Add relevant labels to help categorize the issue

### Submitting Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines below
3. **Test your changes** thoroughly
4. **Update documentation** if you've added or changed functionality
5. **Commit your changes** with clear, descriptive commit messages
6. **Push to your fork** and submit a pull request

### Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Run linters before submitting (flake8, pylint)
- Format code with `black` and `isort`

### Code Formatting

Before submitting a PR, please format your code:

```bash
# Install formatting tools
pip install black isort flake8

# Format code
black .
isort .

# Check for issues
flake8 .
```

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GizzZmo/prompt-to-song-generation-using-large-language-models.git
   cd prompt-to-song-generation-using-large-language-models
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make your changes and test them

### Commit Message Guidelines

- Use clear and meaningful commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Add detailed description if needed in the commit body

Examples:
- `Add genre classification model`
- `Fix chord progression generation bug`
- `Update README with installation instructions`

### Testing

- Test your changes thoroughly before submitting
- Ensure existing functionality is not broken
- Add comments explaining complex logic

### Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Update examples if the API changes

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Questions?

Feel free to open an issue for any questions or clarifications needed.

Thank you for contributing! 🎵
