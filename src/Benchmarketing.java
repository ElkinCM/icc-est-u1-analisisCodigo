public class Benchmarketing {

    private MetodosOrdenamiento MetodosOrdenamiento;

    public Benchmarketing() {



        MetodosOrdenamiento = new MetodosOrdenamiento();
            int[] arreglo = generarArreglAleatorio(10000);
            Runnable tareaBurbuja = () -> MetodosOrdenamiento.burbujaTradicional(arreglo);

            double tiempoBurbujaMillis = medirConCurrentTime(tareaBurbuja);
            double tiempoBurbujaNanos = medirConNanoTime(tareaBurbuja);

            System.out.println("Tiempo burbuja tradicional (nanosegundos): " + tiempoBurbujaNanos + " segundos");
            System.out.println("Tiempo burbuja tradicional (milisegundos): " + tiempoBurbujaMillis + " segundos");
            

            
        }
    
    private int[] generarArreglAleatorio(int size) {
            int[] arreglo = new int[size];
            for (int i = 0; i < size; i++) {
                arreglo[i] = (int) (Math.random() * 9999999);
            }
            return arreglo;
    }
    

    public final double medirConNanoTime (Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;

    }

    public final double medirConCurrentTime (Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0;

    }


}
