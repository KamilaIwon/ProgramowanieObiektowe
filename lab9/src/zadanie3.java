import java.util.Random;
import java.util.Scanner;

// iloczyn macierzy + macierz c
public class zadanie3 {
    public static void main(String[] args) {

        Random r = new Random();
        Scanner s = new Scanner(System.in);

        System.out.print("Podaj m: ");
        int m = s.nextInt();

        System.out.print("Podaj n: ");
        int n = s.nextInt();

        System.out.print("Podaj k: ");
        int k = s.nextInt();

        if (m < 1 || n < 1 || k < 1 || m > 10 || n > 10 || k > 10) {
            System.out.println("Bledne liczby");
            return;
        }

        int sizeA = m * n;
        int sizeB = n * k;

        int[] matrixA = new int[sizeA];
        int[] matrixB = new int[sizeB];

        for (int i = 0; i < sizeA; ++i) matrixA[i] = r.nextInt(10);
        for (int i = 0; i < sizeB; ++i) matrixB[i] = r.nextInt(10);

        printMatrix(matrixA, m);
        printMatrix(matrixB, n);
    }

        static void printMatrix(int[] matrix, int columns)
        {
            System.out.println("Matrix:");

            for (int i = 0; i < matrix.length; ++i)
            {
                if (i > 0 && i % columns == 0) System.out.println();

                System.out.printf("%d ", matrix[i]);
            }

            System.out.println();
        }
    }

