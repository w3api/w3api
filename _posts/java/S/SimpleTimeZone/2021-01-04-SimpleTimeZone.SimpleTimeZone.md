---
title: SimpleTimeZone.SimpleTimeZone()
permalink: Java/SimpleTimeZone/SimpleTimeZone
date: 2021-01-04
key: JavaJava.S.SimpleTimeZone
category: java
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
* **int rawOffset**,  {% include w3api/param_description.html metodo=_data parametro="int rawOffset" %}
* **int endTimeMode**,  {% include w3api/param_description.html metodo=_data parametro="int endTimeMode" %}
* **int endMonth**,  {% include w3api/param_description.html metodo=_data parametro="int endMonth" %}
* **int startTimeMode**,  {% include w3api/param_description.html metodo=_data parametro="int startTimeMode" %}
* **int startMonth**,  {% include w3api/param_description.html metodo=_data parametro="int startMonth" %}
* **int startDayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int startDayOfWeek" %}
* **String ID**,  {% include w3api/param_description.html metodo=_data parametro="String ID" %}
* **int dstSavings**,  {% include w3api/param_description.html metodo=_data parametro="int dstSavings" %}
* **int endTime**,  {% include w3api/param_description.html metodo=_data parametro="int endTime" %}
* **int startTime**,  {% include w3api/param_description.html metodo=_data parametro="int startTime" %}
* **int endDay**,  {% include w3api/param_description.html metodo=_data parametro="int endDay" %}
* **int endDayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int endDayOfWeek" %}
* **int startDay**,  {% include w3api/param_description.html metodo=_data parametro="int startDay" %}

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
{%- for _ldc in site.data.Java.S.SimpleTimeZone.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
