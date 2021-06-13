---
title: SimpleTimeZone.setStartRule()
permalink: /Java/SimpleTimeZone/setStartRule/
date: 2021-01-11
key: Java.S.SimpleTimeZone
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTimeZone.metodos valor="setStartRule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setStartRule(int startMonth, int startDay, int startTime)
public void setStartRule(int startMonth, int startDay, int startDayOfWeek, int startTime)
public void setStartRule(int startMonth, int startDay, int startDayOfWeek, int startTime, boolean after)
~~~

## Parámetros
* **boolean after**,  {% include w3api/param_description.html metodo=_dato parametro="boolean after" %}
* **int startDay**,  {% include w3api/param_description.html metodo=_dato parametro="int startDay" %}
* **int startDayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int startDayOfWeek" %}
* **int startTime**,  {% include w3api/param_description.html metodo=_dato parametro="int startTime" %}
* **int startMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int startMonth" %}

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
