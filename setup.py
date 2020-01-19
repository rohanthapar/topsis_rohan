import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bawa_rohan',     #How the package folder is named
    packages = ['bawa_rohan'],   #Same name as "name"
    version='0.1',  #Update version with every change you make
    license='MIT',   # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'This package allows you to run topsis on your dataset for Multiple Attribute Decision Making(MADM) on python',  
    author="Rohan Bawa",
    author_email="rohanbawa8f@gmail.com",
    url = 'https://github.com/rohanthapar/topsis_rohan',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/jaskeerat31/topsis_jaskeerat/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'DATA ANALYSTICS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
