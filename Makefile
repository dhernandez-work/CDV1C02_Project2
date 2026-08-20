# ==============================================================================
# ClassGroup Manager - Environment Automation Makefile
# ------------------------------------------------------------------------------
# This file automates the teardown, recreation, and dependency installation 
# for both the Development workspace and the Production server environments.
# ==============================================================================

.PHONY: dev prod clean push tag

# ------------------------------------------------------------------------------
# Target: dev
# Purpose: Builds the local development environment with the (DEV) prompt.
# ------------------------------------------------------------------------------
dev: clean
	@echo ">>> Building DEV Workspace..."
	python3 -m venv venv --prompt="DEV"
	venv/bin/python -m pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	@echo ">>> DEV Workspace is ready! Run 'source venv/bin/activate' to enter."

# ------------------------------------------------------------------------------
# Target: prod
# Purpose: Builds the isolated production environment with the (PROD) prompt.
# ------------------------------------------------------------------------------
prod: clean
	@echo ">>> Building PROD Server Environment..."
	python3 -m venv venv --prompt="PROD"
	venv/bin/python -m pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	@echo ">>> PROD Environment is ready! Run 'source venv/bin/activate' and 'python3 app.py'."

# ------------------------------------------------------------------------------
# Target: clean
# Purpose: Safely removes the existing virtual environment to ensure a fresh build.
# ------------------------------------------------------------------------------
clean:
	@echo ">>> Removing existing virtual environment..."
	rm -rf venv

# ------------------------------------------------------------------------------
# Target: push
# Purpose: Automates the Git add, commit, and push sequence to the current branch.
# Usage: make push m="your commit message here"
# ------------------------------------------------------------------------------
push:
	@echo ">>> Staging all changes..."
	git add .
	@echo ">>> Committing with message: $(m)"
	git commit -m "$(m)"
	@echo ">>> Pushing current branch to origin..."
	git push origin HEAD

# ------------------------------------------------------------------------------
# Target: tag
# Purpose: Tags the current commit with a version number and pushes the tag.
# Usage: make tag v="1.0.0" m="Release 1.0.0 - Added web interface"
# ------------------------------------------------------------------------------
tag:
	@echo ">>> Tagging release v$(v)..."
	git tag -a v$(v) -m "$(m)"
	@echo ">>> Pushing tag to GitHub..."
	git push origin v$(v)