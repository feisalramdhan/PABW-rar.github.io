import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello World")

class staticRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("Cars.csv")
		
if __name__ == '__main__':
	app = tornado.web.Application([
		(r"/", basicRequestHandler),
		(r"/7B2_RAR", staticRequestHandler)


	])

	app.listen(8881)
	print("I'm listening on port 8881")
	tornado.ioloop.IOLoop.current().start()