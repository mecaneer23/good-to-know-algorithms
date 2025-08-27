private class Node<T> {
    private T data;
    private Node next;

    Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}

public class LinkedList<T> {
    private Node head;

    public LinkedList() {
        this.head = null;
    }

    public void add(T item) {
        Node newNode = new Node(item);

        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;
        while (current.getNext() != null) {
            current = current.getNext();
        }

        current.setNext(newNode);
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(1);
        list.add(2);
        list.add(3);
    }
}