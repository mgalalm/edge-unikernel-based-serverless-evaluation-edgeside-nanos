#!/bin/python
import subprocess
import os
import redis
import uuid
import flask
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
app = flask.Flask(__name__)
@app.route('/<unikernel_name>', methods=['GET'])
def invoke(unikernel_name="helloworld"):

    activation_id = uuid.uuid1()
    logging.info(f"Activation id: {activation_id}")


    # where elf lives
    os.chdir("/home/pi/src")

    proc = subprocess.Popen(f"ops run {unikernel_name} -i {activation_id}", shell=True, stdout=subprocess.PIPE)
    print(proc.pid)
    proc.wait()
    result = r.hgetall(str(activation_id))
    result['activationId'] = activation_id
    logging.info(f"Result: {result}")
    return result

# def main():
#     invoke("helloworld")

# if __name__ == "__main__":
#     main()
app.run(host='0.0.0.0', port=8080)
