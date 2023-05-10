import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            if ( i != t-1) {
                String a = br.readLine();
                bw.write(a.charAt(0));
                bw.write(a.charAt(a.length()-1));
                bw.newLine();
            } else {
                String a = br.readLine();
                bw.write(a.charAt(0));
                bw.write(a.charAt(a.length()-1));
            }
            
        }
        bw.flush();
        bw.close();
        
    }
}
