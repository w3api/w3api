---
title: IsoChronology.epochSecond()
permalink: Java/IsoChronology/epochSecond
date: 2021-01-04
key: JavaJava.I.IsoChronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="epochSecond" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long epochSecond(int prolepticYear, int month, int dayOfMonth, int hour, int minute, int second, ZoneOffset zoneOffset)
~~~

## Parámetros
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **ZoneOffset zoneOffset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset zoneOffset" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[IsoChronology](/Java/IsoChronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IsoChronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
