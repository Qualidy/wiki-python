import unittest

if __name__ == "__main__":
    # Startet die Testentdeckung im 'tests' Verzeichnis
    loader = unittest.TestLoader()
    start_dir = '.'  # Passe diesen Pfad so an, dass er auf das korrekte Verzeichnis zeigt
    suite = loader.discover(start_dir, pattern="test_*.py")

    # Erstellt den Testrunner, der die Tests ausführt
    runner = unittest.TextTestRunner()
    runner.run(suite)
