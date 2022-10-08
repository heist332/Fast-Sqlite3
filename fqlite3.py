import random, json, requests, sqlite3, string, os, datetime



class func_tool:
    def __init__(self):
        pass

    def connect_list(self, contents) -> str:
       
        if len(contents) > 1:
            result = ''
            
            for content in list(contents):
                if result == '':
                    result += f'{content} == ?'
                else:
                    result += f' AND {content} == ?'
            
            return result
        
        else:
            
            return f'{list(contents)[0]} == ?'

    def connect_params(self, contents) -> str:
       
        if len(contents) > 1:
            result = ''
            
            for content in list(contents):
                if result == '':
                    result += f'{content} = ?'
                else:
                    result += f', {content} = ?'
            
            return result
        
        else:
            
            return f'{list(contents)[0]} = ?'

class fqlite3:
    '''DB 제어 클래스'''
    def __init__(self):
        self.tool = func_tool()

    def select_one(self, table, field='*', db='main.db', **kwargs) -> bool:
        '''DB SELECT ONE'''
        try:
          
            #SELECT * FROM kwargs[table] WHERE 
            db = db

            con = sqlite3.connect(db)
            cur = con.cursor()
            if len(kwargs) == 0:
                cur.execute(f'SELECT {field} FROM {table};')
            else:
                format_content = self.tool.connect_list(kwargs.keys())
                cur.execute('SELECT * FROM {0} WHERE {1};'.format(table, format_content), tuple(kwargs.values()))
            result = cur.fetchone()
            return result
            
            

        except:
            return False
    
    def select_many(self, table, field='*', db='main.db', **kwargs) -> bool:
        '''DB SELECT ONE'''
        try:
            
            #SELECT * FROM kwargs[table] WHERE 
            db =db

            con = sqlite3.connect(db)
            cur = con.cursor()
            if len(kwargs) == 0:
                cur.execute(f'SELECT {field} FROM {table};')
            else:
                format_content = self.tool.connect_list(kwargs.keys())
                cur.execute('SELECT {0} FROM {1} WHERE {2};'.format(field, table, format_content), tuple(kwargs.values()))
            result = cur.fetchall()
            return result
        except:
            return False

    def insert(self, table, db='main', **kwargs) -> bool:
        '''DB INSERT'''

  

        try:
            db = db

            joining = ', '.join( ['?' for kwarg in range(len(kwargs))] )

            con = sqlite3.connect(db)
            cur = con.cursor()
            cur.execute('INSERT INTO {0} VALUES({1});'.format(table, joining ), tuple(kwargs.values()))
            con.commit()
            con.close()

            return True
        except Exception as e:
            return False
    
    def update(self, table, where, db='main', **kwargs) -> bool:
        '''DB INSERT'''

        #cur.execute(
      #                          'UPDATE users SET money = money + ?, bat = ? WHERE id == ?;', (int(int(par[-1][2]) * 1.95), str(par), str(i[0])))

        try:
            db = db

            params = self.tool.connect_params( kwargs.keys() )
            body = self.tool.connect_list( where.keys() ) 
            
            con = sqlite3.connect(db)
            cur = con.cursor()
            cur.execute('UPDATE {0} SET {1} WHERE {2};'.format(table, params, body ), tuple(kwargs.values()) + tuple(where.values()))
            con.commit()
            con.close()

            return True
        except Exception as e:
            return False
            

        

   