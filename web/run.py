from marketplace import app
import os


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000',debug = os.environ.get('DEBUG') == '1') 
    # to pass env variable to a docker container
    # check if the DEBUG env variable is equal to 1 then it will return True
    # docker run -p 5000:5000 -e DEBUG=1 name //debug = True when we are in dev 
    # docker run -p 5000:5000 name //debug = False in prod mode