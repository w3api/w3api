---
title: Chronology.dateYearDay()
permalink: Java/Chronology/dateYearDay
date: 2021-01-04
key: JavaJava.C.Chronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="dateYearDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoLocalDate dateYearDay(int prolepticYear, int dayOfYear)
default ChronoLocalDate dateYearDay(Era era, int yearOfEra, int dayOfYear)
~~~

## Parámetros
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfYear" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}
* **Era era**,  {% include w3api/param_description.html metodo=_data parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}

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
