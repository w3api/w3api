---
title: ChronoLocalDate.minus()
permalink: Java/ChronoLocalDate/minus
date: 2021-01-11
key: JavaJava.C.ChronoLocalDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDate minus(long amountToSubtract, TemporalUnit unit)
default ChronoLocalDate minus(TemporalAmount amount)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToSubtract" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amount" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDate](/Java/ChronoLocalDate/)

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
