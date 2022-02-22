import pyodbc

DB = {'servername': 'voxbi.westus2.cloudapp.azure.com',
      'db': 'VoxBI',
      'uid': 'voxage',
      'pwd': 'vox@ge!K27Zf49',
      'port': 1433}

driver = '/usr/local/lib/libmsodbcsql.17.dylib' # Change this to where FreeTDS installed the driver library!

def connect():
    c = pyodbc.connect(
        driver = driver,
        server = DB['servername'],
        port = DB['port'],
        database = DB['db'],
        uid = DB['uid'],
        pwd = DB['pwd'])
    return c
