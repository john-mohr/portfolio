import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;
import java.util.Scanner;
public class ReaderThread implements Runnable
{
	
	private Socket client;
	public ReaderThread(Socket sock) {
		this.client = sock;
	}
	
    public void run() {
    	BufferedReader networkBin = null;	// the reader from the network
    	
		
        try {
            // get the input stream from the socket
			networkBin = new BufferedReader(new InputStreamReader(client.getInputStream()));
			String line;
			System.out.println("connection made");
			
          while((line = networkBin.readLine()) != null) {
        	  Message server_message = Message.constructMessage(line);
        	  Payload server_payload[] = server_message.getPayload();
              String  phrase = server_payload[0].getMessage();
              System.out.println(phrase);
              
              if (EchoClient.userId.equals("0")) {
            	  EchoClient.userId =  String.valueOf(server_payload[0].getUserId());
              }
              
        	  
            // read from the socket
        	  
             /**
              * ok, data has now arrived. Display it in the text area,
              * and resume listening from the socket.
              */
          }
        }
        catch (java.io.IOException ioe) { }
    }
}