from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

name="Xray",
version="0.0.1",
author="Devendra Singh",
author_email="singhdevendra8398@gmail.com",
install_requires=get_requirements(r"D:\\My Projects\ALL DEEP LEARNING PROJECT\\final_xray\\xray_deep_learning_project\\requirements_dev.txt"),
package=find_packages()

)


