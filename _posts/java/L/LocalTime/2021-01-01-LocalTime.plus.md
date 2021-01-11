---
title: LocalTime.plus()
permalink: Java/LocalTime/plus
date: 2021-01-11
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="plus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalTime plus(long amountToAdd, TemporalUnit unit)
public LocalTime plus(TemporalAmount amountToAdd)
~~~

## Parámetros
* **long amountToAdd**,  {% include w3api/param_description.html metodo=_dato parametro="long amountToAdd" %}
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **TemporalAmount amountToAdd**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amountToAdd" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[LocalTime](/Java/LocalTime/)

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
