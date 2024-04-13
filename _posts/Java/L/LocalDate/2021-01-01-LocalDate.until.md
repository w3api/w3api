---
title: LocalDate.until()
permalink: /Java/LocalDate/until/
date: 2021-01-11
key: Java.L.LocalDate
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="until" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Period until(ChronoLocalDate endDateExclusive)
public long until(Temporal endExclusive, TemporalUnit unit)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **Temporal endExclusive**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal endExclusive" %}
* **ChronoLocalDate endDateExclusive**,  {% include w3api/param_description.html metodo=_dato parametro="ChronoLocalDate endDateExclusive" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
