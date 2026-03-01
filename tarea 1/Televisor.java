
package auxiliatura;

public class Televisor {
    private String marca; 
    private int resolucion; 
    private String tipo; 
    
    public Televisor(String x, int y, String z){
        this.marca = x; 
        this.resolucion = y; 
        this.tipo = z ; 
    }
    public Televisor(){
        
    }
    public String toString(){
        return "marca: " + this.marca + " resolucion: " + this.resolucion + " tipo: " + this.tipo;
    }
    
    
}
