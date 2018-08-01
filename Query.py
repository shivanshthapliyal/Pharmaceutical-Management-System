"""CREATE TABLE customer (cid int(11) NOT NULL,cname varchar(20) DEFAULT NULL,phone varchar(10) DEFAULT NULL,email varchar(30) NOT NULL ,address varchar(20) DEFAULT NULL,password varchar(20) NOT null,PRIMARY KEY (cid))"""

"""CREATE TABLE manufacturer (manid int(11) NOT NULL,mname varchar(20) DEFAULT NULL,PRIMARY KEY (manid))"""

"""CREATE TABLE medicine (
  mid int(11) NOT NULL,
  mname varchar(20) DEFAULT NULL,
  price int(11) DEFAULT NULL,
  qty int(11) DEFAULT NULL,
  manid int(11) DEFAULT NULL,
  exp_date date NOT NULL,
  PRIMARY KEY (mid),
  KEY manid (manid),
  CONSTRAINT medicine_ibfk_1 FOREIGN KEY (manid) REFERENCES manufacturer (manid))"""

"""CREATE TABLE orders (
  oid int(11) NOT NULL,
  cid int(11) NOT NULL,
  mid int(11) NOT NULL,
  status varchar(20) DEFAULT 'pending',
  dateoforder date NOT NULL DEFAULT NULL,
  PRIMARY KEY (oid,mid),
  KEY cid (cid),
  KEY mid (mid),
  CHECK (status in('pending','completed')),
  CONSTRAINT orders_ibfk_1 FOREIGN KEY (cid) REFERENCES customer (cid),
  CONSTRAINT orders_ibfk_2 FOREIGN KEY (mid) REFERENCES medicine (mid))"""
  
"""INSERT INTO customer VALUES (1023,'Shishir Goyal','1452365987','sgoyal@gmail.com','sdfafas','qwert'),(1024,'Shivansh Thapliyal','3698452353','sthap@yahoo.com','tyuityij','asdf'),(1025,'Souradeep Banerjee','2103968486','sbanerjee@gmail.com','fdhfgcn','zxcv'),(1026,'Siddharth Sharma','3239465167','ssharma@yahoo.com','vbmvcbn','!@#$'),(1027,'Shivam Sharma','9876513654','ssharma12@yahoo.com','asdad','Abc123')"""

"""INSERT INTO manufacturer VALUES (245,'Wolter Kluwer'),(1103,'Cerner'),(3569,'Reddys'),(4587,'Truven'),(5463,'Reiden Global'),(6945,'ashp')"""

"""INSERT INTO medicine VALUES (256,'Calpol',25,100,5463,'2019-02-23'),(1450,'Hetrazein',36,200,3569,'2019-01-12'),(2213,'Acetaminophen.',1200,150,245,'2019-04-14'),(2598,'Adderall.',2050,100,1103,'2018-08-15'),(3219,'Apex',25,250,1103,'2018-12-12'),(6544,'Aciloc',10,500,4587,'2019-05-15'),(7451,'Atorvastatin.',50,600,6945,'2019-05-15'),(9870,'Morphine',50,236,6945,'2019-03-11')"""
