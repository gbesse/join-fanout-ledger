# join-fanout-ledger

## Français

Expliquer pourquoi une jointure multiplie un montant métier.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m join_fanout_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Rejoue une jointure gauche réelle et explique, pour chaque ligne métier, le nombre de correspondances et le montant répété. Différent de sql-delta-reconcile : le témoin porte sur la multiplicité de la jointure elle-même.

### Limites

Égalité de clés textuelles avec sémantique NULL SQLite, une seule unité monétaire déclarée. Ni détection automatique du bon grain métier ni correction SQL imposée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Explain why a join multiplies a business amount.

Synthetic data; no network access or secret required.

```sh
python -m join_fanout_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Replays an actual left join and explains each business row matched count and repeated amount. Unlike sql-delta-reconcile, the witness concerns join multiplicity itself.

### Limits

Text-key equality with SQLite NULL semantics and one declared monetary unit. Does not infer correct business grain or impose a SQL rewrite.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Explicar por qué una unión multiplica un importe de negocio.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m join_fanout_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Reproduce una unión izquierda real y explica por fila el número de coincidencias y el importe repetido. A diferencia de sql-delta-reconcile, analiza la multiplicidad de la propia unión.

### Límites

Igualdad de claves textuales con semántica NULL SQLite y una unidad monetaria declarada. No deduce granularidad de negocio ni impone reescritura SQL.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/lang_select.html
