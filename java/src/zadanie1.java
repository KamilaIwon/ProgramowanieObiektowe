import java.util.Random;
import java.util.Scanner;

public class zadanie1 {
    public static void main(String[] args)
    {
        Random r = new Random();
        Scanner s = new Scanner(System.in);
        int n;

        System.out.print("ile ma byc elementow tablicy n: ");
        n = s.nextInt();

        int[] tab = new int[n];

        for (int i = 0; i < n; ++i)
        {
            tab[i] = r.nextInt(1999) - 999;
        }

        printArray(tab, n);
    }
    static void printArray(int[] array, int n)
    {
        for (int i = 0; i < n; ++i)
        {
            System.out.printf("%d ", array[i]);
        }

        System.out.println();
    }
}