public class Task implements Thing
{
    final int ID = 2; // 1 represents Task instances
    String date;
    String startTime;
    String duration;
    String people;

    public Task(String date, String startTime, String duration, String people)
    {
        this.date = date;
        this.startTime = startTime;
        this.duration = duration;
        this.people = people;
    }

    public int getID()
    {
        return this.ID;
    }

    public String toString()
    {
        return "Task : " + "Start Date -> " + date + ", Start Time -> " + startTime + ", Duration -> " + duration + ", People Assigned -> " + people + "\n"; 
    }
}
