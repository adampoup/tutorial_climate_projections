from setuptools import setup

name = 'tutorial_climate_projections'
reqs = ['Cartopy ==0.23.0', 'matplotlib ==3.9.1', 'netCDF4 ==1.7.1.post1',
        'numpy ==2.0.1', 'pandas ==2.2.2', 'rasterio ==1.3.10', 'shapely ==2.0.5',
        'jupyter', 'jupyterlab']

setup(name=name, install_requires=reqs)
