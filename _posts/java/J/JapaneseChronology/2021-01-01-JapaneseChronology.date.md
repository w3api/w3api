---
title: JapaneseChronology.date()
permalink: /Java/JapaneseChronology/date/
date: 2021-01-11
key: Java.J.JapaneseChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JapaneseChronology.metodos valor="date" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JapaneseDate date(int prolepticYear, int month, int dayOfMonth)
public JapaneseDate date(Era era, int yearOfEra, int month, int dayOfMonth)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[JapaneseChronology](/Java/JapaneseChronology/)

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
