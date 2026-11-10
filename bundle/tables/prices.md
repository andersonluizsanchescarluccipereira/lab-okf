---
type: Table
title: Preços fictícios do catálogo
description: Valores ilustrativos para exemplificar o cálculo do preço médio de veículos.
tags: [preco, valores, tabela, veiculos]
status: draft
---

# Schema

| Campo | Tipo | Significado |
|---|---|---|
| vehicle_id | string | Chave do veículo |
| preco_brl | decimal | Valor em reais, inteiramente fictício |

# Dados artificiais

| vehicle_id | preco_brl |
|---|---:|
| V001 | 100000 |
| V002 | 80000 |
| V003 | 90000 |

A média destes três preços é R$ 90.000,00 (apenas exemplo matemático).
A definição formal está na [métrica de preço médio](/metrics/average-price.md).
A chave está na [tabela de veículos](/tables/vehicles.md).
