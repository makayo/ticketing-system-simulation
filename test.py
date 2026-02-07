import unittest
from ticketing_system import queue, generate_tickets, process_tickets, next_number

class TestTicketingSystem(unittest.TestCase):

    def setUp(self):
        # Reset queue and numbering before each test
        queue.clear()
        global next_number
        next_number = 1

    # -------------------------
    # NORMAL TEST CASES
    # -------------------------

    def test_single_ticket_generated(self):
        generate_tickets(1)
        self.assertEqual(len(queue), 1)

    def test_multiple_tickets_generated(self):
        generate_tickets(3)
        self.assertEqual(len(queue), 3)

    def test_processing_removes_all_tickets(self):
        generate_tickets(2)
        process_tickets()
        self.assertEqual(len(queue), 0)

    # -------------------------
    # EDGE TEST CASES
    # -------------------------

    def test_generate_zero_tickets(self):
        generate_tickets(0)
        self.assertEqual(len(queue), 0)

    def test_process_with_empty_queue(self):
        process_tickets()  # should not crash
        self.assertEqual(len(queue), 0)

    def test_generate_then_process_one(self):
        generate_tickets(1)
        process_tickets()
        self.assertEqual(len(queue), 0)


if __name__ == "__main__":
    unittest.main()
