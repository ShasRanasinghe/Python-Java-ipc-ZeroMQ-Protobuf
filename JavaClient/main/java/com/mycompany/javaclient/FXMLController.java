package com.mycompany.javaclient;

import TORCS_Sensors.Sensor_Message;
import TORCS_Sensors.Sensor_Message.Sensors;
import com.google.protobuf.InvalidProtocolBufferException;
import java.net.URL;
import java.util.Arrays;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import org.zeromq.ZMQ;
import org.zeromq.ZMQ.Context;
import org.zeromq.ZMQ.Socket;

public class FXMLController implements Initializable {

    @FXML
    private Label label;

    //Constants
    private static final String SUBSCRIBER_PORT = "tcp://localhost:5555";
    private static final String SYNC_PORT = "tcp://localhost:5556";
    private static final String HANDSHAKE_INIT = "Init";
    private static final String HANDSHAKE_ACK = "SyncAck";

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        Context context = ZMQ.context(1);

        //Connect our subscriber socket with a PUB/SUB pair
        Socket subscriber = context.socket(ZMQ.SUB);
        subscriber.setRcvHWM(0);
        subscriber.connect(SUBSCRIBER_PORT);
        //subscribe to empty string to get all messages
        subscriber.subscribe("".getBytes());

        //Create ynchronize port with a REQ/REP pair
        Socket sync_socket = context.socket(ZMQ.REQ);
        sync_socket.connect(SYNC_PORT);

        //wait for handshake
        System.out.println("Awaiting Handshake");
        while (true) {
            String recvString = subscriber.recvStr(0);
            if (recvString.equals(HANDSHAKE_INIT)) {
                System.out.println("Acknowledging Handshake");
                sync_socket.send(HANDSHAKE_ACK);
                break;
            }
        }

        //Get updates from publisher
        System.out.println("Receiving Updates");
        Sensors message;
        while (true) {
            byte[] update = subscriber.recv();

            if (Arrays.equals(update, "END".getBytes())) {
                System.out.println("Ending updates");
                break;
            }

            try {
                message = Sensor_Message.Sensors.parseFrom(update);
                System.out.println(message.toString());
            } catch (InvalidProtocolBufferException ex) {
                System.out.println("Well that was not supposed to happen");
            }
        }

        subscriber.close();
        sync_socket.close();
        context.term();
    }

    @FXML
    private void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
        label.setText("Hello World!");
    }
}
