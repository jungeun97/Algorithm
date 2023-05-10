import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        int result = 0;

        if ( a % 4 == 0 ) {
            if (a % 100 != 0 || a % 400 == 0) {
                result = 1;
            }
        }

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}