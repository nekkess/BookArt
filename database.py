import os
import string
import pandas as pd


class Database:
    def __init__(self, csv_file: str):
        #load from csv
        self.full_df = pd.read_csv(csv_file)

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

    def search_column(self, text: str, top_k: int, column: str, 
                      df: pd.DataFrame, threshold: float=0.5) -> pd.DataFrame:
        """
        Returns slice of df with column matching some text
        """
        matches = df[column].apply(lambda x: self.match_strings(text, x))
        if top_k > 0:
            indexes = matches.sort_values(ascending=False).index[:top_k]
        else:
            indexes = matches[matches > threshold].index
        sliced_df = df.loc[indexes]
        return sliced_df
    
    def get_url(self, author: str):
        return self.search_column(author, -5, 'name', self.full_df, threshold= 0.3)
        # return self.search_column(title, 1, 'TITLE', sliced_df)['URL'].values[0]
        
        

if __name__ == "__main__":
    db = Database(os.path.join("assets", "artists.csv"))
    print(db.get_url('Rene Magritte'))

   

        