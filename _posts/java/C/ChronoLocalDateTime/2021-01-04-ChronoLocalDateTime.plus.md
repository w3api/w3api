---
title: ChronoLocalDateTime.plus()
permalink: Java/ChronoLocalDateTime/plus
date: 2021-01-04
key: JavaJava.C.ChronoLocalDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="plus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoLocalDateTime<D> plus(long amountToAdd, TemporalUnit unit)
default ChronoLocalDateTime<D> plus(TemporalAmount amount)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **long amountToAdd**,  {% include w3api/param_description.html metodo=_data parametro="long amountToAdd" %}
* **TemporalAmount amount**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAmount amount" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
