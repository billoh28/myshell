import java.io.*;
import java.util.Scanner;

public class QueueV2
{
    // first in -> first out
    Node first;
    Node pointer;
    File file = new File("todo.txt");
    Boolean fileEmpty = true;
    String output;
    FileWriter writer;
    Scanner readFile;

    public QueueV2()
    {
        // Read if file is empty or not

        output = file.getAbsolutePath();

        if(file.length() > 0)
        {
            fileEmpty = false; // Set the file as non empty
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
            writer = new FileWriter(output, true);
            output = file.getAbsolutePath();

            while(this.first != null)
            {
                writer.write(this.first.toString());
            }
        }

        catch(IOException e)
        {
            System.out.println("Error: IOException " + e + " occurred while writing to file");
        }
    }

    public String dequeue()
    {
        if(!fileEmpty)
        {
            // Remove first line from file
            try
            {
                Scanner fileScanner = new Scanner(file);
                writer = new FileWriter(file);
                String next = "";
                String t = fileScanner.nextLine();
                
                while(fileScanner.hasNextLine())
                {
                    next = fileScanner.nextLine();
                    writer.write(next);
                }
                fileScanner.close();
                writer.close();
                return t;
            }

            catch(IOException e)
            {
                System.out.println(e);
            }
        }

        else if(!(this.isEmpty()))
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
