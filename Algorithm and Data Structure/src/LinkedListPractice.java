import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class LinkedListPractice {
    public static void main(String[] args) {
        /*LinkedList lst = new LinkedList();
        lst.add(3);
        lst.removeFirst();
        lst.add(5);
        lst.add(7);
        lst.addFirst(2);
        lst.removeLast();
        System.out.println(lst);*/
        /*Stack stack = new Stack();
        stack.push(new Integer(11));
        stack.push(new Integer(13));
        stack.push(new Integer(2));
        stack.peek();
        System.out.println(stack);
        stack.pop();
        System.out.println(stack);*/
        /*Stack stack = new Stack();

        stack.push(new Integer(1));
        stack.push(new Integer(3));
        stack.pop();
        stack.push(new Integer(2));

        System.out.println(stack);*/
        Queue queue = new LinkedList();
        queue.add(10);
        queue.add(24);
        queue.add(42);
        queue.add(5);
        queue.poll();
        queue.poll();
        System.out.println(queue);
    }
}
