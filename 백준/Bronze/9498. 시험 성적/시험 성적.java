import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int score = parseToInt(readLineAsStrArray()[0]);
        if(score >= 90){
            System.out.println("A");
        } else if (score >= 80) {
            System.out.println("B");
        } else if (score >= 70) {
            System.out.println("C");
        }else if (score >= 60) {
            System.out.println("D");
        }else{
            System.out.println("F");
        }

    }

    public static String[] readLineAsStrArray() throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        return reader.readLine().split(" ");
    }

    public static int parseToInt(String strNum){
        return Integer.parseInt(strNum);
    }
}