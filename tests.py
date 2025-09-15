# from functions.get_files_info import get_file_content
from functions.write_file import write_file

results = [
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

for result in results:
    print(result)


# Goes with get_file_content
# print(get_file_content("calculator", "lorem.txt"))
#
#
# results = [
#     get_file_content("calculator", "main.py"),
#     get_file_content("calculator", "pkg/calculator.py"),
#     get_file_content("calculator", "/bin/cat"),
#     get_file_content("calculator", "pkg/does_not_exist.py"),
# ]
#
# for i, result in enumerate(results):
#     if i > 0:
#         print("\n", "=+" * 40)
#     print(result)
