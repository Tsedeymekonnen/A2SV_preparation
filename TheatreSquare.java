import java.util.Scanner;
public class TheatreSquare 
{  
public static void main(String... arg){
     long m, n, a, x, y;
     try (Scanner scanner = new Scanner(System.in)) {
        m = scanner.nextLong();
        n = scanner.nextLong();
        a = scanner.nextLong();
    }
    if(m % a == 0)
    {
        x = m / a;
   }
   else{
        x = m / a + 1;
   }
   if(n % a == 0){
        y = n / a;
   }
   else{
        y = n / a + 1;
   }
   System.out.println( x * y);



    }
}
