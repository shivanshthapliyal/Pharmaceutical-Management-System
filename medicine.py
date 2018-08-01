import pymysql
import datetime
now = datetime.datetime.now()

con = pymysql.connect("localhost","root","root","pharmacy" )
curs=con.cursor()
class Medicine:

    def __init__(self,mid):
        med_id=mid
        stmt="""Select qty from medicine where mid=:1"""
        curs.execute(stmt,(med_id))
        result=curs.fetchall()
        for i in result:
            for j in i:
                qty_avail=j
        stmt="""Select exp_date from medicine where mid=:1"""
        curs.execute(stmt,(med_id))
        result=curs.fetchall()
        for i in result:
            for j in i:
                med_expdate=datetime.datetime.strftime(j,"%Y-%M-%D")
        stmt="""Select price from medicine where mid=:1"""
        curs.execute(stmt,(med_id))
        result=curs.fetchall()
        for i in result:
            for j in i:
                price=j


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
        stmt="""Update medicine set qty=:1 where mid=:2"""
        curs.execute(stmt,(self.qty_avail+qty,self.med_id))
        con.commit()

    def updateExp(self,dt):
        stmt="""Update medicine set exp_date=:1 where mid=:2"""
        curs.execute(stmt,(dt,self.med_id))
        con.commit()
