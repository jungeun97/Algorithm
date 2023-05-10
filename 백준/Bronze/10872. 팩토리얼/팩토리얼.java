import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        int result = factorial(a);

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }

    public static int factorial(int a) {
        if ( a <= 1) return 1;
        return a * factorial(a-1);
    }
}
