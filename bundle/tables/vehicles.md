---
type: Table
title: Catálogo de veículos
description: Tabela de modelos com marca, categoria SUV híbrido, sedã, picape e motorização.
tags: [veiculos, catalogo, suv, hibrido]
status: draft
---

# Schema

| Campo | Tipo | Significado |
|---|---|---|
| vehicle_id | string | Identificador ilustrativo do veículo |
| marca | string | Nome comercial da marca |
| modelo | string | Nome do modelo |
| categoria | string | SUV, sedã, picape ou motocicleta |
| motorizacao | string | Híbrida, combustão ou não especificada |

# Registros fictícios

| vehicle_id | marca | modelo | categoria | motorizacao |
|---|---|---|---|---|
| V001 | GWM | Haval H6 | SUV | híbrida |
| V002 | Honda | Civic | sedã | não especificada |
| V003 | Toyota | Corolla | sedã | não especificada |
| V004 | Toyota | Hilux | picape | não especificada |
| V005 | Honda | CB 500 | motocicleta | combustão |

# Relacionamentos

- A classificação é explicada na [regra de SUV híbrido](/rules/hybrid-classification.md).
- Os preços ilustrativos estão em [preços](/tables/prices.md).
- Os fabricantes são descritos em [fabricantes](/tables/manufacturers.md).

# Observação

Não se deve inferir motorização dos veículos marcados como "não especificada".
