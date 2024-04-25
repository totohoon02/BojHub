import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] strNumbers = reader.readLine().split(" ");
        double result = Double.parseDouble(strNumbers[0]) / Double.parseDouble(strNumbers[1]);
        System.out.println(result);
    }
}