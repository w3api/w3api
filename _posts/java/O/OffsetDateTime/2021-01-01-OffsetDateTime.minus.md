---
title: OffsetDateTime.minus()
permalink: /Java/OffsetDateTime/minus/
date: 2021-01-11
key: Java.O.OffsetDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetDateTime.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OffsetDateTime minus(long amountToSubtract, TemporalUnit unit)
public OffsetDateTime minus(TemporalAmount amountToSubtract)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToSubtract" %}
* **TemporalAmount amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amountToSubtract" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[OffsetDateTime](/Java/OffsetDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
