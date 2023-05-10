import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // String str = br.readLine();
        // StringTokenizer st = new StringTokenizer(str, " ");
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c;

        if ( a>0 && b>0) {
            c = 1;
        } else if ( a>0 && b <0) {
            c = 4;
        } else if ( a<0 && b<0) {
            c = 3;
        } else {
            c = 2;
        }

        bw.write(String.valueOf(c));
        bw.flush();
        bw.close();

    }
}
