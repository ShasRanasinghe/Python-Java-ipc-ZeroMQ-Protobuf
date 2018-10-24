#
#  Synchronized publisher
#
import zmq
import proto_schema_pb2
from google.protobuf.internal import encoder
import random


publisher_port = 'tcp://*:5555'
sync_port = 'tcp://*:5556'
handshake_init = 'Init'
poll_timeout = 100


def get_message():
    message = proto_schema_pb2.Sensors()
    message.angle = random.uniform(-1, 1)
    message.currentLabTime = random.uniform(-1, 1)
    message.damage = random.uniform(-1, 1)
    message.distanceFromStart = random.uniform(-1, 1)
    message.totalDistanceFromStart = random.uniform(-1, 1)
    message.distanceRaced = random.uniform(-1, 1)
    message.fuel = random.uniform(-1, 1)
    message.gear = random.uniform(-1, 1)
    message.lastLapTime = random.uniform(-1, 1)
    message.opponents = random.uniform(-1, 1)
    message.racePos = random.uniform(-1, 1)
    message.rpm = random.uniform(-1, 1)
    message.speedX = random.uniform(-1, 1)
    message.speedY = random.uniform(-1, 1)
    message.speedZ = random.uniform(-1, 1)
    message.track = random.uniform(-1, 1)
    message.trackPosition = random.uniform(-1, 1)
    message.wheelSpinVelocity = random.uniform(-1, 1)
    message.z = random.uniform(-1, 1)
    message.focus = random.uniform(-1, 1)
    return message.SerializeToString()


def main():
    context = zmq.Context()

    # Socket to talk to clients
    publisher_socket = context.socket(zmq.PUB)
    # set SNDHWM, so we don't drop messages for slow subscribers
    publisher_socket.sndhwm = 1100000
    publisher_socket.bind(publisher_port)

    # Socket to receive signals
    sync_socket = context.socket(zmq.REP)
    sync_socket.bind(sync_port)

    # Send initialize messages through publisher
    print('Attempting Handshake')
    while True:
        publisher_socket.send_string(handshake_init)
        ack = sync_socket.poll(poll_timeout)
        if ack:
            print('Handshake Accepted')
            break

    # Now broadcast exactly 10 updates followed by END
    print('Sending Updates')
    for i in range(10):
        sent = publisher_socket.send(get_message())
        if sent == 0:
            print('Send Failed')

    publisher_socket.send(b'END')


if __name__ == '__main__':
    main()