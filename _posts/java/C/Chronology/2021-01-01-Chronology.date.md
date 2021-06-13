---
title: Chronology.date()
permalink: /Java/Chronology/date/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="date" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoLocalDate date(int prolepticYear, int month, int dayOfMonth)
default ChronoLocalDate date(Era era, int yearOfEra, int month, int dayOfMonth)
ChronoLocalDate date(TemporalAccessor temporal)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[Chronology](/Java/Chronology/)

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
