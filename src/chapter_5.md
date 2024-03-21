# Sortieren und Suchen 

Informatik Studenten lernen das Sortieren verfahren mindestens 3 mal bevor sie ihren Abschluss bekommen.
Wieso ist Sortieren und Suchen für einen Informatiker bzw. in der Softwareentwicklung so wichtig?

* Sortieren ist die Grundlage für viele andere Algorithmen die schon exestieren oder die wir selber erstellen.
Das verstehen von Sortieren hilft einen Programmierer andere Probleme zu Lösen.

* Die Interessantesten Ideen und Erfindungen basieren auf das Sortieraglorithmen und sie werden überall verwendet,
bsp. Teile und Hersche, Datenstrukturen, Zufällige Algorithmen

* Computer haben in ihrer ganzen Lebenszeit mehr Zeit mit Sortieren verbracht als mit anderen dingen

**Wir werden in diesem Kapitel (Achtung auf Neuerungen) nur Quicksort Bubblesort Linearsort ansprechen**

## Anwendung

Es gibt viele Sortieraglorithmen und ihre Komplexitäten, dabei ist wichtig zu merken das
Clevere Sortieralgorithmen eine Komplexität von \\(O(n\ log\ n)\\)
\
\
Das ist ein große Verbesserungen zu den alten bzw. herkömmlichen \\(O(n^2)\\)

| n    | \\(n^2/4\\)    | n lg n  |
|---------------- | --------------- | --------------- |
| 10    | 25    | 33    
| 100    | 2 500   | 664   
| 1 000    | 250 000   | 9 965   
| 10 000    | 25 000 000   | 132 877   
| 100 000    | 2 500 000 000  | 1 660 960   

Ein Cleveres Sortieralgorithmen mit \\(O(n\ log\ n)\\) ist Essenziell für das Lösen von großen Problemen, 
stellt die vor du möchtest etwas suchen davor wäre es aber leichter die liste zu Sortieren aber die Liste
hat 10 000 000 Elemente. Da würde sich mit einer Quadratischen Komplexität das Sortieren nicht ausszahlen

* Beispiel: Binäre Suche
* Es gibt viele andere Anwendung die werden noch kommen sind aber nicht Prüfungsrelveant...

Wobei manche Probleme duruch linear time Algorithmen gelöst werden können, 
kann man mit Sortieren viele Probleme einfacher Lösen.

> **_Take-Home Lesson:_**: Sortieren ist eine klein Lösung für viele Algorithmen. Eine Sortierte Liste von Daten ist einer der Dinge die man als erstes machen sollte für das Effiziente Lösen eines Problems


# Sortieralgorithmus

Bei einem Sortieralgorithmus handelt es sich in der Informatik um ein Sortierverfahren, der einen Array nach dem gewünschten Suchkriterium ordnen soll.

Das funktioniert aber nur für eine streng schwache Ordnung, heißt entweder auf lexikografischer Basis – also nach Buchstaben bei einer Zeichenkette oder eben nummerisch – also nach Zahlen.

Zur Umsetzung wird also eine Menge benötigt, die sortiert werden soll, die dabei aber auch gleichzeitig die Eingabe darstellt. Das Hauptziel eines Sortieralgorithmus ist zum einen, eine gegebene Menge effizient zu ordnen und zum anderen die sortierte Liste als Ausgabe zu übergeben.

**Zwei Typen von Sortieralgorithmus**

* Vergleichsbasiert
* Vergleiche von Elementen der Liste verwendet, um die Elemente entsprechend in die richtige Reihenfolge zu tauschen
* Nicht vergleichsbasierten Verfahren
* liegt der Fokus auf die Kondition der Eingabm

**Man kann sie in zwei weiter verfahren unterteilen**

* Stabilem Sortieren
* Die Reihenfolge der Datensätze gleichbleibt, deren Sortierschlüssel auch gleich sind



* Instabilem Sortieren
* In diesem Fall verschiedene Endergebnisse nach einem Sortiervorgang vorkommen, daher auch die Bezeichnung instabil




**Komplexität**

Die Effizienz der Sortieralgorithmen ist in den meisten Fällen vom Ausgangszustand abhängig – also wie ist die Datenmenge bei der Eingabe angeordnet. Dabei wird immer zwischen Best Case, Average Case und Worst Case unterschieden.



## Bubblesort

