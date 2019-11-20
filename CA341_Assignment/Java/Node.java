public class Node
{
    Thing value;
    Node next;

    public Node(Thing value)
    {
        this.value = value;
    }

    public void addNext(Node next)
    {
        this.next = next;
    }

    public Thing getter()
    {
        return this.value;
    }
}
