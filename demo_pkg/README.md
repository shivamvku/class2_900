# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.






setup and upgrate the setup tool (Wheel)
===============================================
python3 -m pip install --user --upgrade setuptools wheel



Build you pakg
================================================
python3 setup.py sdist bdist_wheel


Upgrade Twine
===========================================
python3 -m pip install --user --upgrade twine



upload to pypi
=============

twine upload dist/*


Installing the pkg globally
================================

pip install pkgname
	

	pip3 install demopkg