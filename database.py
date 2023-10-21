import os
import string
import pandas as pd


class Database:
    def __init__(self, excel_filepath: str):
        self.df = pd.read_excel(excel_filepath)

    @staticmethod
    def match_strings(text1: str, text2: str) -> float:
        """
        Example: ('VAN GOGH', 'vincent van gogh') -> True
        """
        list1 = text1.lower().split()
        list1 = [word.strip(string.punctuation) for word in list1]
        list2 = text2.lower().split()
        list2 = [word.strip(string.punctuation) for word in list2]

        common = set(list1).intersection(set(list2))
        percentage = 2 * len(common) / (len(list1) + len(list2))
        return percentage

    def find_author(self, text: str, top_k: int):
        self.df['AUTHOR'].apply(lambda x: self.match_strings(text, x))

        
if __name__ == "__main__":
    db = Database(os.path.join("assets", "catalog.xlsx"))

        