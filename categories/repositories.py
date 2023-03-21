import sqlite3
from .models import Category

class CategoryRepository:
    def get_categories(self):
        connection = sqlite3.connect('/home/ethanl/foss-finder-main/FossFinder/db.sqlite3')
        cursor = connection.cursor()
        cursor.execute('SELECT tag_AntiVirus, tag_CodeEditor, tag_Communication, tag_DiskBurner, tag_FileShare, tag_GraphicsEditor, tag_Multimedia, tag_Other, tag_SpreadSheet, tag_wordProcessor FROM SoftwareSubmissionPage_submittedsoftware')
        row = cursor.fetchone()
        category = Category()
        category.antivirus = row[0]
        category.code_editor = row[1]
        category.communication = row[2]
        category.disk_burning_software = row[3]
        category.file_sharing = row[4]
        category.graphical_editing = row[5]
        category.multimedia = row[6]
        category.other = row[7]
        category.spreadsheet_editor = row[8]
        category.word_processor = row[9]
        return category

