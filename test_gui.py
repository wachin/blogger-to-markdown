#!/usr/bin/env python3
"""
Test script to verify GUI dependencies and basic functionality
"""

import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...\n")
    
    tests = [
        ("requests", "Requests library"),
        ("bs4", "BeautifulSoup4"),
        ("html2text", "HTML2Text"),
        ("lxml", "LXML parser"),
        ("PyQt5.QtWidgets", "PyQt5 Widgets"),
        ("PyQt5.QtCore", "PyQt5 Core"),
        ("PyQt5.QtGui", "PyQt5 GUI"),
    ]
    
    failed = []
    
    for module_name, description in tests:
        try:
            __import__(module_name)
            print(f"✓ {description:20} OK")
        except ImportError as e:
            print(f"✗ {description:20} FAILED")
            failed.append((module_name, description, str(e)))
    
    print()
    
    if failed:
        print("❌ Some imports failed:\n")
        for module_name, description, error in failed:
            print(f"  - {description}: {error}")
        print("\nInstall missing dependencies:")
        print("  source venv/bin/activate")
        print("  pip install -r requirements.txt")
        return False
    else:
        print("✅ All imports successful!")
        return True

def test_pyqt():
    """Test PyQt5 basic functionality"""
    print("\n🧪 Testing PyQt5...\n")
    
    try:
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
        
        print(f"  Qt Version: {QT_VERSION_STR}")
        print(f"  PyQt Version: {PYQT_VERSION_STR}")
        
        # Try to create a QApplication instance
        app = QApplication(sys.argv)
        print("  ✓ QApplication created successfully")
        
        return True
    except Exception as e:
        print(f"  ✗ PyQt5 test failed: {e}")
        return False

def test_translations():
    """Test if translation files exist"""
    print("\n🧪 Testing translations...\n")
    
    import os
    
    translation_files = [
        "translations/blog_downloader_en.ts",
        "translations/blog_downloader_es.ts",
    ]
    
    all_exist = True
    for file_path in translation_files:
        if os.path.exists(file_path):
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} not found")
            all_exist = False
    
    # Check for compiled translations (optional)
    print("\n  Compiled translations (.qm files):")
    compiled_files = [
        "translations/blog_downloader_en.qm",
        "translations/blog_downloader_es.qm",
    ]
    
    any_compiled = False
    for file_path in compiled_files:
        if os.path.exists(file_path):
            print(f"    ✓ {file_path}")
            any_compiled = True
        else:
            print(f"    ℹ {file_path} (optional, not compiled yet)")
    
    if not any_compiled:
        print("\n  ℹ️  To compile translations, run:")
        print("     ./compile_translations.sh")
    
    return all_exist

def main():
    """Run all tests"""
    print("=" * 60)
    print("  Blog Downloader GUI - Dependency Test")
    print("=" * 60)
    print()
    
    results = []
    
    # Test imports
    results.append(("Imports", test_imports()))
    
    # Test PyQt
    results.append(("PyQt5", test_pyqt()))
    
    # Test translations
    results.append(("Translations", test_translations()))
    
    # Summary
    print("\n" + "=" * 60)
    print("  Test Summary")
    print("=" * 60)
    print()
    
    all_passed = True
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {test_name:20} {status}")
        if not passed:
            all_passed = False
    
    print()
    
    if all_passed:
        print("✅ All tests passed! You're ready to run the GUI.")
        print("\nTo start the application:")
        print("  ./run_gui.sh")
        return 0
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("\nTo install dependencies:")
        print("  source venv/bin/activate")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
