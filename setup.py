from setuptools import setup, find_packages

setup(
    name="sems",
    version="0.0.8",
    url="http://github.com/diegorubin/simple-environment-monitor-system",
    author="Diego Rubin",
    author_email="rubin.diego@gmail.com",
    license="GPL2",
    scripts=['bin/sems-start'],
    include_package_data=True,
    description="A Simple Environment Monitor System",
    install_requires=[
        "tornado",
        "tornado_json",
        "tinydb"
    ],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages()
)

