using System;
using System.Collections.Generic;
using System.Linq;

class Ahorcado
{
    static void Main()
    {
        string[] palabras = { "programacion", "computadora", "algoritmo", "variable", "desarrollador" };
        Random rand = new Random();
        string palabraSecreta = palabras[rand.Next(palabras.Length)];
        HashSet<char> letrasAdivinadas = new HashSet<char>();
        int intentosRestantes = 6;

        Console.WriteLine("🕹 Bienvenido al juego del Ahorcado!");
        Console.WriteLine($"La palabra tiene {palabraSecreta.Length} letras.");

        while (intentosRestantes > 0)
        {
            MostrarEstado(palabraSecreta, letrasAdivinadas);
            Console.Write("Ingresa una letra: ");
            string entrada = Console.ReadLine().ToLower();

            if (string.IsNullOrWhiteSpace(entrada) || entrada.Length != 1 || !char.IsLetter(entrada[0]))
            {
                Console.WriteLine("Por favor, ingresa una sola letra válida.");
                continue;
            }

            char letra = entrada[0];

            if (letrasAdivinadas.Contains(letra))
            {
                Console.WriteLine("Ya intentaste con esa letra.");
                continue;
            }

            letrasAdivinadas.Add(letra);

            if (palabraSecreta.Contains(letra))
            {
                Console.WriteLine("¡Bien hecho! La letra está en la palabra.");
            }
            else
            {
                intentosRestantes--;
                Console.WriteLine($"Letra incorrecta. Te quedan {intentosRestantes} intentos.");
            }

            if (PalabraAdivinada(palabraSecreta, letrasAdivinadas))
            {
                Console.WriteLine($"\n🎉 ¡Felicidades! Adivinaste la palabra: {palabraSecreta}");
                return;
            }
        }

        Console.WriteLine($"\n💀 Has perdido. La palabra era: {palabraSecreta}");
    }

    static void MostrarEstado(string palabra, HashSet<char> letras)
    {
        foreach (char c in palabra)
        {
            if (letras.Contains(c))
                Console.Write(c + " ");
            else
                Console.Write("_ ");
        }
        Console.WriteLine();
    }

    static bool PalabraAdivinada(string palabra, HashSet<char> letras)
    {
        return palabra.All(letras.Contains);
    }
}
