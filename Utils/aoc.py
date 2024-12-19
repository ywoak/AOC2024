import os
import sys
import subprocess

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

GRAY = "\033[1;30m"
BLUE = "\033[1;34m"
RED = "\033[1;31m"
RESET = "\033[0m"

def get_python_file():
    """Récupère le fichier Python dans le répertoire actuel."""
    python_files = [f for f in os.listdir() if f.endswith(".py") and f != "aoc.py"]
    if len(python_files) != 1:
        print(f"{RED}Erreur : un seul fichier Python est attendu.{RESET}")
        sys.exit(1)
    return python_files[0]

def run_tests():
    """Exécute les tests."""
    for test_file in sorted(f for f in os.listdir() if f.startswith("test") and f.endswith(".txt")):
        result = subprocess.run(
            [sys.executable, get_python_file()],
            input=open(test_file).read(),
            text=True,
            capture_output=True,
            env={**os.environ, 'PYTHONPATH': os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils'))}
        )

        print(f"{GRAY}{result.stdout}{RESET}\n\n")
        if result.stderr:
            print(f"{RED}{result.stderr}{RESET}")

def run_input():
    """Exécute avec input.txt."""
    input_file = "input.txt"
    if os.path.exists(input_file):
        result = subprocess.run(
            [sys.executable, get_python_file()],
            input=open(input_file).read(),
            text=True,
            capture_output=True,
            env={**os.environ, 'PYTHONPATH': os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils'))}
        )

        print(f"{BLUE}{result.stdout}{RESET}")
        if result.stderr:
            print(f"{RED}{result.stderr}{RESET}")
    else:
        print(f"{RED}Le fichier input.txt est introuvable.{RESET}")

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    if mode in ["both", "t"]:
        run_tests()
    if mode in ["both", "i"]:
        run_input()

if __name__ == "__main__":
    main()
