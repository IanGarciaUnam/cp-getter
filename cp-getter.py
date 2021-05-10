import xlrd, sys

def get_data_from_xlsx(file_path:str,column:int):
	cp_list:list=[]
	loc= file_path
	wb=xlrd.open_workbook(loc)
	sheet=wb.sheet_by_index(0)
	x=5
	for x in range(sheet.nrows):
		try:
			cp_list.append(int(sheet.cell_value(x,column)))
		except ValueError:
			continue

	return cp_list

def write_txt(cps: list):
    content=""

    for cp in cps:
        cp_str = str(cp)
        cp_str = cp_str.rjust(5, "0")
        content += cp_str + "\n"

    textfile = open("file.txt","w")
    textfile.write(content)
    textfile.close()


if __name__=="__main__":
	file_path=sys.argv[1]
	write_txt(get_data_from_xlsx(file_path, 0))
