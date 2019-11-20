import java.util.*;
import java.io.*;

public class ToDo
{
    public static void main(String [] args)
    {
        Queue q = new Queue();

        // Set up dictionary for Queue methods
        Map<String, Runnable> commands = new HashMap<>();
        commands.put("quit", () -> System.exit(0));
        commands.put("top", () -> q.top());
        commands.put("isEmpty", () -> q.isEmpty());
        commands.put("length", () -> q.length());
        commands.put("dequeue", () -> q.dequeue());
        //commands.put("enqueue", () -> q.enqueue());
        //commands.put("help", () -> help());

        //Scanner in = new Scanner(System.in);
        //String [] input;
        System.out.println("Welcome! For help on how to use the program please type 'help'");
        
        //while(in.hasNextLine())

        // Queue tests
        q.enqueue(new Event("21/12/1998", "12:00", "Cavan"));
        q.dequeue();
        q.dequeue();
        q.dequeue();
        q.dequeue();
        q.writeToFile();
    }
}
