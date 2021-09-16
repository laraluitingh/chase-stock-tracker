import psycopg2

def sql_select(query,params):
  conn = psycopg2.connect("dbname=chase-stocks")
  cur = conn.cursor()
  cur.execute(query, params)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results

def sql_write(query, params):
  conn = psycopg2.connect("dbname=chase-stocks")
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  conn.close()

def sql_select_without_params(query):
  conn = psycopg2.connect("dbname=chase-stocks")
  cur = conn.cursor()
  cur.execute(query)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results