# Kapitel 4

# Rekursive Funktionen

Rekursive Funktionen sind Funktionen in der Informatik, die sich selbst aufrufen, um eine bestimmte Aufgabe zu lösen. Sie sind besonders nützlich, wenn eine Aufgabe in kleinere, ähnliche Teilaufgaben zerlegt werden kann. Hier sind einige Punkte, die man bei rekursiven Funktionen beachten sollte:

1. **Basisfall:** Eine rekursive Funktion muss einen Basisfall haben, der definiert, wann die Rekursion endet und die Funktion ohne weitere rekursive Aufrufe zurückkehrt.

2. **Fortsetzungsfall:** Die rekursive Funktion muss einen Fortsetzungsfall haben, der den rekursiven Aufruf enthält und das Problem in kleinere Teilaufgaben aufteilt.

3. **Konvergenz:** Die rekursive Funktion sollte sicherstellen, dass sie sich dem Basisfall nähert und nicht in einer Endlosschleife feststeckt.

4. **Speichern von Zwischenergebnissen:** Bei rekursiven Funktionen ist es wichtig zu überprüfen, ob Zwischenergebnisse gespeichert werden müssen, um unnötige Berechnungen zu vermeiden und die Effizienz zu verbessern.

5. **Stack Overflow vermeiden:** Rekursion führt dazu, dass Funktionen auf dem Stack gespeichert werden. Bei zu vielen rekursiven Aufrufen kann ein Stack Overflow auftreten, was bedeutet, dass der verfügbare Speicher für den Stack überschritten wurde.

6. **Testen und Debuggen:** Rekursive Funktionen können schwer zu verstehen und zu debuggen sein. Daher ist gründliches Testen und Debuggen unerlässlich, um sicherzustellen, dass die Funktion korrekt funktioniert.

## Beispiel in JavaScript

```javascript
// Beispiel einer rekursiven Funktion zur Berechnung der Fakultät einer Zahl
function factorial(n) {
    // Basisfall: Wenn n kleiner oder gleich 1 ist, ist die Fakultät 1
    if (n <= 1) {
        return 1;
    }
    // Fortsetzungsfall: n * factorial(n-1)
    else {
        return n * factorial(n - 1);
    }
}

// Test der rekursiven Funktion
console.log(factorial(5)); // Ausgabe: 120 (5! = 5*4*3*2*1 = 120)
```
### Beispiel 1: Summe der ersten n natürlichen Zahlen
```javascript
// Rekursive Funktion zur Berechnung der Summe der ersten n natürlichen Zahlen
function sumOfNaturals(n) {
    // Basisfall: Wenn n gleich 1 ist, ist die Summe 1
    if (n === 1) {
        return 1;
    }
    // Fortsetzungsfall: n + sumOfNaturals(n-1)
    else {
        return n + sumOfNaturals(n - 1);
    }
}

// Test der rekursiven Funktion
console.log(sumOfNaturals(5)); // Ausgabe: 15 (1 + 2 + 3 + 4 + 5 = 15)
```

### Beispiel 2: Implementation in Java

```java
// Rekursive Funktion zur Berechnung der n-ten Fibonacci-Zahl
public class Fibonacci {
    public static int fibonacci(int n) {
        // Basisfälle: Wenn n kleiner oder gleich 1 ist, ist die Fibonacci-Zahl n
        if (n <= 1) {
            return n;
        }
        // Fortsetzungsfall: fibonacci(n-1) + fibonacci(n-2)
        else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }

    // Test der rekursiven Funktion
    public static void main(String[] args) {
        System.out.println(fibonacci(6)); // Ausgabe: 8 (die 6. Fibonacci-Zahl ist 8)
    }
}

```
