---
title: SimpleTimeZone.setEndRule()
permalink: /Java/SimpleTimeZone/setEndRule/
date: 2021-01-11
key: Java.S.SimpleTimeZone
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTimeZone.metodos valor="setEndRule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setEndRule(int endMonth, int endDay, int endTime)
public void setEndRule(int endMonth, int endDay, int endDayOfWeek, int endTime)
public void setEndRule(int endMonth, int endDay, int endDayOfWeek, int endTime, boolean after)
~~~

## Parámetros
* **int endMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int endMonth" %}
* **int endDay**,  {% include w3api/param_description.html metodo=_dato parametro="int endDay" %}
* **boolean after**,  {% include w3api/param_description.html metodo=_dato parametro="boolean after" %}
* **int endDayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int endDayOfWeek" %}
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
