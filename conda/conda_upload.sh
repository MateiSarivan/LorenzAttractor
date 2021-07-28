# Only need to change these two variables
PKG_NAME=lorat
USER=mateisarivan

OS=linux-64
mkdir ~/conda-bld
conda config --set anaconda_upload no
export CONDA_BLD_PATH=~/conda-bld
export VERSION="0.0.7"
conda build -c conda-forge .
anaconda -t $CONDA_UPLOAD_TOKEN upload -u $USER $CONDA_BLD_PATH/$OS/$PKG_NAME-$VERSION-py39hfeaa757-1.tar.bz2 --force