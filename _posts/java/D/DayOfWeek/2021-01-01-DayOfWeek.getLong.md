---
title: DayOfWeek.getLong()
permalink: /Java/DayOfWeek/getLong/
date: 2021-01-11
key: Java.D.DayOfWeek
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DayOfWeek.metodos valor="getLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getLong(TemporalField field)
~~~

## Parámetros
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[DayOfWeek](/Java/DayOfWeek/)

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
