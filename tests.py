# Need to run the following:
# get_files_info("calculator", ".")
# Output needs to be similar to:
# Result for current directory:
# - main.py: file_size=576 bytes, is_dir=False
# - tests.py: file_size=1343 bytes, is_dir=False
# - pkg: file_size=92 bytes, is_dir=True
from functions.get_files_info import get_files_info

get_files_info("calculator", ".")

print("=" * 60)
get_files_info("calculator", "pkg")

print("=" * 60)
get_files_info("calculator", "/bin")

print("=" * 60)
get_files_info("calculator", "../")
