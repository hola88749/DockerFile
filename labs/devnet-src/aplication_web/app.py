from flask import Flask, request, render_template
import socket
import getpass
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')

#def hola_mundo():
#       mjs = "hola esta es mi primer app Flask"
#       ipadd = request.remote_addr
#       return mjs+str(ipadd)

def home():
        ipadd = request.remote_addr
        hostname = socket.gethostname ()
        usuario = getpass.getuser()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ruta_script = os.path.abspath(__file__)
        return render_template('./index.html', ip = ipadd, SO = hostname,user=usuario, fecha=fecha,ruta=ruta_script )

if __name__ == '__main__':
        app.run(host='0.0.0.0',port= 5000, threaded=False)
