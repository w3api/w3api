---
title: WeekFields.of()
permalink: /Java/WeekFields/of/
date: 2021-01-11
key: Java.W.WeekFields
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WeekFields.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static WeekFields of(DayOfWeek firstDayOfWeek, int minimalDaysInFirstWeek)
public static WeekFields of(Locale locale)
~~~

## Parámetros
* **int minimalDaysInFirstWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int minimalDaysInFirstWeek" %}
* **DayOfWeek firstDayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="DayOfWeek firstDayOfWeek" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[WeekFields](/Java/WeekFields/)

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
