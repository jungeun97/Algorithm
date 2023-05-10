import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String c = br.readLine();

        if (c.startsWith("A")) {
            if (c.endsWith("+")) {
                bw.write(String.valueOf(4.3));
            } else if (c.endsWith("0")) {
                bw.write(String.valueOf(4.0));
            } else {
                bw.write(String.valueOf(3.7));
            }
        } else if (c.startsWith("B")) {
            if (c.endsWith("+")) {
                bw.write(String.valueOf(3.3));
            } else if (c.endsWith("0")) {
                bw.write(String.valueOf(3.0));
            } else {
                bw.write(String.valueOf(2.7));
            }
        } else if (c.startsWith("C")) {
            if (c.endsWith("+")) {
                bw.write(String.valueOf(2.3));
            } else if (c.endsWith("0")) {
                bw.write(String.valueOf(2.0));
            } else {
                bw.write(String.valueOf(1.7));
            }
        } else if (c.startsWith("D")) {
            if (c.endsWith("+")) {
                bw.write(String.valueOf(1.3));
            } else if (c.endsWith("0")) {
                bw.write(String.valueOf(1.0));
            } else {
                bw.write(String.valueOf(0.7));
            }
        } else {
            bw.write(String.valueOf(0.0));
        }
        bw.flush();
        bw.close();
    }
}