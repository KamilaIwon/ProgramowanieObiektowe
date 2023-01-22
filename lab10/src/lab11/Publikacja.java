package lab11;

import java.time.LocalDate;
import java.util.Objects;

public class Publikacja {
    private String tytul;
    private double cena;
    private LocalDate dataWydania;
    static int ile;

    public Publikacja(String tytul, double cena, int rok, int miesiac, int dzien) {
        this.tytul = tytul;
        this.cena = cena;
        this.dataWydania = LocalDate.of(rok, miesiac, dzien);
        ++ile;
    }

    public Publikacja(String tytul, double cena){
        this(tytul, cena, LocalDate.now().getYear(), LocalDate.now().getMonthValue(), LocalDate.now().getDayOfMonth());
    }

    public String getTytul() {
        return tytul;
    }

    public double getCena() {
        return cena;
    }

    public LocalDate getDataWydania() {
        return dataWydania;
    }


    public void setDataWydania(int rok, int miesiac, int dzien) {
        if (rok > 0 && miesiac > 0 && miesiac <= 12 && dzien > 0 && dzien <= 31){
            this.dataWydania = LocalDate.of(rok, miesiac, dzien);
        }
    }

    public static int getIle() {
        return ile;
    }

    @Override
    public String toString(){
        String text =  getClass().getName() + "[" + dataWydania + "], [" ;
        if (!tytul.equals("Publikacja nieznana")){
            text += tytul + "], [";
        }
        text +=  cena + "]";
        return text;

    }

    @Override
    public boolean equals(Object otherObject) {
        if (otherObject == this) return true;
        if (otherObject == null) return false;
        if (getClass() != otherObject.getClass()) return false;

        Publikacja other = (Publikacja) otherObject;
        return cena == other.cena && tytul.equals(other.tytul) && dataWydania.equals(other.dataWydania);
    }

    public void zwiekszCene( double procent){
        this.cena += cena*(procent/100);
    }

}
