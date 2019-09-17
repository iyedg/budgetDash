# Budget classification under LOB2019

## Circulaire

### *Article 1:* Expenses classification

* نفقات التأجير
* نفقات التسيير
* نفقات التدخلات
* نفقات الاستثمار
* نفقات العمليات المالية
* نفقات التمويل
* النفقات الطارئة وغير الموزعة

### *Article 2:* Allocation

## Organization

```mermaid
graph TD
    mission["La mission = ministère(s)"] --> responsables[Responsables]
    responsables --> p1[Programme 1]
    responsables --> p2[Programme 2]
    responsables --> p3[Programme n]
    p1 --> o1["Objectif(s)"]
    p2 --> o2["Objectif(s)"]
    p3 --> o3["Objectif(s)"]
    o2 --> i11[Indicateur 1]
    o2 --> i12[Indicateur 2]
    p1 --> pap1[PAP]
    p2 --> pap2[PAP]
    p3 --> pap3[PAP]
    pap1 --> rap1[RAP]
    pap2 --> rap2[RAP]
    pap3 --> rap3[RAP]
```

### *Articles 4 - 5*: Code

$$
\overbrace{*}^{\text{Code du programme}} \underbrace{*}_{\text{Code du sous-programme}} \overbrace{***}^{\text{Code de l'article}}
$$

e.g.

!!! bug
    un meilleur exemple

$$
\overbrace{9}^{\text{Code du programme}} \underbrace{1}_{\text{Code du sous-programme}} \overbrace{100}^{\text{Code de l'article}}
$$

* $9$ est le code du programme.
* $8$ est le code du sous-programme.
* $100$ est le code de l'article "المنح المخولة للسلط العمومية"

### Glossaire

* **RDP**
:   Responsable de programme
* **PAP:**
:   Projet Annuel de Performance: un engagement sur les résultats
* **RAP:**
:   Rapport Annuel de Performance: un compte rendu des résultats
