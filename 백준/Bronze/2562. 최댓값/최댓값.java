import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[9];

        for (int i = 0; i <9; i++) {
            int a = Integer.parseInt(br.readLine());
            arr[i] = a;
        }

        int max = 0;
        int cnt = 0;

        for (int i = 0; i < 9; i++ ) {
            if (max < arr[i]) {
                max = arr[i];
                cnt = i+1;
            }
        }

        bw.write(String.valueOf(max));
        bw.newLine();
        bw.write(String.valueOf(cnt));
        bw.flush();
        bw.close();
    }
}
