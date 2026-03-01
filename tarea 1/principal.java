package auxiliatura;

public class principal {
    public static void main(String[] args) {
         Anime a1 = new Anime ("Overflow", "Hentai", 8); 
         Anime a2 = new Anime ("One Piece", "Shonen", 234322034); 
         Televisor t1 = new Televisor ("LG", 1880, "OLED");
         Televisor t2 = new Televisor ("Samsung", 2440, "OLED");
         Instrumento i1 = new Instrumento ("Guitarra", "madera", "cordofono"); 
         Instrumento i2 = new Instrumento ("Trompeta", "laton", "Aerofono");
         System.out.print(t1.toString()); 
         
         
    }
}