* Anwendung:
In der Praxis wird der Sortieralgorithmus kaum verwendet. Grund hierfür ist seine sehr lange Laufzeit, weswegen sich andere Sortierverfahren deutlich besser eignen. Beispielsweise der Mergesort oder der Heapsort sind bei einem Datensatz im über vierstelligem Bereich tausendmal schneller.


* Funktion:

Beim Bubblesort Algorithmus wird ein Array – also eine Eingabe-Liste – immer paarweise von links nach rechts in einer sogenannten Bubble-Phase durchlaufen. Man startet also mit der ersten Zahl und vergleicht diese dann mit ihrem direkten Nachbarn nach dem Sortierkriterium. Sollten beide Elemente nicht in der richtigen Reihenfolge sein, werden sie ganz einfach miteinander vertauscht. Danach wird direkt das nächste Paar miteinander verglichen, bis die gesamte Liste einmal durchlaufen wurde. Die Phase wird so oft wiederholt, bis der gesamte Array vollständig sortiert ist.

1.	Phase
 
      [5] [1] [4] [9] [0] [8] [6]
 
      [1] [5] [4] [9] [0] [8] [6]
 
      [1] [4] [5] [9] [0] [8] [6]
 
      [1] [4] [5] [9] [0] [8] [6]
 
      [1] [4] [5] [0] [9] [8] [6]
 
      [1] [4] [5] [0] [8] [9] [6]
 
      [1] [4] [5] [0] [8] [6] [9]

2.	Phase
 
      [1] [4] [5] [0] [8] [6] [9]

      [1] [4] [5] [0] [8] [6] [9]

      [1] [4] [5] [0] [8] [6] [9]

      [1] [4] [0] [5] [8] [6] [9]
 
      [1] [4] [0] [5] [8] [6] [9]
 
      [1] [4] [0] [5] [6] [8] [9]
 
3.	Phase
 
      [1] [4] [0] [5] [6] [8] [9]
 
      [1] [4] [0] [5] [6] [8] [9]
 
      [1] [0] [4] [5] [6] [8] [9]
 
      [1] [0] [4] [5] [6] [8] [9]
 
      [1] [0] [4] [5] [6] [8] [9]


Die durchschnittliche/schlechteste Zeitkomplexität des Bubble-Sort-Algorithmus beträgt \\(O(n^2)\\), da wir so oft durch das Array gehen müssen, wie es Paare im bereitgestellten Array gibt. Daher kann es bessere Optionen geben, wenn die Zeit eine Rolle spielt. Schlechteste Zeitkomplexität: \\(O(n^2)\\). Durchschnittliche Zeitkomplexität: \\(O(n^2)\\).

```cpp
// Funktion zum Austauschen von zwei Elementen
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Bubble-Sort Algorithmus
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Tausche die benachbarten Elemente, wenn sie in der falschen Reihenfolge sind
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```

## Teile und Hersche Methode

Viele nützliche Algorithmen haben eine rekursive Struktur: Um ein gegebenes Problem zu lösen, rufen sie sich selbst (rekursiv) ein oder mehrere Male auf, um eng verwandte Teilprobleme zu behandeln. Diese Algorithmen folgen typischerweise der Divide-and-Conquer-Methode: Sie zerlegen das Problem in mehrere Teilprobleme, die dem Originalproblem ähnlich sind, aber kleiner sind, lösen die Teilprobleme rekursiv und kombinieren dann diese Lösungen, um eine Lösung für das ursprüngliche Problem zu erstellen.
In der Divide-and-Conquer-Methode, wenn das Problem klein genug ist (die Basisfall), lösen Sie es direkt, ohne rekursiv zu sein. Andernfalls (im rekursiven Fall) führen Sie drei charakteristische Schritte durch:
1. Teilen Sie das Problem in ein oder mehrere Teilprobleme auf, die kleinere Instanzen des gleichen Problems sind.
2. Bezwingen Sie die Teilprobleme, indem Sie sie rekursiv lösen.
3. Kombinieren Sie die Lösungen der Teilprobleme, um eine Lösung für das Originalproblem zu bilden.


## Quicksort

Der Quicksort-Algorithmus hat eine schlechteste Laufzeit von \\(O(n^2)\\) wenn die Eingabedaten schlecht sortiert sind. Aber in der Praxis ist Quicksort oft die beste Wahl, da die erwartete Laufzeit im Durchschnitt nur \\(O(n \log n)\\) beträgt.

