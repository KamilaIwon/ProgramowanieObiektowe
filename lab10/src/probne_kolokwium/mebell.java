package probne_kolokwium;

class Mebell {
    private String nazwa;
    private double dlugosc;
    private double szerokosc;
    private int iloscNog;
    private static int ile;

    // Czteroargumentowy konstruktor
    public Mebell(String nazwa, double dlugosc, double szerokosc, int iloscNog) {
        this.nazwa = nazwa;
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.iloscNog = iloscNog;
        ile++;
    }

    // Trzyargumentowy konstruktor wykorzystujący powyższy konstruktor
    public Mebell(double dlugosc, double szerokosc, int iloscNog) {
        this("Jakis Mebel", dlugosc, szerokosc, iloscNog);

    }

    // Metody get dla wszystkich pól
    public String getNazwa() { return nazwa; }
    public double getDlugosc() { return dlugosc; }
    public double getSzerokosc() { return szerokosc; }
    public int getIloscNog() { return iloscNog; }

    // Nadpisana metoda toString
    @Override
    public String toString() {
        if (!nazwa.equals("Jakis Mebel")) {
            return getClass().getName() + "[nazwa=" + nazwa + ",dlugosc=" + dlugosc + ",szerokosc=" + szerokosc + ",iloscNog=" + iloscNog + "]";
        }
        else {
            return getClass().getName() + "[dlugosc=" + dlugosc + ",szerokosc=" + szerokosc + ",iloscNog=" + iloscNog + "]";
        }
    }

    // Nadpisana metoda equals
    @Override
    public boolean equals(Object obj) {
        if (obj == null) return false;
        if (obj == this) return true;
        if (!(obj instanceof Mebel)) return false;

        Mebell mebel = (Mebell) obj;
        return nazwa.equals(mebel.getNazwa()) && dlugosc == mebel.getDlugosc() && szerokosc == mebel.getSzerokosc() && iloscNog == mebel.getIloscNog();
    }

    // Statyczna metoda getIle
    public static int getIle() { return ile; }
}
