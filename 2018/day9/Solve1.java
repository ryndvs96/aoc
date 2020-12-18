
// # 424 players; last marble is worth 71482 points
// ps = 424
// ls = 7148200
import java.util.LinkedList;
public class Solve1 {
  public static void main(String[] args) {
    int ps = 424;
    int ls = 7148200;
    
    LinkedList<Integer> circ = new LinkedList<>();
    LinkedList<Integer> scores = new LinkedList<>();
    for (int i = 1; i <= ps + 1; i++) {
      scores.add(0);
    }
    circ.add(0);
    circ.add(1);
    int p = 1;
    int curr = 1;
    for (int i = 2; i <= ls; i++) {
      p = p + 1;
      if (p == ps + 1) {
        p = 1;
      }
      if (i % 23 == 0) {
        int n = circ.size();
        int seven = (curr - 7) % n;
        if (seven < 0) {
          seven = n + seven;
        }
        int val = circ.remove(seven);
        curr = seven;
        scores.set(p, scores.get(p) + val + i);
      } else {
        int n = circ.size();
        int one = (curr + 1) % n;
        int two = (curr + 2) % n;
        circ.add(two, i);
        curr = two;
      }
    }
    int m = 0;
    for (Integer c : circ) {
        if (c > m) {
          m = c;
        }
    }
    System.out.println("" + m);
  }
}

// circ = {0: 0, 1: 1}
// scores = [0 for i in range(0, ps + 1)]
// p = 1
// curr = 1
// for i in range(2, ls + 1):
//     if i % 100000 == 0:
//         print(i)
//     p += 1
//     if p == ps + 1:
//         p = 1
//     if i % 23 == 0:
//         seven = (curr - 7) % n
//         val = circ.pop(seven)
//         curr = seven
//         scores[p] += val + i
//     else:
//         n = len(circ)
//         one = (curr + 1) % n 
//         two = (curr + 2) % n 
//         circ.insert(two, i)
//         curr = two
// 
// print(max(scores))


