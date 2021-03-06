---
title: MinguoChronology.dateYearDay()
permalink: /Java/MinguoChronology/dateYearDay/
date: 2021-01-11
key: Java.M.MinguoChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoChronology.metodos valor="dateYearDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MinguoDate dateYearDay(int prolepticYear, int dayOfYear)
public MinguoDate dateYearDay(Era era, int yearOfEra, int dayOfYear)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfYear" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[MinguoChronology](/Java/MinguoChronology/)

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
