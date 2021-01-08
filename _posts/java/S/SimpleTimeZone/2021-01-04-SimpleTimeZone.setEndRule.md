---
title: SimpleTimeZone.setEndRule()
permalink: Java/SimpleTimeZone/setEndRule
date: 2021-01-04
key: JavaJava.S.SimpleTimeZone
category: java
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
* **int endMonth**,  {% include w3api/param_description.html metodo=_data parametro="int endMonth" %}
* **int endTime**,  {% include w3api/param_description.html metodo=_data parametro="int endTime" %}
* **int endDay**,  {% include w3api/param_description.html metodo=_data parametro="int endDay" %}
* **int endDayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int endDayOfWeek" %}
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
