import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] info = br.readLine().split(" ");
        int N = Integer.parseInt(info[0]);
        LinkedList<Integer> deque = new LinkedList<>();
        for (int i = 1; i <= N; i++) deque.add(i);
        String[] indices = br.readLine().split(" ");

        int count = 0;
        for (int i = 0; i < indices.length; i++) {
            int index = deque.indexOf(Integer.parseInt(indices[i]));
            boolean isLeft = index <= deque.size() - index;
            if (isLeft) {
                while (index > 0) {
                    deque.addLast(deque.removeFirst());
                    index--;
                    count++;
                }
            } else {
                while (index < deque.size()) {
                    deque.addFirst(deque.removeLast());
                    index++;
                    count++;
                }
            }
            deque.removeFirst();
        }
        System.out.println(count);
    }
}
