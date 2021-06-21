---
title: IsoChronology.dateYearDay()
permalink: /Java/IsoChronology/dateYearDay/
date: 2021-01-11
key: Java.I.IsoChronology
category: Java
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
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfYear" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[IsoChronology](/Java/IsoChronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
