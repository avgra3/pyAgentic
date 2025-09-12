from functions.get_files_info import get_file_content

print(get_file_content("calculator", "lorem.txt"))


results = [
    get_file_content("calculator", "main.py"),
    get_file_content("calculator", "pkg/calculator.py"),
    get_file_content("calculator", "/bin/cat"),
    get_file_content("calculator", "pkg/does_not_exist.py"),
]

for i, result in enumerate(results):
    if i > 0:
        print("\n", "=+" * 40)
    print(result)
