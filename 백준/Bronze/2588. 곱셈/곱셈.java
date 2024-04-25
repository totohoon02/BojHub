import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int num1 = Integer.parseInt(reader.readLine());
        char[] num2 = reader.readLine().toCharArray();
        int result = 0;

        for (int i = num2.length - 1; i >= 0; i--) {
            int cross = num1 * Character.getNumericValue(num2[i]);
            System.out.println(cross);
            result += (int) (cross * Math.pow(10, num2.length -1 - i));
        }

        System.out.println(result);


    }
}