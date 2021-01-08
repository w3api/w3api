---
title: SimpleTimeZone.getOffset()
permalink: Java/SimpleTimeZone/getOffset
date: 2021-01-04
key: JavaJava.S.SimpleTimeZone
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTimeZone.metodos valor="getOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getOffset(int era, int year, int month, int day, int dayOfWeek, int millis)
public int getOffset(long date)
~~~

## Parámetros
* **int millis**,  {% include w3api/param_description.html metodo=_data parametro="int millis" %}
* **int dayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfWeek" %}
* **int era**,  {% include w3api/param_description.html metodo=_data parametro="int era" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int day**,  {% include w3api/param_description.html metodo=_data parametro="int day" %}
* **long date**,  {% include w3api/param_description.html metodo=_data parametro="long date" %}

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
