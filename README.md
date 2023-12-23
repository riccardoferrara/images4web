# images4web
From a input folder containing images, it compress images for the web: it sycronize (or creates eventually) an output folder with the compressed images

# install external libs
python -m pip install 'files @ git+https://github.com/riccardoferrara/files.git'   
python -m pip install 'files @ git+https://github.com/riccardoferrara/files.git' --force

# run test
python -m build
pip install pip install dist/<images4web-package>.whl --force-reinstall
python tests/test_syncronize.py
