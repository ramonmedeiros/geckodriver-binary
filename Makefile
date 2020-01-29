default: clean package

package:
	python3 setup.py sdist

clean:
	rm -f geckodriver_binary/geckodriver
	rm -rf geckodriver_binary.egg-info build dist
	find . -name __pycache__ | xargs rm -rf 
	find . -name *pyc | xargs rm -rf 
