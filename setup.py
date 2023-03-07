from distutils.core import setup

setup(
    name='slick-pay',
    packages=['slick-pay'],  # Chose the same as "name"
    version='0.3',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='slick-pay Gateway (Python Library)',  # Give a short description about your library
    author='Rahim',  # Type in your name
    author_email='hala.rahim@azimutbs.com',  # Type in your E-Mail
    url='https://github.com/Slick-Pay-Algeria/python-slick-pay-package',  # Provide either the link to your github or to your website
    download_url='',  # I explain this later on
    keywords=['e-pay', 'slick-pay', 'edahabia', 'cib'],  # Keywords that define your package best

    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
