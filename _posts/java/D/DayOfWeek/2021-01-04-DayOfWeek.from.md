---
title: DayOfWeek.from()
permalink: Java/DayOfWeek/from
date: 2021-01-04
key: JavaJava.D.DayOfWeek
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DayOfWeek.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DayOfWeek from(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAccessor temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[DayOfWeek](/Java/DayOfWeek/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DayOfWeek.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
