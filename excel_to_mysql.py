"""
功能：将Excel数据导入到MySQL数据库
"""
import xlrd
import mysql_python # 导入之前封装的mysql操作类

# Open the workbook and define the worksheet
book = xlrd.open_workbook("pytest.xlsx")
sheet = book.sheet_by_name("source")
mydb=mysql_python.MyDB()


# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
for r in range(1, sheet.nrows):
      no      = sheet.cell(r,0).value
      name = sheet.cell(r,1).value
      values = (no,name)
      query1= "INSERT INTO stu (no,name) VALUES "+ str(values)
      #下面这句sql语句name字段不包含单引号或者双引号，插入数据会失败
      query = "INSERT INTO stu (no,name) VALUES (%s,%s)" %values

      # 执行sql语句

      mydb.execute_update_insert(query1)

mydb.close()

# 打印结果
print("")
print("Done! ")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("我刚导入了 "+columns + "列"+rows +"行数据到MySQL!")
