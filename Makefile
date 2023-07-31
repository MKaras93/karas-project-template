# Example Makefile with most often used commands.


#  loads .env file so that env variables are available in commands
include .env
export

init-pre-commit:
	pip3 install pre-commit
	pre-commit install

install-dependencies:
	  python3 -m pip install --upgrade pip setuptools wheel
	  python3 -m pip install poetry
	  python3 -m poetry install -v --no-root --compile

# example ssh access command - configure via .env file
remote-ssh:
	ssh -i $(PRIVATE_KEY_FILE_LOCATION) $(REMOTE_USER)@$(REMOTE_ADDRESS)

# example ssh deploy command - adds git deploy key to ssh agent and pulls newest version of main branch
DEPLOY_COMMAND=cd project && ssh-agent bash -c 'ssh-add ../git-deploy-key && git pull origin main && git checkout main && git status'
remote-deploy:
	ssh -i $(PRIVATE_KEY_FILE_LOCATION) $(REMOTE_USER)@$(REMOTE_ADDRESS) \
	 "$(DEPLOY_COMMAND)"
