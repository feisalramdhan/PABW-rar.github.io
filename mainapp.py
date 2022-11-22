import tornado.ioloop
import tornado.web
import sqlite3

def _execute(query):
        dbPath = 'C:/server/database1'
        connection = sqlite3.connect(dbPath)
        cursorobj = connection.cursor()
        try:
                cursorobj.execute(query)
                result = cursorobj.fetchall()
                connection.commit()
        except Exception:
                raise
        connection.close()
        return result


class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("Main")

class AddCars(tornado.web.RequestHandler):
    def get(self):
        self.render('form.html')

    def post(self):
        name = self.get_argument("name")
        price = self.get_argument("price")
        query = ''' insert into cars (name, price) values ('%s', %s) ''' %(name, price);
        _execute(query)
        self.render('success.html')

class ShowCars(tornado.web.RequestHandler):
    def get(self):
        query = ''' select * from cars'''
        rows = _execute(query)
        self._processresponse(rows)

    def _processresponse(self,rows):
        self.write("<b>Records</b> <br /><br />")
        for row in rows:
                self.write(str(row[0]) + "      " + str(row[1]) + "     " + str(row[2]) +" <br />" )
application = tornado.web.Application([
    (r"/", Main),
    (r"/create" ,AddCars),
    (r"/show",ShowCars),
],debug=True)

if __name__ == "__main__":
    application.listen(8881)
    print("I'm listening on port 8881")
    tornado.ioloop.IOLoop.instance().start()