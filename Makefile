# Example Makefile with most often used commands.


#  loads .env file so that env variables are available in commands
include .env
export

init-pre-commit:
	pip3 install pre-commit
	pre-commit install

install-uv-unix:
	curl -LsSf https://astral.sh/uv/install.sh | sh

install-uv-win:
	powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

install-dependencies:
	@which uv > /dev/null 2>&1 || (echo "Error: uv is not installed. Please run 'make install-uv-unix' (Linux/macOS) or 'make install-uv-win' (Windows)" && exit 1)
	uv sync --extra dev

# example ssh access command - configure via .env file
remote-ssh:
	ssh -i $(PRIVATE_KEY_FILE_LOCATION) $(REMOTE_USER)@$(REMOTE_ADDRESS)

# example ssh deploy command - adds git deploy key to ssh agent and pulls newest version of main branch
DEPLOY_COMMAND=cd project && ssh-agent bash -c 'ssh-add ../git-deploy-key && git pull origin main && git checkout main && git status'
remote-deploy:
	ssh -i $(PRIVATE_KEY_FILE_LOCATION) $(REMOTE_USER)@$(REMOTE_ADDRESS) \
	 "$(DEPLOY_COMMAND)"
