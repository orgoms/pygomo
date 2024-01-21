# Contributing Guidelines

Thank you for your interest in contributing to this project! We appreciate your help
in making it better. By following these guidelines, you can help us maintain a
collaborative and productive environment for everyone involved.

## Getting Started

### Issues

If you encounter a bug or have a feature request,
please check if there's already an existing issue;
if not, kindly open a new issue with a clear description.

1. **Go to the "Issues" tab** [here][issues]
2. **Click the "New issue" button**
3. **Follow the guidelines**
4. **Click the "Submit new issue" button**

### Development Setup

If you want to set up a development environment to develop your contribution,
follow these steps:

1. **Fork the repository** by clicking the "Fork" button [here][repository]
2. **Clone the forked repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/pyndow.git
   ```
3. **Change the directory**:
   ```bash
   cd vorcle
   ```
4. **Add the upstream repository** as a remote:
     ```bash
     git remote add upstream https://github.com/vorcle/pyndow.git
     ```
5. **Install `pdm`** by following the [installation instructions][pdm-installation]
6. **Install the dependencies** from the lock file:
   ```bash
   pdm install
   ```

### Making Changes

After you're done setting up a development environment,
you can now develop your contributions.

1. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature-branch
   ```
2. **Make your changes** to the codebase
3. **Commit your changes**:
   ```bash
   git commit -m "Your descriptive commit message here"
   ```
4. **Push your changes** to the forked repository:
   ```bash
   git push origin feature-branch
   ```

### Pull Requests

After you're done developing your contributions,
you can now create a pull request.

1. **Go to the "Pull requests" tab** of the forked repository
2. **Click the "New pull request" button**
3. **Select the base repository**, ideally the original repository
4. **Select the base branch**, ideally the `main` branch
5. **Select the head repository**, ideally the forked repository
6. **Select the branch to compare**, ideally the branch you made your contributions
7. **Click the "Create pull request" button**
8. **Follow the guidelines**
9. **Click the "Create pull request" button**

If your changes are still a work in progress (WIP) or if you want to gather
feedback before formal review, you can create a draft pull request.

1. **Before clicking the "Create pull request" button**,
   look for the dropdown menu next to it.
2. **Select "Create draft pull request"** instead.

When your changes are complete and you are confident in the quality of your code,
you can update the pull request to indicate that it is ready for review.
Simply click the "Ready for review" button.

### Commit Guidelines

**Format:**
```
[optional-scope] subject

optional-body
```

**General Rules:**
- The first line must not exceed 72 characters
- The scope must be surrounded with square brackets
- The subject must use the imperative mood
- The subject must be seperated from body with a blank line
- The body must wrap at 88 characters

**Advices:**
- The first line should be assumed as the most important
- The first line should not exceed 50 characters
- The subject should start with a capitalized letter
- The subject should not end with a period
- The body should wrap at 72 characters
- The body should explain as to *what* and *why*

## Code of Conduct

This project and everyone participating in it is governed by our
[Code of Conduct][code-of-conduct]. By participating, you are expected
to uphold this code. Please report any unacceptable behavior.

## License

By contributing to this project, you agree that your contributions will be
licensed under the BSD 2-Clause “Simplified” License - see the [LICENSE.txt](license)
file for details.

[repository]: https://github.com/vorcle/pyndow
[issues]: https://github.com/vorcle/pyndow/issues
[pulls]: https://github.com/vorcle/pyndow/pulls
[pdm-installation]: https://pdm-project.org/latest/#installation
[code-of-conduct]: https://github.com/vorcle/pyndow/blob/main/CODE_OF_CONDUCT.md
[license]: https://github.com/vorcle/pyndow/blob/main/LICENSE.txt
