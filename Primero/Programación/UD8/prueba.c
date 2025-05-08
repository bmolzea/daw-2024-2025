#include <stdio.h>
#include <string.h>

#define MAX_PALABRAS 100
#define MAX_LONGITUD 100

int main() {
    char palabras[MAX_PALABRAS][MAX_LONGITUD];
    int contador = 0;

    printf("Introduce palabras (escribe 'fin' para terminar):\n");

    while (contador < MAX_PALABRAS) {
        scanf("%s", palabras[contador]);
        if (strcmp(palabras[contador], "fin") == 0) {
            break;
        }
        contador++;
    }

    if (contador == 0) {
        printf("No se introdujeron palabras.\n");
        return 0;
    }

    char *palabraMayor = palabras[0];
    for (int i = 1; i < contador; i++) {
        if (strlen(palabras[i]) > strlen(palabraMayor)) {
            palabraMayor = palabras[i];
        }
    }

    printf("La palabra más larga es: %s\n", palabraMayor);

    return 0;
}
