import java.util.*;

public class Main {
    public static void main(String[] args) {
/*
        // All about list
        List ix = new ArrayList();

        ix.add(12);
        ix.add(13);
        ix.add(14);

        System.out.println(ix);
        System.out.println(ix.get(2));
        System.out.println(ix.indexOf(13));
        System.out.println(ix.size());
 */

        // Map
/*
        Map map = new HashMap();

        map.put(2, "Alok");

        System.out.println(map);
        System.out.println(map.get(2));
        System.out.println(map.getClass());

        System.out.println(map.values());
        System.out.println(map.keySet());
*/

        // It maintains key order in ascending
//        Map tm = new TreeMap();
//
//        tm.put(1,11);
//        tm.put(3,13);
//        tm.put(2,10);
//
//        System.out.println(tm);


        Map mp = new LinkedHashMap();

        mp.put(1,10);
        mp.put(3,11);
        mp.put(11,1);

        System.out.println(mp);

    }
}

