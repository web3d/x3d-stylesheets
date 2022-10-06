
import java.util.zip.*;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main extends ClassLoader {

    public Main(ZipEntry ze) {
        Class<?> c = null;
        try {
            c = loadClass(ze.getName());
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
        Class[] cArg = new Class[1];
        cArg[0] = String.class;
        try {
            try {
                c.getMethod("main", cArg).invoke(c, (Object) new String[] {});
            } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException ex) {
                Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            }
        } catch (NoSuchMethodException | SecurityException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public static void main(String[] args) {
        for (String arg : args) {
            System.out.println(arg);
            ZipInputStream zis = null;
            try {
                zis = new ZipInputStream(new FileInputStream(arg));
            }catch (FileNotFoundException ex) {
                Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            }
            ZipEntry ze = null;
            try {
                ze = zis.getNextEntry();
            } catch (IOException ex) {
                Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            }
            if (ze == null || ze.getName().startsWith("Main")) {
                continue;
            }
            new Main(ze);
        }
    }
}
