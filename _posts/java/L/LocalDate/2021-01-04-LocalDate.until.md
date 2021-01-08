---
title: LocalDate.until()
permalink: Java/LocalDate/until
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
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
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **ChronoLocalDate endDateExclusive**,  {% include w3api/param_description.html metodo=_data parametro="ChronoLocalDate endDateExclusive" %}
* **Temporal endExclusive**,  {% include w3api/param_description.html metodo=_data parametro="Temporal endExclusive" %}

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
{%- for _ldc in site.data.Java.L.LocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
