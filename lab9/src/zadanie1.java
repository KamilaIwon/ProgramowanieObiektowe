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
        System.out.print("\n---------------------\nzadanie 1a\n");

        int parz = 0;
        int nieparz = 0;
        for(int i = 0; i < n; ++i){
            if(tab[i] % 2 == 0) ++parz;
            else ++nieparz;
        }
        System.out.printf("nieparzyste: %d,  parzyste: %d", nieparz, parz);

        System.out.print("\n---------------------\nzadanie 1b\n");
        int uj = 0;
        int dod = 0;
        int zer = 0;

        for(int i = 0; i < n; ++i){
            if(tab[i] < 0) ++uj;
            if(tab[i] == 0) ++zer;
            if(tab[i] > 0) ++dod;
        }
        System.out.printf("ujemne: %d,  zerowe: %d, dodatnie: %d", uj, zer, dod);

        System.out.print("\n---------------------\nzadanie 1c\n");
        int maks = tab[0];
        int ile = 0;

         for(int i = 1; i < n; ++i){
             if(tab[i] > maks){
                 maks = tab[i];
             }
         }
         for(int i = 0; i < n; ++i){
             if(tab[i] == maks) ++ile;
         }
         System.out.printf("Najwiekszy element: %d, wystepuje %d razy", maks, ile);

        System.out.print("\n---------------------\nzadanie 1d\n");
        int sumaUj = 0;
        int sumaDod = 0;

        for(int i = 0; i < n; ++i){
            if(tab[i] < 0){
                sumaUj += tab[i];
            }
            if(tab[i] > 0){
                sumaDod += tab[i];
            }
        }
        System.out.printf("suma ujemych: %d, suma dodatnich: %d", sumaUj, sumaDod);

        System.out.print("\n---------------------\nzadanie 1e\n");
        int maksDl = 0;
        int tym_maks = 0;

        for(int i = 0; i < n; ++i){
            if(tab[i] < 1){
                tym_maks = 0;
                continue;
            }
            tym_maks += 1;
            if ( maksDl < tym_maks){
                maksDl = tym_maks;
            }
        }
        if(tym_maks > maksDl){
            maksDl = tym_maks;
        }
        System.out.printf("Najdluzszy lancuch dodatnich: %d", maksDl);

        System.out.print("\n---------------------\nzadanie 1g\n");
        int prawy, lewy;
        System.out.print("podaj lewy: ");
        lewy = s.nextInt();

        System.out.print("podaj prawy: ");
        prawy = s.nextInt();

        if (prawy < lewy || lewy < 1 || lewy >= n || prawy >= n)
        {
            System.out.println("Wrong numbers.");
            return;
        }

        int temp;

        while (lewy < prawy)
        {
            temp = tab[lewy];
            tab[lewy] = tab[prawy];
            tab[prawy] = temp;

            ++lewy;
            --prawy;
        }
        printArray(tab, n);

        System.out.print("\n---------------------\nzadanie 1f\n");
        for(int i = 0; i < n; ++i){
            if(tab[i] < 0){
                tab[i] = -1;
            }
            if(tab[i] > 0){
                tab[i] = 1;
            }
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