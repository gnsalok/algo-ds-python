# Contributing to Algorithms and Data Structures using Python

First off, thank you for considering contributing to this project! It's people like you that make this repository such a great learning resource.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Coding Guidelines](#coding-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

1. Make sure you have Python 3.x installed
2. Fork the repository
3. Clone your fork locally
4. Create a new branch for your contribution
5. Make your changes
6. Push to your fork
7. Submit a Pull Request

## Project Structure

When adding new content, please follow this structure:

```
algo-ds-python/
├── data_structures/
│   ├── arrays/
│   ├── linked_lists/
│   ├── trees/
│   └── ...
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── graph/
│   └── ...
├── tests/
│   ├── test_data_structures/
│   └── test_algorithms/
└── examples/
    ├── array_examples/
    └── ...
```

## Coding Guidelines

### Python Style
- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines
- Use 4 spaces for indentation
- Maximum line length of 79 characters
- Use meaningful variable and function names
- Add type hints where appropriate

### Git Practices

#### Commit Messages
- Use clear and descriptive commit messages
- Start with a verb in the present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Add detailed description if needed after a blank line

#### Changing Commit Messages

1. **For the most recent commit:**
   ```bash
   git commit --amend -m "New commit message"
   ```

2. **For older commits:**
   ```bash
   # Show last n commits
   git rebase -i HEAD~n

   # In the editor, change 'pick' to 'reword' for commits you want to modify
   # Save and close the editor
   # Enter new commit message in the next editor
   ```

3. **If you've already pushed to remote:**
   ```bash
   # After changing commit message locally
   git push --force-with-lease origin your-branch-name
   ```
   ⚠️ Note: Only force push to your own feature branches, never to main/master!

### Example Implementation Structure

```python
def algorithm_name(param1: type1, param2: type2) -> return_type:
    """
    Brief description of what the algorithm does.

    Args:
        param1 (type1): Description of param1
        param2 (type2): Description of param2

    Returns:
        return_type: Description of return value

    Time Complexity: O(n)
    Space Complexity: O(1)

    Example:
        >>> algorithm_name(1, 2)
        3
    """
    # Implementation
    pass
```

## Documentation Guidelines

### Required Documentation
1. **Docstrings**: Every function and class must have a docstring that includes:
   - Brief description
   - Parameters and their types
   - Return value and type
   - Time and space complexity
   - Example usage

2. **Comments**:
   - Add comments for complex logic
   - Explain any non-obvious decisions
   - Document any assumptions

3. **README**:
   - If adding a new category, include a README.md in that directory
   - Explain the concept
   - Include relevant resources and references

## Testing Guidelines

1. **Test Structure**
   - Place tests in the `tests/` directory
   - Follow the same structure as the main code
   - Name test files with `test_` prefix

2. **Test Requirements**
   - Include unit tests for all new functions
   - Test edge cases
   - Test expected failures
   - Aim for high test coverage

3. **Example Test**:
```python
def test_algorithm_name():
    # Arrange
    input_data = [1, 2, 3]
    expected_output = 6

    # Act
    result = algorithm_name(input_data)

    # Assert
    assert result == expected_output
```

## Pull Request Process

1. **Before Submitting**
   - Ensure all tests pass
   - Update documentation if needed
   - Add your changes to CHANGELOG.md if it exists
   - Squash related commits

2. **PR Description**
   - Clearly describe the changes
   - Link any related issues
   - Include example output if applicable
   - List any breaking changes

3. **Review Process**
   - Address review comments promptly
   - Keep discussions focused and professional
   - Be open to suggestions and feedback

4. **After Merging**
   - Delete your branch
   - Update your fork
   - Celebrate your contribution! 🎉

## Questions?

If you have any questions or need clarification, feel free to:
1. Open an issue
2. Contact the maintainers
3. Ask for help in your pull request

Thank you for contributing to making this project better! 🙏 