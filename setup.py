from setuptools import setup, find_packages

setup(
    name="EcosDataReader",  # 패키지 이름 (PyPI에 표시될 이름)
    version="0.1.0",  # 패키지 버전
    author="jackmappotion",  # 작성자 이름
    author_email="jackmappotion@gmail.com",  # 작성자 이메일
    description="한국은행 OPEN-API 활용을 위한 TOOL",  # 패키지 설명
    long_description=open("README.md", "r", encoding="utf-8").read(),  # 상세 설명 (README.md를 읽어 사용)
    long_description_content_type="text/markdown",  # README 파일 형식 (주로 markdown 사용)
    url="https://github.com/your_username/EcosDataReader",  # 프로젝트 GitHub URL
    packages=find_packages(),  # 패키지 자동 탐색
    classifiers=[  # PyPI 분류 정보
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 지원 Python 버전
    install_requires=[  # 의존성 패키지
        "requests>=2.0.0",
        "pandas>=2.0.0",
    ],
    
)
