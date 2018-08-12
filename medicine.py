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



    def checkExpiry(self):

        if(self.med_expdate>now.strftime("%Y-%M-%D")):
            return False
        else:
            self.qty_avail=0
            return True

    def checkAvail(self):
        if(self.qty_avail>0):
            return True
        else:
            False

    def updateQty(self,qty):
        bool=self.checkExpiry()
        if(bool==True):
            print("Old medicines of this id have got expired.Therefore discarding the old medicines from the stock  and updating it with new one")
        stmt="""Update medicine set qty=%s where mid=%s"""
        curs.execute(stmt,(self.qty_avail+qty,self.med_id))
        con.commit()

    def updateExp(self,dt):
        stmt="""Update medicine set exp_date=%s where mid=%s"""
        curs.execute(stmt,(dt,self.med_id))
        con.commit()
