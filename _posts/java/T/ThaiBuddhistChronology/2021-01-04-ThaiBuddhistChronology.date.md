---
title: ThaiBuddhistChronology.date()
permalink: Java/ThaiBuddhistChronology/date
date: 2021-01-04
key: JavaJava.T.ThaiBuddhistChronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThaiBuddhistChronology.metodos valor="date" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ThaiBuddhistDate date(int prolepticYear, int month, int dayOfMonth)
public ThaiBuddhistDate date(Era era, int yearOfEra, int month, int dayOfMonth)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_data parametro="Era era" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ThaiBuddhistChronology](/Java/ThaiBuddhistChronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThaiBuddhistChronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
