'''
create table tmp1 (
ID NUMBER(20) PRIMARY KEY,
PORTFOLIO number(20),
partner_portfolio number(20)
);

insert into oracle.tmp1 values (1, 100001, 100000);
insert into oracle.tmp1 values (2, 100001, 100001);
commit;

select * from oracle.tmp1;
'''

import cx_Oracle
from pprint import pprint

connection = cx_Oracle.connect('oracle/oracle@localhost:1521/XE')

cursor = connection.cursor()
cursor.execute('select * from oracle.tmp1')

# for row in cursor:
#     print(row)
# connection.close()

pprint(cursor.fetchall())

connection.close()