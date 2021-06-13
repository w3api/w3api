---
title: SimpleTimeZone.SimpleTimeZone()
permalink: /Java/SimpleTimeZone/SimpleTimeZone/
date: 2021-01-11
key: Java.S.SimpleTimeZone
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTimeZone.constructores valor="SimpleTimeZone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleTimeZone(int rawOffset, String ID)
public SimpleTimeZone(int rawOffset, String ID, int startMonth, int startDay, int startDayOfWeek, int startTime, int endMonth, int endDay, int endDayOfWeek, int endTime)
public SimpleTimeZone(int rawOffset, String ID, int startMonth, int startDay, int startDayOfWeek, int startTime, int endMonth, int endDay, int endDayOfWeek, int endTime, int dstSavings)
public SimpleTimeZone(int rawOffset, String ID, int startMonth, int startDay, int startDayOfWeek, int startTime, int startTimeMode, int endMonth, int endDay, int endDayOfWeek, int endTime, int endTimeMode, int dstSavings)
~~~

## Parámetros
* **int endMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int endMonth" %}
* **int endDay**,  {% include w3api/param_description.html metodo=_dato parametro="int endDay" %}
* **int startDay**,  {% include w3api/param_description.html metodo=_dato parametro="int startDay" %}
* **int endDayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int endDayOfWeek" %}
* **int rawOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int rawOffset" %}
* **String ID**,  {% include w3api/param_description.html metodo=_dato parametro="String ID" %}
* **int startDayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int startDayOfWeek" %}
* **int startTime**,  {% include w3api/param_description.html metodo=_dato parametro="int startTime" %}
* **int dstSavings**,  {% include w3api/param_description.html metodo=_dato parametro="int dstSavings" %}
* **int startTimeMode**,  {% include w3api/param_description.html metodo=_dato parametro="int startTimeMode" %}
* **int startMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int startMonth" %}
* **int endTimeMode**,  {% include w3api/param_description.html metodo=_dato parametro="int endTimeMode" %}
* **int endTime**,  {% include w3api/param_description.html metodo=_dato parametro="int endTime" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SimpleTimeZone](/Java/SimpleTimeZone/)

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
