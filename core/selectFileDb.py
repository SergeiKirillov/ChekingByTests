from testManager import TestManager

manager = TestManager()
#print(manager.get_tests_names())

tests = manager.get_tests_names()
for i, test in enumerate(tests, 1):
    print(f"{i}. {test}")
choice = int(input("> "))
selected_test = tests[choice - 1]

selectDB = manager.load_test(selected_test)
print(selectDB["title"])
