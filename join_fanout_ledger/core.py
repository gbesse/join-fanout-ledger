import sqlite3
from .common import integer,unique_ids

def key(x):
 if x is not None and (not isinstance(x,str)or len(x)>200):raise ValueError('key')
 return x
def run(data):
 left=data['left'];right=data['right'];unique_ids(left);unique_ids(right)
 if len(left)>1000 or len(right)>1000:raise ValueError('rows')
 L=[(r['id'],key(r.get('key')),integer(r['amount_cents'],-1000000000,1000000000))for r in left];R=[(r['id'],key(r.get('key')))for r in right];c=sqlite3.connect(':memory:')
 try:
  c.executescript('CREATE TABLE l(id TEXT PRIMARY KEY,k TEXT,amount INTEGER);CREATE TABLE r(id TEXT PRIMARY KEY,k TEXT);');c.executemany('INSERT INTO l VALUES (?,?,?)',L);c.executemany('INSERT INTO r VALUES (?,?)',R)
  rows=[{'id':id,'key':k,'original_cents':amount,'matched_right_rows':count,'joined_contribution_cents':amount*max(1,count),'extra_cents':amount*(max(1,count)-1)}for id,k,amount,count in c.execute('SELECT l.id,l.k,l.amount,COUNT(r.id) FROM l LEFT JOIN r ON l.k=r.k GROUP BY l.id ORDER BY l.id')];baseline=c.execute('SELECT COALESCE(SUM(amount),0)FROM l').fetchone()[0];joined=c.execute('SELECT COALESCE(SUM(l.amount),0)FROM l LEFT JOIN r ON l.k=r.k').fetchone()[0]
  return {'left_total_cents':baseline,'left_join_total_cents':joined,'fanout_delta_cents':joined-baseline,'rows':rows,'model':'native_sqlite_left_equality_join_one_declared_amount_unit','sqlite_version':sqlite3.sqlite_version}
 finally:c.close()
