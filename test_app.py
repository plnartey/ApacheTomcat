# test_app.py - Basic Test Script for Cloud CI Lab Project

import subprocess
import sys

def test_app_runs_without_error():
    """Test that app.py runs without throwing any errors."""
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"app.py exited with error code {result.returncode}"
    print("✅ PASS: app.py runs without error")

def test_app_output():
    """Test that app.py prints the expected output."""
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True
    )
    expected = "Cloud CI Pipeline Running"
    assert expected in result.stdout, f"Expected '{expected}' in output, got: '{result.stdout}'"
    print(f"✅ PASS: Output contains '{expected}'")

if __name__ == "__main__":
    print("Running tests...\n")
    try:
        test_app_runs_without_error()
        test_app_output()
        print("\n✅ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
