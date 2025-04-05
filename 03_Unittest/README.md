## 🧪 **Unit Testing with unittest in Python**

This project uses Python's built-in unittest framework to write and run tests for the application.
## 🧪 Writing Tests
Create a new test file under the tests/ directory, and name it starting with test_.

Here’s a basic example:
```
import unittest
from app.your_module import add

class TestYourModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 2), 5)

if __name__ == '__main__':
    unittest.main()

```
### **Key Concepts**

Test fixture — a block of code that implements actions that should be executed before or after tests

Test Case — a single test unit that stores checks for specific functionality

Test Suite — a set of tests or test suites with the same object of testing

Test Runner — a component that controls tests execution and provides results to the user in a human-readable format

### **Unittest Features**

#### Test Fixture

A test fixture represents the preparation needed to perform one or more tests and any associated cleanup actions. For such purposes, the setUp, setUpClass, teardown, and tearDownClass methods of the unittest.TestCase class can be used. These help implement pre- and post-conditions.

#### tearDown()

Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than AssertionError or SkipTest, raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the setUp() succeeds, regardless of the outcome of the test method. The default implementation does nothing.

tearDown() and tearDownClass() methods will only be called if the setUp() and setUpClass() succeed.

#### Test Suite

In the unittest framework, a test suite is a way of grouping test cases.

A test suite is created as an instance of the unittest.TestSuite class, and then you need to add the previously implemented test cases using the addTest() method.

#### Skip Tests

Checks in a test case can be skipped one by one, or you can skip the whole test case. In the first case, the engineer can use either the decorator @unittest.skip(reason_text) if they want to skip the test regardless or @unittest.skipUnless(condition_function(), reason_text) if they want to skip the test if condition_function returns False.

The decorator @unittest.skipif(condition, reason) is used to skip the test if the condition is True.

#### Expected Test Failures

Sometimes, tests should fail to show whether an application works correctly. For example, if you write a test to check for the ability to log in with an incorrect login and password, it will fail, and such behavior will be correct. But how do you explain this to unittest? To do this, such tests should be decorated with @unittest.expectedFailure*.


## **▶️ Running Tests**

Execute tests via the directory where test modules are stored
```
python -m unittest discover <test_directory>
```
Execute tests via the module name
```
python -m unittest <test_module1> <test_module2>
```
Execute tests via the testcase/testsuite name
```
python -m unittest <test_module.TestCaseClassName/TestSuiteName>
```
Execute tests via the method name
```
python -m unittest <test_module.TestCaseClassName.test_method_name>
```
Execute tests using Test Runner - You may call the unittest test runner directly via unittest.main() method

## 🛠️ **Common Assertions**
```
assertEqual(a, b)

```

See the full list in the official documentation[official documentation](https://docs.python.org/3/library/unittest.html#assert-methods).

## ✅ **Best Practices**

Name your test files with the test_ prefix.

Group related tests in classes that inherit from unittest.TestCase.

Use setup/teardown methods (setUp, tearDown) if needed.

Keep tests isolated and independent.