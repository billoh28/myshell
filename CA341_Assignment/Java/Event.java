public class Event implements Thing
{
    final int ID = 1; // 1 represents Event instances
    
    String date;
    String startTime;
    String location;

    public Event(String date, String startTime, String location)
    {
        this.date = date;
        this.startTime = startTime;
        this.location = location;
    }

    public int getID()
    {
        return this.ID;
    }

    public String toString()
    {
        return "Event: " + "Start Date -> " + date + ", Start Time -> " + startTime + ", Location -> " + location + "\n"; 
    }
}
