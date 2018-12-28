from setuptools import setup

setup(name='pygriffinlim',
      version='0.1',
      description='An implementation of the Griffin Lim Algorithm',
      author='Ramsey Barghouti',
      license='GPL3',
      packages=['pygriffinlim'],
      install_requires=[
            "numpy",
            "librosa",
      ],
      entry_points={
            "console_scripts": [
                  "pygl=pygriffinlim.cli:main"
            ]
      },
      zip_safe=False)