Ein wichtiger Vorteil von Quicksort ist, dass er die Daten "an Ort und Stelle" sortieren kann, d.h. ohne zusätzlichen Speicher. Der Algorithmus teilt die Liste rekursiv in kleinere Teillisten auf, bis nur noch Listen mit einem Element übrig sind.

Der randomisierte Quicksort verbessert den normalen Quicksort, indem ein zufälliges Element als Trennelement ausgewählt wird. Dadurch hat er im Durchschnitt immer eine gute Laufzeit von \\(O(n \log n)\\) und weist keine extrem schlechten Fälle auf.

![](./img/quick.png) 

```cpp
// Funktion zur Aufteilung des Arrays und Bestimmung des Pivotelements
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // wähle das letzte Element als Pivotelement
    int i = low - 1; // Index des kleineren Elements
  
    for (int j = low; j <= high - 1; j++) {
        // Wenn das aktuelle Element kleiner oder gleich dem Pivotelement ist
        if (arr[j] <= pivot) {
            i++; // erhöhe den Index des kleineren Elements
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Quicksort Algorithmus
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // partitioniere das Array und erhalte den Pivotelementindex
        int pi = partition(arr, low, high);
        
        // Sortiere die beiden Teilarrays rekursiv
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```


# Suchalgorithmen

`Definition`
* Ein Suchalgorithmen ist ein Verfahren, bei dem Schritt für Schritt Daten innerhalb einer Datensammlung(Array) ausfindig gemacht werden

Wie beim Sortieralgorithmen gehört auch Suchalgorithmen zu den grundlegenden Methoden der Informatik.
Wie beim Sortieralgorithmen gibt es auch hier verschieden Arten von Sortieralgorithmen und für jede dieser Arten unterschiedliche Anwendung

* Wichtig zu Merken ist das die Komplexität der Laufzeit immer eine Rolle spielt dabei.


`Anwendung`
* Wie es der Name bereits verrät, werden mithilfe von Suchalgorithmen Daten, Listen oder Baumstrukturen durchsucht. Wann welcher Algorithmus verwendet wird, kannst Du den folgenden Abschnitten entnehmen.

`Arten von Suchalgorithmen`
* Einfache Suchalgorithmen
    * Sie werden meist abstrakt implementiert
    * Können für vielzahl von kleineren Problemen eingesetzt werden
    * Vorteil: Einfach
    * Nachteil: Meist relative lange Laufzeit
* Heuristische Suchalgorithmen
    * Genaure Information über die durchsuchende Menge (Verteilung der Daten)
    * Heuristik: Versteht man ein Vorgehen mit der Lösungsstrategien für ein Prolem schneller gefunden werden kann
* Weitere Suchverfahren (Nicht relevant für uns)
    *  Darunter zählen evolutionäre Algorithmen, Suchverfahren für Zeichenketten oder beispielsweise die Adversarial Search, die vor allem im Bereich der künstlichen Intelligenz eingesetzt wird.


`Beispiele`

## Lineare Suche
* Zu den einfachen Suchalgorithmen gehört die lineare oder auch sequentielle Suche. Sie wird in der Regel bei ungeordneten Arrays verwendet und eignet sich vor allem bei eher kleineren Datenmengen.
    - Ein einfaches Beispiel für eine lineare Suche: Durchsuche eine Datenmenge nach dem kleinsten oder größten Element. Dabei musst Du die Daten durchgehen und alle Elemente miteinander vergleichen. Dadurch steigt die benötigte Anzahl an Vergleichen ebenfalls linear an – was die lineare Suche meist nicht besonders schnell macht.

* Iteration durch ein Menge von Elementen einer nach dem anderen
* Laufzeit Komplexität: O(n)

* Nachteile: 
    - Langsam für große Mengen von Daten
* Vorteil: 
    - Schnell für kleine Mengen von Daten
    - Muss nicht Sortiert werden
    - Sehr gut bei Daten die nicht zufällig verstreut sind

`Pseudocode`
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
Funktion lineareSuche(Array arr, Zielwert target)
    für jeden Index i von 0 bis zur Länge von arr - 1
        falls arr[i] gleich target ist
            gib i zurück // Element gefunden, gibt den Index zurück
    gib -1 zurück // Element nicht gefunden
Ende Funktion
```

`Linear Search in Javascript`
```js
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      return i; // Element gefunden, gibt den Index zurück
    }
  }
  return -1; // Element nicht gefunden
}

// Beispiel
const array = [1, 2, 3, 4, 5];
const targetElement = 3;

