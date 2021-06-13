---
title: Chronology.dateYearDay()
permalink: /Java/Chronology/dateYearDay/
date: 2021-01-11
key: Java.C.Chronology
category: Java
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
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfYear" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}

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
