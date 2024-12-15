import unittest
from lab4.task13.src.task13_2 import isEmpty, enqueue, dequeue, isFull, display

class TestQueueOperations(unittest.TestCase):

    def test_should_return_true_when_queue_is_empty(self):
        # given
        head = None

        # when
        result = isEmpty(head)

        # then
        self.assertTrue(result)

    def test_should_return_false_when_queue_is_not_empty(self):
        # given
        head, tail, size = None, None, 0
        head, tail, size = enqueue(head, tail, size, 10)

        # when
        result = isEmpty(head)

        # then
        self.assertFalse(result)

    def test_should_return_true_when_queue_is_full(self):
        # given
        size = 3
        max_size = 3

        # when
        result = isFull(size, max_size)

        # then
        self.assertTrue(result)

    def test_should_enqueue_elements_until_full(self):
        # given
        head, tail, size = None, None, 0

        # when
        head, tail, size = enqueue(head, tail, size, 1)
        head, tail, size = enqueue(head, tail, size, 2)
        head, tail, size = enqueue(head, tail, size, 3)

        # then
        self.assertEqual(size, 3)  # Размер очереди должен быть 3
        with self.assertRaises(OverflowError):
            enqueue(head, tail, size, 4)  # Очередь полна, добавление должно вызвать ошибку

    def test_should_dequeue_elements_correctly(self):
        # given
        head, tail, size = None, None, 0
        head, tail, size = enqueue(head, tail, size, 1)
        head, tail, size = enqueue(head, tail, size, 2)
        head, tail, size = enqueue(head, tail, size, 3)

        # when
        value, head, tail, size = dequeue(head, tail, size)

        # then
        self.assertEqual(value, 1)  # Удалён первый элемент
        self.assertEqual(size, 2)  # Размер уменьшился до 2
        self.assertFalse(isEmpty(head))  # Очередь не пуста

    def test_should_raise_exception_when_dequeue_from_empty_queue(self):
        # given
        head, tail, size = None, None, 0

        # then
        with self.assertRaises(IndexError) as context:
            dequeue(head, tail, size)

        self.assertEqual(str(context.exception), "Dequeue from empty queue")

    def test_should_display_queue_correctly(self):
        # given
        head, tail, size = None, None, 0
        head, tail, size = enqueue(head, tail, size, 10)
        head, tail, size = enqueue(head, tail, size, 20)
        head, tail, size = enqueue(head, tail, size, 30)

        # when
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        display(head)

        sys.stdout = sys.__stdout__

        # then
        expected_output = "10 -> 20 -> 30 -> None\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
