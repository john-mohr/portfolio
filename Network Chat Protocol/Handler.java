import java.io.*;
import java.util.*;
import java.util.ArrayList;
import java.net.*;
public class Handler 
{
	public static final int BUFFER_SIZE = 256;
	
	/**
	 * this method is invoked by a separate thread
	 * for output stream use data output stream and can write bites
	 */
	public void process(Socket client, ArrayList<DataOutputStream> outputStreams, Dictionary userList) throws java.io.IOException {
		BufferedReader fromClient = null;
		DataOutputStream toClient = null;
		Message messageFinal = null;
		Dictionary user_list = null;
		
		try {
			/**
			 * get the input and output streams associated with the socket.
			 */
			
			fromClient = new BufferedReader(new InputStreamReader(client.getInputStream()));
			toClient = new DataOutputStream(client.getOutputStream());
			outputStreams.add(toClient);
			user_list = new Hashtable();
			user_list.put(0,"server");
			String message;
			/** use the message class and call construct message on the fromClient then can use the methods in the 
			 * payload and message class to get control types from the message object then according to that result 
			 * send the message with the writeBytes method on toClient */
			/** continually loop until the client closes the connection */
			DataOutputStream clients = null;
			while ( (message = fromClient.readLine()) != null) {
				messageFinal = EchoClient.constructMessage(message);
				
				
				/**has to change to include the full message including the control code so that 
				 * the server can send it all too all clients*/
				if(messageFinal.getControlCode() == 1) {
					Payload[] payload = messageFinal.getPayload();
					user_list.put(user_list.size() + 1, payload[0].getMessage());
					String response = "0,1," + String.valueOf(user_list.size())
						+ "," + payload[0].getLength() + "," + payload[0].getMessage() + "\r\n";
					
					for(int i = 0; i < outputStreams.size(); i++) {
						clients = outputStreams.get(i);
						clients.writeBytes(response);
						clients.flush();
					}
				}
				
				if(messageFinal.getControlCode() == 255) {
					
					Payload[] payload = messageFinal.getPayload();
					String phrase = user_list.get(payload[0].getUserId())+ ": "+ payload[0].getMessage();
					String response = "255,1," + String.valueOf(payload[0].getUserId())
						+ "," + String.valueOf(phrase.length()) + "," + phrase + "\r\n";
					
					for(int i = 0; i < outputStreams.size(); i++) {
						clients = outputStreams.get(i);
						clients.writeBytes(response);
						clients.flush();
					}
				}
				/**
				 * "flushing" the stream writes the contents of the data to the network.
				 */
				
			}
  		}
		catch (IOException ioe) {
			System.err.println(ioe.getStackTrace());
		}
		finally {
			// close streams and socket
			if (fromClient != null)
				fromClient.close();
			if (toClient != null)
				toClient.close();
		}
	}
}