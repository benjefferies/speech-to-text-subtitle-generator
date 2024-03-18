from setuptools import setup, find_packages

setup(
    name='speech-to-text-subtitle-generator',
    version='1.0.0',
    packages=find_packages(),
    author='Ben Jefferies',
    author_email='benjefferies@echosoft.uk',
    description='A tool to generate subtitles from audio files using the Whisper model.',
    entry_points={
        'console_scripts': [
            'speech-to-text-subtitle-generator = speech_to_text:main',
        ],
    },
)
