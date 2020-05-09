import requests
import json
import time
import sqlite3

def change_all_db(text):
    conn1 = sqlite3.connect('person.db')
    conn1.execute("INSERT INTO status VALUES( ?)",(text,))
    conn1.commit()
    conn1.close()

def get_papers():
	con = sqlite3.connect('person.db')
	mat=con.execute('SELECT * FROM papers')
	arr={}
	for i in mat:
		arr[i[0]]=i[1]
	return arr

def refresh_papers():
	url1='https://trustgaruda.firebaseio.com/.json'
	auth_key = 'VyiSDTWZvNCytmG9tL3mZ8fN1lISeuT68532Y6xP'
	try:
		r1=requests.get(url1 + '?auth=' + auth_key)
		k=r1.json()
		con=sqlite3.connect('person.db')
		con.execute('delete from papers')
		for i in k.keys():
			con.execute('insert into papers values(?,?)',(i,k[i]))
		con.commit()
		con.close()
		return True
	except Exception as e:
		print(str(e))
		return 0

def do_base(real_date,taken_date,amount,amount_give,intrest,six,no_of_months):
    tim=time.strftime('%T')
    date=time.strftime('%d-%m-%Y')
    bundle=tim+'$'+date+'$'+real_date+'$'+taken_date+'$'+str(amount)+'$'+str(amount_give)+'$'+str(intrest)+'$'+str(six)+'$'+str(no_of_months)+'\n'
    change_all_db(bundle)

def set_firebase(path,data):
	url1='https://test-bfdc9.firebaseio.com/'+path+'/.json'
	if path=='':
		url1='https://test-bfdc9.firebaseio.com/.json'
	r = json.dumps(data)
	to_database = json.loads(r)
	requests.patch(url = url1 , json = to_database)


def get_db():
    conn=sqlite3.connect("person.db")
    a=conn.execute("SELECT * from status")
    db=[]
    for i in a:
        db.append(i[0])
    print(db)
    conn.close()
    return db

def delete_db():
    conn=sqlite3.connect("person.db")
    a=conn.execute("DELETE FROM status")
    conn.commit()
    conn.close()

def do_all(uid,real_date,taken_date,amount,amount_give,intrest,six,no_of_months):
	do_base(real_date,taken_date,amount,amount_give,intrest,six,no_of_months)
	k=get_db()
	kz=''
	for i in k:
		kz+=i
	print('-'*100)
	print(uid)
	tim=time.strftime('%T')
	date=time.strftime('%d-%m-%Y')
	try:
		set_firebase(uid,{tim+'@'+date:kz})
		delete_db()
	except Exception as e:
		pass

#set_firebase('path',{'datta':'guru'})