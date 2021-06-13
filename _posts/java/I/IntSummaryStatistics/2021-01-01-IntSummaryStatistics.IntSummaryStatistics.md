---
title: IntSummaryStatistics.IntSummaryStatistics()
permalink: /Java/IntSummaryStatistics/IntSummaryStatistics/
date: 2021-01-11
key: Java.I.IntSummaryStatistics
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntSummaryStatistics.constructores valor="IntSummaryStatistics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IntSummaryStatistics()
public IntSummaryStatistics(long count, int min, int max, long sum) throws IllegalArgumentException
~~~

## Parámetros
* **long sum**,  {% include w3api/param_description.html metodo=_dato parametro="long sum" %}
* **int min**,  {% include w3api/param_description.html metodo=_dato parametro="int min" %}
* **long count**,  {% include w3api/param_description.html metodo=_dato parametro="long count" %}
* **int max**,  {% include w3api/param_description.html metodo=_dato parametro="int max" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IntSummaryStatistics](/Java/IntSummaryStatistics/)

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
