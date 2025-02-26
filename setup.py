from setuptools import setup

setup(
    name='sonos_ping',
    version='0.1.0',    
    description='A simple Sonos ping utility',
    url='https://github.com/jaygalvin/my-cool-workspace/',
    author='Jay Galvin',
    author_email='sgtgalvin@gmail.com',
    license='BSD 2-clause',
    packages=['sonos_ping'],
    install_requires=['soco',
                      'netdisco',
                      'urllib3'
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)