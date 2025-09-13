from abc import ABC, abstractmethod

from fastapi import UploadFile

from backend.models.diff import Diff


class BaseDiffExtractor(ABC):
    def __init__(self, file1: UploadFile, file2: UploadFile):
        self.file1 = file1
        self.file2 = file2

    @abstractmethod
    def extract(self) -> list[Diff]:
        """
        Extracts the diff between old_code and new_code.

        Args:
            old_code (str): The original version of the code.
            new_code (str): The modified version of the code.
        """
        raise NotImplementedError("Subclasses must implement this method.")
