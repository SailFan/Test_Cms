import sqlite3
import unittest
# from ddt import ddt, data, unpack
from ddt import ddt,data, unpack

def getUser():
    conn = sqlite3.connect("D:\pycode\Test_Cms\dao\CMS.db")
    c = conn.cursor()
    sql = """ SELECT ID, USERNAME, PASSWORD, CASENAME FROM cms_login"""
    results = c.execute(sql)
    all_user = results.fetchall()
    return all_user

if __name__ == '__main__':
    for user in getUser():
        print(user)