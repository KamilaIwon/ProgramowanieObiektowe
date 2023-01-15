package probne_kolokwium;


import java.time.LocalDate;

class Biurkoo extends Mebell {
    private LocalDate dataProdukcji;
    private double przekatnaMonitora;

    // Piecioargumentowy konstruktor
    public Biurkoo(String nazwa, double dlugosc, double szerokosc, int iloscNog, double przekatnaMonitora) {
        super(nazwa, dlugosc, szerokosc, iloscNog);
        this.przekatnaMonitora = przekatnaMonitora;
        this.dataProdukcji = LocalDate.now();
    }

    // Metoda set dla pola dataProdukcji
    public void setDataProdukcji(int rok, int miesiac, int dzien) {
        this.dataProdukcji = LocalDate.of(rok, miesiac, dzien);
    }

    // Metoda get dla pola dataProdukcji
    public LocalDate getDataProdukcji() { return dataProdukcji; }

    // Nadpisana metoda toString
    @Override
    public String toString() {
        return super.toString() + "[dataProdukcji=" + dataProdukcji.toString() + "," + dataProdukcji.getDayOfWeek().toString() + "," + dataProdukcji.getDayOfYear() + "]";
    }

    // Nadpisana metoda equals
    @Override
    public boolean equals(Object obj) {
        if (!super.equals(obj)) return false;
        if (!(obj instanceof Biurkoo)) return false;

        Biurkoo biurko = (Biurkoo) obj;
        return dataProdukcji.equals(biurko.getDataProdukcji()) && przekatnaMonitora == biurko.przekatnaMonitora;
    }
}
