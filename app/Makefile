# Define the package manager (npm or yarn)
PKG_MANAGER := npm

default: test

# Install dependencies
install:
	$(PKG_MANAGER) install

# Run tests
# Change 'jest' to 'mocha' or any other testing framework if needed
test:
	$(PKG_MANAGER) test

# Clean node_modules (optional)
clean:
	rm -rf node_modules

# Reinstall dependencies
reinstall: clean install