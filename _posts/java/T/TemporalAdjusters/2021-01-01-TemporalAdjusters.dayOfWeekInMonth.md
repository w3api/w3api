---
title: TemporalAdjusters.dayOfWeekInMonth()
permalink: /Java/TemporalAdjusters/dayOfWeekInMonth/
date: 2021-01-11
key: Java.T.TemporalAdjusters
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalAdjusters.metodos valor="dayOfWeekInMonth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TemporalAdjuster dayOfWeekInMonth(int ordinal, DayOfWeek dayOfWeek)
~~~

## Parámetros
* **DayOfWeek dayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="DayOfWeek dayOfWeek" %}
* **int ordinal**,  {% include w3api/param_description.html metodo=_dato parametro="int ordinal" %}

## Clase Padre
[TemporalAdjusters](/Java/TemporalAdjusters/)

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
