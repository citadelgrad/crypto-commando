from cement.core import foundation

app = foundation.TestApp('helloworld')
try:
    app.setup()
    app.run()
    print('Hello World')
finally:
    app.close()