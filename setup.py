from setuptools import setup, find_packages

setup(
    name="enrichr_plot",
    version="1.0.0",
    description="A tool for enrichment analysis visualization and filtering",
    author="Christoffer Frisk",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "seaborn",
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "enrichr-plot=enrichr_plot.cli:main",
        ]
    },
)
