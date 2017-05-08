import MySQLdb
import sys
import datetime
def getValues(fid):
    x=fid
    db=MySQLdb.connect(host="gndb2.cff0wq1cnhui.us-west-2.rds.amazonaws.com",port=3306,user="*******",passwd="*****",db="*****")
    co=db.cursor()
    co.execute("SELECT dfruit,dcalories,dprotein,dfat,dsugars from dfood WHERE dfid=%d" %(x))
    data=co.fetchall()
    co.close()
    #for row in data:
        #print(row)
    db.close()
    return data

def setConsumedValues(rfid,fid,c1,c2,c3,c4):
    rfid1=rfid
    s=datetime.date.today()
    fid1=fid
    db=MySQLdb.connect(host="gndb2.cff0wq1cnhui.us-west-2.rds.amazonaws.com",port=3306,user="******",passwd="******",db="Sample")
    co=db.cursor()
    co.execute("Insert into dintake (duid,didate,dfid,dicalories,diprotein,difat,disugars) values ('%s','%s','%d','%s','%s','%s','%s')" %(rfid1,s,fid1,str(c1),str(c2),str(c3),str(c4)))
    #co.execute("Insert into dintake(duid,didate,dfid,dicalories,diprotein,difat,disugars) values ("1111","%s",'%d','%s','%s','%s','%s')" %(x,str(c1),str(c2),str(c3),str(c4)))	 	
    data=co.fetchall()
    cc='commit'
    co.execute('%s' %(cc))
    co.close()
    #for row in data:
     #   print(row)
    db.close()
