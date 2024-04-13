---
title: ChronoLocalDateTime.minus()
permalink: /Java/ChronoLocalDateTime/minus/
date: 2021-01-11
key: Java.C.ChronoLocalDateTime
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDateTime<D> minus(long amountToSubtract, TemporalUnit unit)
default ChronoLocalDateTime<D> minus(TemporalAmount amount)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToSubtract" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amount" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
