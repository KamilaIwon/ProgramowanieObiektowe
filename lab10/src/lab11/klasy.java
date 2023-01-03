package lab11;

public class klasy {

    public static void main(String[] args) {

        RachunekBankowy saver1 = new RachunekBankowy(2000.00);
        RachunekBankowy saver2 = new RachunekBankowy(3000.00);
        RachunekBankowy.setRocznaStopaProcentowa(0.04);
        saver1.obliczMiesieczneOdsetki();
        saver2.obliczMiesieczneOdsetki();
        System.out.println("saver1: " + saver1.getSaldo() + "\nsaver2: " + saver2.getSaldo());
        RachunekBankowy.setRocznaStopaProcentowa(0.05);
        saver1.obliczMiesieczneOdsetki();
        saver2.obliczMiesieczneOdsetki();
        System.out.println("saver1: " + saver1.getSaldo() + "\nsaver2: " + saver2.getSaldo());
    }
}


class RachunekBankowy {
    private static double rocznaStopaProcentowa;
    private double saldo;

    // konstruktor domyslny
    public RachunekBankowy() {
        this.saldo = 0.0;
    }

    // konstruktor glowny
    public RachunekBankowy(double saldoValue) {
        this.saldo = saldoValue;
    }

    public void obliczMiesieczneOdsetki() {
        double odsetki = (this.saldo * RachunekBankowy.rocznaStopaProcentowa) / 12;
        this.saldo += odsetki;
    }

    public static void setRocznaStopaProcentowa(double value) {
        RachunekBankowy.rocznaStopaProcentowa = value;
    }

    public double getSaldo(){
        return this.saldo;
    }


}

