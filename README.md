# geckodriver-binary
Downloads and installs the [geckodriver](https://github.com/mozilla/geckodriver) binary version @@GECKODRIVER_VERSION@@ or automated testing of webapps. The installer supports Linux, MacOS and Windows operating systems.

## Installation

### From PyPI
```
pip install geckodriver-binary
```

### From GitHub
```
pip install git+https://github.com/ramonmedeiros/geckodriver-binary.git
```

## Usage
To use geckodriver just `import geckodriver_binary`. This will add the executable to your PATH so it will be found. You can also get the absolute filename of the binary with `geckodriver_binary.geckodriver_filename`.

### Example
```
from selenium import webdriver
import geckodriver_binary  # Adds geckodriver binary to path

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
```

### Exporting geckodriver binary path
This package installs a small shell script `geckodriver-path` to easily set and export the PATH variable:
```
$ export PATH=$PATH:`geckodriver-path`
```

### This project is based and inspire on https://github.com/danielkaiser/python-chromedriver-binary
