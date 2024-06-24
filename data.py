import os
import pandas as pd


class Data:

    def __init__(self) -> None:
        os.chdir(r'C:\Users\vasuj\Documents\Data collection (dboard)')
        self.df = pd.read_csv('cleaned_job_data.csv')


