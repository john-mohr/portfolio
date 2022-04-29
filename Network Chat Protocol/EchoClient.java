/**
 * An echo client. The client enters data to the server, and the
 * server echoes the data back to the client.
 *
 * @author - Greg Gagne
 */

import java.net.*;
import java.io.*;
import java.util.Scanner;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
public class EchoClient
{
	public static final int DEFAULT_PORT = 4200;
	private static final Executor exec = Executors.newCachedThreadPool();
	public static String userId = "0";
	public static Message constructMessage(String contents) {
        Scanner message = new Scanner(contents).useDelimiter(",");

        int controlCode = message.nextInt();
        int quantity = message.nextInt();

        Message m = new Message(controlCode, quantity);

        Payload payload;

        for (int i = 0; i < quantity; i++) {
            int userID = message.nextInt();
            int length = message.nextInt();
            String  phrase = message.next();

            payload = new Payload(userID, length, phrase);
            m.addPayload(payload);
        }

        return m;
    }


	
	public static void main(String[] args) throws IOException {
		if (args.length != 1) {
			System.err.println("Usage: java EchoClient <echo server>");
			System.exit(0);
		}
		
		
		DataOutputStream networkPout = null;		// the writer to the network
		Scanner localBin = null;		// the reader from the local keyboard
		Socket sock = null;			// the socket
				
		
		try {
			String join_message = "1,1,0,2,Katr\n";
			
			
			String leave_message = "2,1,0,2,JD\r\n";
			
			localBin = new Scanner(System.in);
			boolean done = false;
			
			System.out.println("Enter (;join) to join the chat room.");
			System.out.println("Enter (;leave) to leave the chat room.");
			
			while(done != true) {
				String line = localBin.nextLine();
				
				if(line.equals(";join")) {
					sock = new Socket(args[0], DEFAULT_PORT);
					networkPout = new DataOutputStream(sock.getOutputStream());
					networkPout.writeBytes(join_message);
					networkPout.flush();
					Runnable task = new ReaderThread(sock);
					exec.execute(task);
				}
				else if(line.equals(";leave")) {
					networkPout.writeBytes(leave_message);
					networkPout.flush();
					done = true;
				}
				else {
					String send_message = "255,1," + userId + "," + line.length() + "," + line + "\r\n";
					
					networkPout.writeBytes(send_message);
					networkPout.flush();
				}
			}
			
			sock.close();
			networkPout.close();
			localBin.close();
			
		}
		catch (IOException ioe) {
			System.err.println(ioe);
		}
		finally {
			if (localBin != null)
				localBin.close();
			if (sock != null)
				sock.close();
		}
	}
}
