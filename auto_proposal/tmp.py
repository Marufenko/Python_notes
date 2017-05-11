import cx_Oracle
import unittest
import HTMLTestRunner3

class tmpTest(unittest.TestCase):
    def setUp(self):
        self.connection = cx_Oracle.connect('oracle/oracle@localhost:1521/XE')

    def test_tmp1(self):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute('select * from tmp1')

        self.assertFalse(cursor.fetchall())

    def test_tmp2(self):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute('select 1 from dual')

        self.assertTrue(cursor.fetchall())

    def test_tmp3(self):
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute('select 1 from dual')

        self.assertFalse(cursor.fetchall())

    def tearDown(self):
        self.connection.close()

# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(tmpTest)
unittest.TextTestRunner(verbosity=2).run(suite)

outfile = open("D:/report.html", "w")
runner = HTMLTestRunner3.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output by me :).'
                )

runner.run(suite)
