---
title: Chronology.epochSecond()
permalink: Java/Chronology/epochSecond
date: 2021-01-04
key: JavaJava.C.Chronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="epochSecond" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default long epochSecond(int prolepticYear, int month, int dayOfMonth, int hour, int minute, int second, ZoneOffset zoneOffset)
default long epochSecond(Era era, int yearOfEra, int month, int dayOfMonth, int hour, int minute, int second, ZoneOffset zoneOffset)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_data parametro="Era era" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}
* **ZoneOffset zoneOffset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset zoneOffset" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

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
