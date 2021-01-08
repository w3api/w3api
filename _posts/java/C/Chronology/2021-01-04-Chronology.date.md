---
title: Chronology.date()
permalink: Java/Chronology/date
date: 2021-01-04
key: JavaJava.C.Chronology
category: java
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
* **Era era**,  {% include w3api/param_description.html metodo=_data parametro="Era era" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAccessor temporal" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [DateTimeException](/Java/DateTimeException/)

## Clase Padre
[Chronology](/Java/Chronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Chronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
