import pymysql
import datetime
now = datetime.datetime.now()

from database import *
con=database.connection()

curs=con.cursor()
class Medicine:
    def __init__(self,mid):
        self.med_id=mid
        curs.execute("""Select qty from medicine where mid=%s""",(self.med_id))
        result=curs.fetchall()
        self.qty_avail=result[0][0]
        stmt="""Select exp_date from medicine where mid=%s"""
        curs.execute(stmt,(self.med_id))
        result=curs.fetchall()
        self.med_expdate=datetime.datetime.strftime(result[0][0],"%Y-%M-%D")
        stmt="""Select price from medicine where mid=%s"""
        curs.execute(stmt,(self.med_id))
        result=curs.fetchall()
        self.price=result[0][0]


    def checkExpiry(self):

        if(self.med_expdate>now.strftime("%Y-%M-%D")):
            return True
        else:
            return False

    def checkAvail(self):
        if(self.qty_avail>0):
            return True
        else:
            False

    def updateQty(self,qty):
        stmt="""Update medicine set qty=%s where mid=%s"""
        curs.execute(stmt,(self.qty_avail+qty,self.med_id))
        con.commit()

    def updateExp(self,dt):
        stmt="""Update medicine set exp_date=%s where mid=%s"""
        curs.execute(stmt,(dt,self.med_id))
        con.commit()
