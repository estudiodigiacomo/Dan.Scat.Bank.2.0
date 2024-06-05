from setuptools import setup, find_packages

setup(
    name='dnaiel_scattone_banks',
    version='0.1.0',
    description='Proyecto de gestión de bancos para descarga de datos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bruno Chamús - Estudio Di Giacomo',
    author_email='bruno@estudiodigiacomo.com',
    url='https://github.com/tu_usuario/tu_repositorio',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'selenium'
        'tkinter'
        'setuptools'
        'reportlab'
        'PyPDF2'
        'python-dateutil'
        'pyautogui'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
