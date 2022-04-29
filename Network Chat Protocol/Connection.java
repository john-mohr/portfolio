/**
 * This is the separate thread that services each
 * incoming echo client request.
 *
 * @author Greg Gagne 
 */

import java.net.*;
import java.util.ArrayList;
import java.io.*;
import java.util.*;
public class Connection implements Runnable
{
	private Socket client;
	private static Handler handler = new Handler();
	private ArrayList<DataOutputStream> outputStreams;
	private Dictionary userList;
	
	public Connection(Socket client, ArrayList<DataOutputStream> outputStreams, Dictionary userList) {
		this.client = client;
		this.outputStreams = outputStreams;
		this.userList = userList;
	}

    /**
     * This method runs in a separate thread.
     */	
	public void run() { 
		try {
			handler.process(client, outputStreams, userList);
		}
		catch (java.io.IOException ioe) {
			System.err.println(ioe);
		}
	}
}

