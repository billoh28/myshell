import java.util.Scanner;
import java.io.*;

public class Runner
{
    public static void main(String [] args)
    {
        Queue todo = new Queue();
        Scanner in = new Scanner(System.in);
        System.out.println("Welcome! What would you like to add something to your to-do list?[y/n]");
        String input = (in.next()).toLowerCase();
        String date;
        String time;
        String location;
        int duration;
        String [] people;
        Thing t;

        // Add something to the list
        if(input.equals("y"))
        {
            // Take in task or event
            System.out.println("Event or Task?");
            input = (in.next()).toLowerCase();

            // Event
            if(input.equals("event"))
            {
                // Need date, start time, location
                System.out.println("Please provide a date, start time and location for the event, respectively");
                // todo.add(new Event("21/12/1998", "12:00", "Cavan"));
                // take in input
                try
                {
                    date = in.next();
                    time = in.next();
                    location = in.next();
                    t = new Event(date, time, location);
                    todo.add(t);
                }

                catch(Exception e)
                {
                    System.out.println("Error: input invalid");
                }
            }

            // Task
            else if(input.equals("task"))
            {
                // Need date, start time, duration, list of people assigned to task
                System.out.println("Please provide a date, start time, duration and people, respectively, for the task");
                try
                {
                    date = in.next();
                    time = in.next();
                    duration = Integer.parseInt((in.next()));
                    people = (in.nextLine()).split(", ");
                    t = new Task(date, time, duration, people);
                    todo.add(t);
                }

                catch(Exception e)
                {
                    System.out.println("Error: input invalid");
                }
            }

            else
            {
                System.out.println("Invalid input provided");
            }
        }

        else if(input.equals("n"))
        {
            System.out.println("Would you like to remove something from your to-do list?[y/n]");
            input = (in.next()).toLowerCase();
            if(input.equals("y"))
            {
                if(!(todo.isEmpty()))
                {
                    t = todo.pop();
                    System.out.println(t.toString());
                }

                else{System.out.println("Error: to-do list is empty");}
            }
        }

        System.out.println("Goodbye!");
    }
}
