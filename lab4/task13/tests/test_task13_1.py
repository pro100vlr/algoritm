import unittest
from lab4.task13.src.task13_1 import isEmpty, push, pop, display

class TestStackOperations(unittest.TestCase):
    
    def test_should_return_true_when_stack_is_empty(self):

        # given
        stack = None

        # when
        result = isEmpty(stack)

        # then
        self.assertTrue(result)

    def test_should_return_false_when_stack_is_not_empty(self):

        # given
        stack = None
        stack = push(stack, 10)

        # when
        result = isEmpty(stack)

        # then
        self.assertFalse(result)

    def test_should_push_element_to_stack(self):

        # given
        stack = None

        # when
        stack = push(stack, 5)
        stack = push(stack, 10)

        # then
        self.assertEqual(stack[0], 10)  # Вершина стека — последний добавленный элемент
        self.assertEqual(stack[1][0], 5)  # Следующий элемент стека — предыдущий элемент

    def test_should_pop_element_from_stack(self):

        # given
        stack = None
        stack = push(stack, 5)
        stack = push(stack, 10)

        # when
        value, stack = pop(stack)

        # then
        self.assertEqual(value, 10)  # Удаленный элемент — вершина стека
        self.assertEqual(stack[0], 5)  # Новая вершина стека после удаления

    def test_should_raise_exception_when_popping_empty_stack(self):

        # given
        stack = None

        # then
        with self.assertRaises(IndexError) as context:
            pop(stack)

        self.assertEqual(str(context.exception), "Pop from empty stack")

    def test_should_display_stack_correctly(self):
        
        # given
        stack = None
        stack = push(stack, 1)
        stack = push(stack, 2)
        stack = push(stack, 3)

        # when
        # Захватываем вывод display() в строку
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        display(stack)

        sys.stdout = sys.__stdout__

        # then
        expected_output = "3 -> 2 -> 1 -> None\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
