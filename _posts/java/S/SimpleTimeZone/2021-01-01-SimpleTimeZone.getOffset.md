---
title: SimpleTimeZone.getOffset()
permalink: /Java/SimpleTimeZone/getOffset/
date: 2021-01-11
key: Java.S.SimpleTimeZone
category: Java
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
* **int day**,  {% include w3api/param_description.html metodo=_dato parametro="int day" %}
* **int dayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfWeek" %}
* **int millis**,  {% include w3api/param_description.html metodo=_dato parametro="int millis" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **long date**,  {% include w3api/param_description.html metodo=_dato parametro="long date" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}
* **int era**,  {% include w3api/param_description.html metodo=_dato parametro="int era" %}

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
