# Datenstrukturen

* Eine Datenstruktur wird definiert als eine bestimmte Art und Weise, Daten in unseren Geräten zu speichern und zu organisieren, um die Daten effizient und effektiv nutzen zu können.

* Die Hauptidee hinter der Verwendung von Datenstrukturen besteht darin, die Zeit- und Speicherkomplexitäten zu minimieren.

* Eine effiziente Datenstruktur benötigt minimalen Speicherplatz und erfordert minimale Zeit zur Ausführung der Daten.

# Zeit komplexität

Stellen Sie sich vor, Sie haben in einem Klassenzimmer mit 100 Schülern einem bestimmten Schüler Ihren Stift gegeben. Sie müssen diesen Stift wiederfinden, ohne zu wissen, wem Sie ihn gegeben haben.

# Zeit komplexität

* $O(n^2)$: Du gehst zur ersten Person in der Klasse und fragst, ob sie den Stift hat. Gleichzeitig fragst du diese Person nach den anderen 99 Personen im Klassenzimmer, ob sie den Stift haben, und so weiter. Das bezeichnen wir als $O(n^2)$.

* $O(n)$: Jeden Schüler einzeln zu fragen, ist $O(N)$.

* $O(\log n)$: Jetzt teile ich die Klasse in zwei Gruppen auf und frage: "Ist der Stift auf der linken Seite oder der rechten Seite des Klassenzimmers?" Dann nehme ich diese Gruppe und teile sie erneut in zwei und frage wieder, und so weiter. Wiederhole den Prozess, bis du nur noch einen Schüler übrig hast, der deinen Stift hat. Das ist das, was du mit $O(\log n)$ meinst.

# Zeit komplexität

* Du gehst zur ersten Person in der Klasse und fragst, ob sie den Stift hat. Gleichzeitig fragst du diese Person nach den anderen 99 Personen im Klassenzimmer, ob sie den Stift haben, und so weiter. Das bezeichnen wir als $O(n^2)$.

* Jeden Schüler einzeln zu fragen, ist $O(N)$.

* Jetzt teile ich die Klasse in zwei Gruppen auf und frage: "Ist der Stift auf der linken Seite oder der rechten Seite des Klassenzimmers?" Dann nehme ich diese Gruppe und teile sie erneut in zwei und frage wieder, und so weiter. Wiederhole den Prozess, bis du nur noch einen Schüler übrig hast, der deinen Stift hat. Das ist das, was du mit $O(\log n)$ meinst.

# Beispiel 1

Was ist die Zeit komplexität?

```cpp
#include <iostream>
using namespace std;
 
int main()
{
    cout << "Hello World";
    return 0;
}
```

# Beispiel 1 Antwort

Im obigen Code wird "Hello World" nur einmal auf dem Bildschirm ausgegeben. Daher ist die Zeitkomplexität konstant: $O(1)$, das heißt, es wird jedes Mal eine konstante Zeitspanne benötigt, um den Code auszuführen, unabhängig davon, welches Betriebssystem oder welche Maschinenkonfigurationen verwendet werden. Der zusätzliche Speicherplatzbedarf beträgt ebenfalls $O(1)$.


# Beispiel 2 

```cpp
#include <iostream>
using namespace std;
 
int main()
{
 
    int i, n = 8;
    for (i = 1; i <= n; i++) {
        cout << "Hello World !!!\n";
    }
    return 0;
}
```

# Beispiel 2 Antwort

Zeitkomplexität: Im obigen Code wird "Hello World !!!" nur n-mal auf dem Bildschirm ausgegeben, da der Wert von n variieren kann. Daher ist die Zeitkomplexität linear: $O(n)$, das heißt, es wird jedes Mal eine lineare Zeitspanne benötigt, um den Code auszuführen. Der zusätzliche Speicherplatzbedarf beträgt ebenfalls $O(1)$.


# Beispiel 3

```cpp
#include <iostream>
using namespace std;
 
int main()
{
 
    int i, n = 8;
    for (i = 1; i <= n; i=i*2) {
        cout << "Hello World !!!\n";
    }
    return 0;
}

```

# Beispiel 3 Antwort

Zeitkomplexität: $O(log2(n))$

# Wie findet man die Zeitkomplexität

Nehmen wir ein Beispiel 

```cpp
int sum(int a,int b)
{
 return a+b; 
}
 
int main() {
      int a = 5, b = 6;
    cout<<sum(a,b)<<endl;
    return 0;
}
```

# Wie findet man die Zeitkomplexität

* Der obige Code benötigt 2 Zeiteinheiten (konstant):
    * eine für die arithmetischen Operationen und
    * eine für die Rückgabe (gemäß den oben genannten Konventionen).
* Daher beträgt die Gesamtkosten für die Durchführung der Summenoperation $(Tsum) = 1 + 1 = 2$
* Die Zeitkomplexität ist $O(2) = O(1)$, da 2 konstant ist.


