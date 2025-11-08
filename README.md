Karas Project Template - A simple project template to quickly start a Python project, with all the boilerplate ready,
without wasting too much time on it.

The template includes:
- uv as a dependency manager
- tests file with a basic pytest test
- docker-compose and Dockerfile for an image with dependencies installed via uv
- pre-commit setup running black (code formatter)
- GitHub CI running black and pytest on Push to GitHub
- basic structure for terraform files
- .gitignore with support for all of the above and some other common file patterns

Feel free to modify it for your needs. If you don't need some part, simply delete it. 

It's published under unilicense, which means you can do with it whatever you want - you don't need to add credits or
anything like that.

WARNING: Delete the license from your project and replace it with the right for you! I recommend using
https://choosealicense.com/ for that.

# But why?
When I come up with a new idea, I want to get right to the fun part - the coding. I want to code, not deal
with quirks of setting up a GitHub pipeline! So I code, and after a few weeks I have a few hundreds/thousands lines of
code... and a terrible mess! Adding black at this point messes up commit history, and even thinking about adding
tests gives me nightmares. Don't even get me started on cloud infrastructure - I didn't have Terraform
set up, so instead of a reproducible infrastructure as a code, I have a few random machines on AWS, which I'm too
afraid to modify at this point.

This is meant to be my remedy.

# Getting started
I usually use it with PyCharm and I do the following steps to start a new project from it:
1. Go to `pyproject.toml` and in `[project]` change the `name` to the name of your project.
2. Install uv if you haven't already:
   - **Linux/macOS**: Run `make install-uv-unix`
   - **Windows**: Run `make install-uv-win`
   - Or see https://docs.astral.sh/uv/getting-started/installation/ for alternative installation methods
3. Run `make install-dependencies` to create a virtual environment and install dependencies (or `uv sync` directly).
4. Create a new test configuration `pytest` and run it. There is one example test in the project - if it passed, you
are setup correctly.