---
title: IsoChronology.dateYearDay()
permalink: Java/IsoChronology/dateYearDay
date: 2021-01-04
key: JavaJava.I.IsoChronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="dateYearDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate dateYearDay(int prolepticYear, int dayOfYear)
public LocalDate dateYearDay(Era era, int yearOfEra, int dayOfYear)
~~~

## Parámetros
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfYear" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}
* **Era era**,  {% include w3api/param_description.html metodo=_data parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}

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
