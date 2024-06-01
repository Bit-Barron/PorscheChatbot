from setuptools import setup, find_packages

setup(
    name='porsche_chatbot_api',
    version='1.0.0',
    description='An API for a chatbot with speech-to-text and text-to-speech functionality for Porsche.',
    author='Bit Barron',
    author_email='lolha6773@gmail.com',
    url='https://github.com/Bit-Barron/PorscheChatbot', 
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Flask>=2.0',
        'requests>=2.25',
        'numpy>=1.19',
        'scipy>=1.6',
        'tensorflow>=2.5',  
        'torch>=1.8',       
        'transformers>=4.5',  
        'beautifulsoup4>=4.9',  
        'pandas>=1.2', 
    ],
    extras_require={
        'dev': [
            'pytest>=6.2',
            'flake8>=3.8',
            'black>=21.4b0',
            'mypy>=0.812',
        ],
    },
    entry_points={
        'console_scripts': [
            'start-chatbot-api=api.api:main',  
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
)
