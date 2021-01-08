---
title: LocalDate.ofYearDay()
permalink: Java/LocalDate/ofYearDay
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="ofYearDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDate ofYearDay(int year, int dayOfYear)
~~~

## Parámetros
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int dayOfYear**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfYear" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
