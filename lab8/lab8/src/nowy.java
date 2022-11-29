import java.lang.Math;
import java.util.Scanner;

public class nowy {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Podaj n: ");

        int n = scanner.nextInt();
        float[] numbers = new float[n];

        for (int i = 0; i < n; ++i)
        {
            System.out.printf("Podaj a%d:%n", i);
            numbers[i] = scanner.nextFloat();
        }
        
    }
}
