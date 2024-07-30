from runner import Runner
import unittest


class TestRunner(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner('test')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        for i in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100, 'Test Runner.run() - failed!')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for i in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50, 'Test Runner.walk() - failed!')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_obj2 = Runner('test2')
        for i in range(10):
            self.runner.walk()
            test_obj2.run()
        self.assertNotEqual(self.runner.distance, test_obj2.distance,
                            'Combined test Runner.walk() & Runner.run()- failed!')


if __name__ == '__main__':
    unittest.main()
