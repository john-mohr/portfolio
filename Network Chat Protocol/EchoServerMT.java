/**
 * An echo server listening on port 6007. 
 * This server reads from the client
 * and echoes back the result. 
 *
 * This services each request in a separate thread.
 *
 * This conforms to RFC 862 for echo servers.
 *
 * @author - Greg Gagne.
 */

import java.net.*;
import java.util.*;
import java.io.*;
import java.util.concurrent.*;
import java.util.ArrayList;
public class  EchoServerMT
{
	public static final int DEFAULT_PORT = 4200;

    // construct a thread pool for concurrency	
	private static final Executor exec = Executors.newCachedThreadPool();
	
	public static void main(String[] args) throws IOException {
		ServerSocket sock = null;
		
		try {
			// establish the socket
			sock = new ServerSocket(DEFAULT_PORT);
			ArrayList<DataOutputStream> outputStreams = new ArrayList<DataOutputStream>();
			Dictionary userList = new Hashtable();
			while (true) {
				/**
				 * now listen for connections
				 * and service the connection in a separate thread.
				 */
				Runnable task = new Connection(sock.accept(), outputStreams, userList);
				System.out.println("connection made");
				exec.execute(task);
			}
		}
		catch (IOException ioe) { System.err.println(ioe); }
		finally {
			if (sock != null)
				sock.close();
		}
	}
}
