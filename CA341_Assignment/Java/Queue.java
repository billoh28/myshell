import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class Queue
{
    // first in -> first out
    Node first;
    Node pointer;
    File file = new File("todo.txt");
    String output;
    FileWriter writer;
    Scanner readFile;

    public Queue()
    {
        // Read if file is empty or not
        try
        {
            output = file.getAbsolutePath();
            if(file.length() > 0)
            {
                // Read file and create queue
                readFile = new Scanner(file);
                String line = "";
                String object = "";
                String [] input;
                while(readFile.hasNextLine())
                {
                    line = readFile.nextLine();
                    // Add existing object from file to Queue
                    // check first five chars of each line to see if event or task
                    object = line.substring(0,5).strip();
                    input = line.split(" -> ");
                    
                    if(object.equals("Event"))
                    {
                        // if event required
                        for(int i=0; i<input.length; i++){input[i] = input[i].split(",")[0];} // should seperate required input
                        enqueue(new Event(input[1], input[2], input[3]));
                    }

                    else if(object.equals("Task"))
                    {
                        // if task required 
                        for(int i=0; i<input.length - 1; i++){input[i] = input[i].split(",")[0];} // should seperate required input, dont split last element
                        enqueue(new Task(input[1], input[2], input[3], input[4]));
                    }
                }
                readFile.close();
            }
            // Create or overwrite file "todo.txt"
            writer = new FileWriter(output, false);
            writer.close();
        }

        catch(Exception e)
        {
            System.out.println("Error: File '../todo.txt' not found: Create file to use program");
        }
    }

    public void enqueue(Thing value)
    {
        if(first == null)
        {
            first = new Node(value);
            pointer = first;
        }

        else
        {
            Node temp = new Node(value);
            pointer.addNext(temp);
            pointer = temp;
        }
    }

    public void writeToFile()
    {
        try
        {
            writer = new FileWriter(output, true); // append to file
            while(first != null)
            {
                writer.write(first.value.toString());
                first = first.next;
            }
            writer.close();
        }

        catch(Exception e)
        {
            System.out.println("Error: IOException occurred while writing to file");
        }
    }

    public String dequeue()
    {
        if(!(this.isEmpty()))
        {
            Thing temp = first.getter();
            first = first.next;
            return temp.toString();
        }
        return null;
    }

    public int length()
    {
        Node n = first;
        int i = 0;

        while(n != null)
        {
            i++;
            n = n.next;
        }

        return i;
    }

    public boolean isEmpty()
    {
        return this.length() == 0;
    }

    public Thing top()
    {
        return first.getter();
    }
}
