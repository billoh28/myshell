import java.util.*;
import java.io.*;

public class ToDoV2
{
    public static void main(String [] args) throws Exception
    {
        QueueV2 q = new QueueV2();

        // Set up dictionary for Queue methods
        Map<String, Runnable> commands = new HashMap<>();
        //commands.put("quit", () -> System.exit(0));
        //commands.put("top", () -> q.top());
        //commands.put("isEmpty", () -> q.isEmpty());
        //commands.put("length", () -> q.length());
        //commands.put("dequeue", () -> q.dequeue());
        //commands.put("enqueue", () -> q.enqueue());
        //commands.put("help", () -> help());

        Scanner in = new Scanner(System.in);
        String [] input;
        System.out.println("Welcome! For help on how to use the program please type 'help'");
        
        //while(in.hasNextLine())

        // Queue tests
        q.enqueue(new Task("21/12/2019", "12:00", 3, new String [] {"Me", "and the bois"}));
        q.enqueue(new Task("21/12/2019", "12:00", 3, new String [] {"Me", "and the bois"}));
        q.enqueue(new Task("21/12/2019", "12:00", 3, new String [] {"Me", "and the bois"}));
        q.writeToFile();
        //String temp = q.dequeue();
        //System.out.println(temp);
    }
}
