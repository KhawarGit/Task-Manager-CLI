import unittest
from to_do_task import TaskManager
import datetime

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task_valid(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]['description'], "Write code")
        self.assertFalse(self.task_manager.tasks[0]['completed'])
        self.assertEqual(self.task_manager.tasks[0]['priority'], "high")
        self.assertEqual(self.task_manager.tasks[0]['due_date'], datetime.datetime(2024, 6, 1))

    def test_add_task_invalid_description(self):
        with self.assertRaises(ValueError):
            self.task_manager.add_task("", "high", "2024-06-01")

    def test_add_task_invalid_priority(self):
        with self.assertRaises(ValueError):
            self.task_manager.add_task("Write code", "urgent", "2024-06-01")

    def test_add_task_invalid_due_date(self):
        with self.assertRaises(ValueError):
            self.task_manager.add_task("Write code", "high", "06-01-2024")

    def test_remove_task_valid(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.remove_task(0)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_remove_task_invalid(self):
        with self.assertRaises(IndexError):
            self.task_manager.remove_task(0)

    def test_mark_task_completed_valid(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.mark_task_completed(0)
        self.assertTrue(self.task_manager.tasks[0]['completed'])

    def test_mark_task_completed_invalid_index(self):
        with self.assertRaises(IndexError):
            self.task_manager.mark_task_completed(0)

    def test_mark_task_completed_already_completed(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.mark_task_completed(0)
        with self.assertRaises(ValueError):
            self.task_manager.mark_task_completed(0)

    def test_list_tasks_empty(self):
        result = self.task_manager.list_tasks()
        self.assertEqual(result, "No tasks available.")

    def test_list_tasks_with_tasks(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.add_task("Review code", "medium", "2024-06-02")
        result = self.task_manager.list_tasks()
        expected = "0: Write code [not completed] Priority: high Due: 2024-06-01\n1: Review code [not completed] Priority: medium Due: 2024-06-02"
        self.assertEqual(result, expected)

    def test_list_tasks_filtered(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.add_task("Review code", "medium", "2024-06-02")
        self.task_manager.mark_task_completed(0)
        result = self.task_manager.list_tasks("completed")
        expected = "0: Write code [completed] Priority: high Due: 2024-06-01"
        self.assertEqual(result, expected)

    def test_update_task_valid(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        self.task_manager.update_task(0, description="Write more code", priority="medium", due_date="2024-06-02")
        self.assertEqual(self.task_manager.tasks[0]['description'], "Write more code")
        self.assertEqual(self.task_manager.tasks[0]['priority'], "medium")
        self.assertEqual(self.task_manager.tasks[0]['due_date'], datetime.datetime(2024, 6, 2))

    def test_update_task_invalid_index(self):
        with self.assertRaises(IndexError):
            self.task_manager.update_task(0, description="Write more code")

    def test_update_task_invalid_priority(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        with self.assertRaises(ValueError):
            self.task_manager.update_task(0, priority="urgent")

    def test_update_task_invalid_due_date(self):
        self.task_manager.add_task("Write code", "high", "2024-06-01")
        with self.assertRaises(ValueError):
            self.task_manager.update_task(0, due_date="06-01-2024")

if __name__ == '__main__':
    unittest.main()
