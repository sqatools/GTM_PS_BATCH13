"""
Installation Verification Script
Run this to check if all dependencies are properly installed
"""

import sys
import subprocess

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    import_name = import_name or package_name.replace('-', '_')
    
    try:
        __import__(import_name)
        print(f"✓ {package_name:30} - Installed")
        return True
    except ImportError:
        print(f"✗ {package_name:30} - NOT installed")
        return False


def main():
    print("\n" + "="*70)
    print("RAG_1 Dependency Verification")
    print("="*70 + "\n")
    
    packages = [
        ("langchain", "langchain"),
        ("langchain-core", "langchain_core"),
        ("langchain-community", "langchain_community"),
        ("langchain-openai", "langchain_openai"),
        ("langchain-text-splitters", "langchain_text_splitters"),
        ("faiss-cpu", "faiss"),
        ("openai", "openai"),
        ("python-docx", "docx"),
        ("pypdf", "pypdf"),
        ("python-dotenv", "dotenv"),
        ("pytest", "pytest"),
        ("pytest-cov", "pytest_cov"),
        ("pytest-mock", "pytest_mock"),
    ]
    
    installed = 0
    missing = 0
    
    print("Checking installed packages:\n")
    for package, import_name in packages:
        if check_package(package, import_name):
            installed += 1
        else:
            missing += 1
    
    print("\n" + "="*70)
    print(f"Summary: {installed} installed, {missing} missing")
    print("="*70 + "\n")
    
    if missing > 0:
        print("To install all dependencies, run:\n")
        print("  pip install -r requirements.txt\n")
        print("Or manually install missing packages:\n")
        print("  pip install langchain-core langchain-community langchain-openai")
        print("  pip install faiss-cpu python-docx pypdf python-dotenv\n")
        return 1
    else:
        print("✓ All dependencies are installed!\n")
        print("You can now run tests:\n")
        print("  pytest tests/ -v\n")
        return 0


if __name__ == "__main__":
    sys.exit(main())
