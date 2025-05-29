import sys
import os
from books_recommender.exception.exception_handler import AppException
from books_recommender.logger.log import logging

print("\n--- Diagnostic: sys.path from app.py ---")
for i, p in enumerate(sys.path):
    print(f"{i}: {p}")
print("----------------------------------------\n")

print("\n--- Diagnostic: Current Working Directory ---")
print(f"CWD: {os.getcwd()}")
print("-------------------------------------------\n")

# Original problematic import

try:
    a = 3/0
except Exception as e:
    logging.info()
    raise AppException(e,sys) from e
