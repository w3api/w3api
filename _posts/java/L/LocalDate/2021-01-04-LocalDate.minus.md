---
title: LocalDate.minus()
permalink: Java/LocalDate/minus
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate minus(long amountToSubtract, TemporalUnit unit)
public LocalDate minus(TemporalAmount amountToSubtract)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}
* **TemporalAmount amountToSubtract**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAmount amountToSubtract" %}
* **long amountToSubtract**,  {% include w3api/param_description.html metodo=_data parametro="long amountToSubtract" %}

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
