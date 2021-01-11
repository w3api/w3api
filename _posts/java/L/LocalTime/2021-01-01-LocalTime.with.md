---
title: LocalTime.with()
permalink: Java/LocalTime/with
date: 2021-01-11
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="with" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalTime with(TemporalAdjuster adjuster)
public LocalTime with(TemporalField field, long newValue)
~~~

## Parámetros
* **long newValue**,  {% include w3api/param_description.html metodo=_dato parametro="long newValue" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}
* **TemporalAdjuster adjuster**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAdjuster adjuster" %}

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