const result = linearSearch(array, targetElement);

if (result !== -1) {
  console.log(`Element ${targetElement} gefunden an Index ${result}.`);
} else {
  console.log(`Element ${targetElement} nicht gefunden.`);
}
```



## Binäre Suche
* Eine effektivere Variante ist die binäre Suche. Die Voraussetzung bei einer binären Suche ist allerdings, dass die Datenmenge vorher sortiert wurde. Bei der binären Suche wird nach dem "Teile-und-Herrsche-Prinzip" vorgegangen.

* Mittleres Element suchen und mit gesuchtem Element vergleichen

    * Ist es kleiner, suche in der rechten Hälfte weiter

    * Ist es größer, suche in der linken Hälfte

* "Neue" Datenmenge erneut halbieren und das gesuchte Element mit dem mittleren Element vergleichen

* Das ganze so lange weiter durchführen, bis das gesuchte Element gefunden wurde
<table><tbody><tr><td><strong>Suchalgorithmen</strong></td><td><strong>Vorteile</strong></td><td><strong>Nachteile</strong></td></tr><tr><td rowspan="3" style="width: 33.3333%;">Lineare Suche</td><td>Einfach zu implementieren.</td><td rowspan="3" style="width: 33.3333%;">Dauert bei großen Datenmengen sehr lange.</td></tr><tr><td>Kann auch in nicht sortierten Datenmengen verwendet werden.</td></tr><tr><td>Sortierte Daten bleiben sortiert, auch wenn ein neues Element eingefügt wird.</td></tr><tr><td rowspan="2" style="width: 33.3333%;"><a data-studyset-id="19463031" data-summary-id="71293597"  rel="nofollow" target="_blank">Binäre Suche</a></td><td>Eignet sich auch bei etwas größeren Datenmengen.</td><td rowspan="2" style="width: 33.3333%;">Die binäre Suche funktioniert nur in sortierten Datenmengen. Sollen neue Elemente eingefügt werden, müssen die Daten zunächst neu sortiert werden. </td></tr><tr><td>Eignet sich besonders gut für bereits sortierte, kleine Datensätze.</td></tr><tr><td>Interpolationssuche</td><td>Ist als Modifizierung der binären Suche schneller als diese, da durch die dynamische Wahl der Trennung meist weniger Werte durchsucht werden müssen.</td><td>Funktioniert ebenfalls nur in sortierten Datenmengen.</td></tr></tbody></table>


* Funktioniert durch das Teile und Hersche Verfahren
* Laufzeit Komplexität: O(Log n)
* Vorteil:
    - Schneller als Linear Search
    - Gut für große Mengen von Daten (Wörterbuch)
* Nachteil:
    - Muss sortiert sein
* Geht Iterrativ und mit Recursive Funktion



`Pseudocode`

```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
Funktion binaereSuche(Array arr, Zielwert target)
    links = 0
    rechts = Länge von arr - 1

    während links <= rechts
        mitte = (links + rechts) / 2

        falls arr[mitte] gleich target ist
            gib mitte zurück // Element gefunden, gibt den Index zurück
        sonst wenn arr[mitte] kleiner als target ist
            setze links = mitte + 1 // Suche in der rechten Hälfte
        sonst
            setze rechts = mitte - 1 // Suche in der linken Hälfte

    gib -1 zurück // Element nicht gefunden
Ende Funktion
```

`Binary Search in Javascript`

```js
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid; // Element gefunden, gibt den Index zurück
    } else if (arr[mid] < target) {
      left = mid + 1; // Suche in der rechten Hälfte
    } else {
      right = mid - 1; // Suche in der linken Hälfte
    }
  }

  return -1; // Element nicht gefunden
}

// Beispiel
const array = [1, 2, 3, 4, 5];
const targetElement = 3;

const result = binarySearch(array, targetElement);

if (result !== -1) {
  console.log(`Element ${targetElement} gefunden an Index ${result}.`);
} else {
  console.log(`Element ${targetElement} nicht gefunden.`);
}
```

### Übung

Gegeben sei ein Array von ganzen Zahlen `nums` und eine ganze Zahl `target`. Schreibe eine Funktion `countPairsWithSumLessThanTarget(nums: number[], target: number): number`, um die Anzahl der Paare `(i, j)` zu zählen, bei denen `nums[i] + nums[j] < target` gilt.

### Beispiel

Input: nums = [-1,1,2,3,1], target = 2

Output: 3

Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

