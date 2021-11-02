---
title: dataclasses
permalink: /Python/dataclasses
date: 2021-01-01
key: Python.D.dataclasses
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.D.dataclasses.description }}

## Funciones
* [asdict](/Python/dataclasses/asdict/)
* [astuple](/Python/dataclasses/astuple/)
* [dataclass](/Python/dataclasses/dataclass/)
* [field](/Python/dataclasses/field/)
* [fields](/Python/dataclasses/fields/)
* [is_dataclass](/Python/dataclasses/is_dataclass/)
* [make_dataclass](/Python/dataclasses/make_dataclass/)
* [replace](/Python/dataclasses/replace/)

## Clases
* [Field](/Python/dataclasses/Field/)

## Excepciones
* [FrozenInstanceError](/Python/dataclasses/FrozenInstanceError/)

## Constantes
* [KW_ONLY](/Python/dataclasses/KW_ONLY/)
* [MISSING](/Python/dataclasses/MISSING/)

## Ejemplo
~~~python
{{ site.data.Python.D.dataclasses.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.D.dataclasses.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
