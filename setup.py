from setuptools import setup

setup(name='bandcamp_dl',
      version='0.2',
      description='Download audio from bandcamp.com',
      long_description= "A module that can download tracks and albums from bandcamp.com.",
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='songs bandcamp_dl bandcamp audio downloader',
      url='http://github.com/sam09/bandcamp_dl',
      author='Sam Radhakrishnan',
      author_email='sk09idm@gmail@gmail.com',
      license='MIT',
      packages=['bandcamp_dl'],
      install_requires=[
          'beautifulsoup4',
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)
