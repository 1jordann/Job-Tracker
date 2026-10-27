import csv
import os
import tempfile
import unittest
from unittest.mock import patch
import job_tracker


class TestJobTracker(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        self.folder = tempfile.TemporaryDirectory()
        self.test_file = os.path.join(
            self.folder.name, "test_applications.csv"
        )

        # Replace the original filename during testing
        self.filename_patch = patch.object(
            job_tracker, "FILENAME", self.test_file
        )
        self.filename_patch.start()

        job_tracker.initialize_file()

    def tearDown(self):
        # Restore the original filename and remove test files
        self.filename_patch.stop()
        self.folder.cleanup()

    def test_initialize_file(self):
        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        self.assertEqual(
            rows[0], ["Company", "Date Applied", "Status"]
        )

    def test_add_application(self):
        with patch("builtins.input", return_value="Google"):
            job_tracker.add_application()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        self.assertEqual(rows[1][0], "Google")
        self.assertEqual(rows[1][2], "Pending")

    def test_blank_company_name(self):
        with patch("builtins.input", return_value="   "):
            job_tracker.add_application()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        # Only the header should exist
        self.assertEqual(len(rows), 1)

    def test_view_applications(self):
        with patch("builtins.input", return_value="Microsoft"):
            job_tracker.add_application()

        with patch("builtins.print") as mock_print:
            job_tracker.view_applications()

        output = str(mock_print.call_args_list)
        self.assertIn("Microsoft", output)

    def test_update_status(self):
        with patch("builtins.input", return_value="Google"):
            job_tracker.add_application()

        with patch(
            "builtins.input",
            side_effect=["google", "Accepted"]
        ):
            job_tracker.update_status()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        self.assertEqual(rows[1][2], "Accepted")

    def test_invalid_status(self):
        with patch("builtins.input", return_value="Google"):
            job_tracker.add_application()

        with patch(
            "builtins.input",
            side_effect=["Google", "Banana"]
        ):
            job_tracker.update_status()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        self.assertEqual(rows[1][2], "Pending")

    def test_delete_application(self):
        with patch("builtins.input", return_value="Google"):
            job_tracker.add_application()

        with patch(
            "builtins.input",
            return_value=" GOOGLE "
        ):
            job_tracker.delete_application()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        # Google should be deleted; header remains
        self.assertEqual(len(rows), 1)

    def test_preserve_existing_records(self):
        for company in ["Google", "Microsoft"]:
            with patch("builtins.input", return_value=company):
                job_tracker.add_application()

        with patch(
            "builtins.input",
            side_effect=["Google", "Accepted"]
        ):
            job_tracker.update_status()

        with open(self.test_file, "r") as file:
            rows = list(csv.reader(file))

        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[1][2], "Accepted")
        self.assertEqual(rows[2][0], "Microsoft")
        self.assertEqual(rows[2][2], "Pending")


if __name__ == "__main__":
    unittest.main()
