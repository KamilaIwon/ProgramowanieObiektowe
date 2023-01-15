package probne_kolokwium;

public class mainn {
    public static void main(String[] args) {
        // Tworzenie obiektu klasy Mebel
        Mebell maly = new Mebell("Maly Mebel", 1, 0.5, 4);
        System.out.println(maly); // wypisanie danych obiektu maly
        System.out.println("Ilość mebli: " + Mebell.getIle()); // wypisanie ilości mebli

        // Tworzenie obiektu klasy Mebel z domyślną wartością pola nazwa
        Mebell sredni = new Mebell(2, 1, 4);
        System.out.println(sredni); // wypisanie danych obiektu sredni

        // Tworzenie obiektu klasy Biurko
        Biurkoo maleBiurko = new Biurkoo("Male Biurko", 2, 1, 4, 22);
        maleBiurko.setDataProdukcji(2005, 2, 28); // zmiana pola dataProdukcji
        System.out.println(maleBiurko); // wypisanie danych obiektu maleBiurko
        System.out.println("Ilość mebli: " + Mebell.getIle()); // wypisanie ilości mebli

        // Tworzenie dwuwymiarowej tablicy spis
        Mebell[][] spis = {{sredni, maly}, {maleBiurko, sredni}};

        // Wypisanie tablicy spis
        for (Mebell[] wiersz : spis) {
            for (Mebell mebel : wiersz) {
                System.out.print(mebel + " ");
            }
            System.out.println();
        }

        // Tworzenie tablicy spisNazw
        String[] spisNazw = {"sredni", "maly", "maleBiurko", "sredni"};

        // Wypisanie tablicy spisNazw
        for (String nazwa : spisNazw) {
            System.out.print(nazwa + " ");
        }
        System.out.println();

        // Wypisanie obiektów z tablicy spis za pomocą instrukcji foreach
        for (Mebell[] wiersz : spis) {
            for (Mebell mebel : wiersz) {
                System.out.print(mebel + " ");
            }
            System.out.println();
        }

        // Porównanie obiektu sredni z obiektem maly i maleBiurko
        System.out.println("Porównanie sredni i maly: " + sredni.equals(maly));
        System.out.println("Porównanie sredni i maleBiurko: " + sredni.equals(maleBiurko));

        // Liczenie ilości biurek w tablicy spis
        int iloscBiurek = 0;
        for (Mebell[] wiersz : spis) {
            for (Mebell mebel : wiersz) {
                if (mebel instanceof Biurkoo) {
                    iloscBiurek++;
                }
            }
        }
        System.out.println("Ilość biurek w tablicy spis: " + iloscBiurek);

        // Wypisanie nazw klas obiektów z tablicy spis
        for (Mebell[] wiersz : spis) {
            for (Mebell mebel : wiersz) {
                System.out.print(mebel.getClass().getName() + " ");
            }
            System.out.println();
        }
    }
}


