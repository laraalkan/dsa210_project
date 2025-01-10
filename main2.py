from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
file_name = "pinterest.html"
with open(file_name, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
