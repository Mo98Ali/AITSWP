from __init__ import app
import ssl

ssl_cert = "./Verschlusselung/SSL Data/self-signed-ca-cert.crt"
ssl_key = "./Verschlusselung/SSL Data/private-ca.key"

cryp = ssl.SSLContext(ssl.PROTOCOL_TLS)
cryp.options |= ssl.OP_NO_TLSv1| ssl.OP_NO_TLSv1_1
cryp.load_cert_chain(ssl_cert,ssl_key)

if __name__ == "__main__":
    app.run(debug = True,ssl_context = cryp, host='0.0.0.0',port=5001)

    