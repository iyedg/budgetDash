# ERD

## Liste d'entités

### GBO

* Organisation
* Mission
* Programme
* Sous-programme
* Objectif
* Indicateur
* Unité opérationelle

### Dépenses

[Lien](http://127.0.0.1:8000/Gestion_du_Budget_par_Objectif/budget_classification/#depenses)

## Relations

```mermaid
graph LR
    m[Mission] -- "1..n | 1..n" --> or[Organisation]
    m -- "1..n | 1..1" --> p[Programme]
    p -- "1..n | 1..1" --> sp[Sous-programme]
    p -- "1..n | 1..1" --> ob[Objectif]
    sp -- "1..n | 1..1" --> ob[Objectif]
    ob -- "1..n | 1..1" --> i[Indicateur]
    p -- "1..n | 0..n هياكل متدخلة" --> or
```
