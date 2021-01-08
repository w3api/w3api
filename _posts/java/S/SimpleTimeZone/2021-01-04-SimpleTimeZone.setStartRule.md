---
title: SimpleTimeZone.setStartRule()
permalink: Java/SimpleTimeZone/setStartRule
date: 2021-01-04
key: JavaJava.S.SimpleTimeZone
category: java
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
* **int startMonth**,  {% include w3api/param_description.html metodo=_data parametro="int startMonth" %}
* **int startDayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int startDayOfWeek" %}
* **int startTime**,  {% include w3api/param_description.html metodo=_data parametro="int startTime" %}
* **int startDay**,  {% include w3api/param_description.html metodo=_data parametro="int startDay" %}
* **boolean after**,  {% include w3api/param_description.html metodo=_data parametro="boolean after" %}

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
