import unittest
import sql_questions
import sqlalchemy_questions

NAME = "🟥Fabian Neumann🟥"


# 🟨Den Rest der Datei kannst du ignorieren.🟨
# Ich nutze diese nur, um schnell alle Ergebnisse zusammenzustellen.

def load_tests_from_module(module):
    # Erstelle eine TestSuite für das Modul
    suite = unittest.TestSuite()
    # Durchlaufe alle Attribute des Moduls, um Testklassen zu finden
    for name in dir(module):
        obj = getattr(module, name)
        # Prüfe, ob das Attribut eine Testklasse ist
        if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
            # Lade alle Tests aus der Testklasse
            suite.addTest(unittest.makeSuite(obj))
    return suite


def evaluate_result(test_result: unittest.TestResult):
    count_errors = len(test_result.errors)
    count_failures = len(test_result.failures)
    count_tests_run = test_result.testsRun
    count_success = count_tests_run - count_errors - count_failures
    return count_tests_run, count_success


if __name__ == '__main__':
    test_modules = [sql_questions, sqlalchemy_questions]
    suite = unittest.TestSuite()

    # Lade die Tests aus jedem Modul
    for module in test_modules:
        suite.addTest(load_tests_from_module(module))

    # Erstelle einen TestRunner und führe die TestSuite aus
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    testsRun, successes = evaluate_result(result)
    print(f"Ergebnis {NAME}:\n"
          f"gelaufene Tests: {testsRun},\n"
          f"Erfolgreiche Tests: {successes},\n"
          f"Anteil erfolgreich: {100 * successes / testsRun:.0f}%\n")
