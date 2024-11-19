# Script to convert generated csv files to xlsx format
# https://stackoverflow.com/a/17684679/11435681

import csv
import glob
import os

from xlsxwriter.workbook import Workbook

for csvfile in glob.glob(os.path.join(".", "output/*.csv")):
    workbook = Workbook(csvfile[:-4] + ".xlsx")
    worksheet = workbook.add_worksheet()
    with open(csvfile, "rt", encoding="utf8") as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
