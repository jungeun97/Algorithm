import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.TimeZone;

public class Main {
    public static void main(String[] args) {
        Date date = new Date();
        DateFormat df = new SimpleDateFormat("YYYY-MM-dd");
        System.out.println(df.format(date));

    }
}




