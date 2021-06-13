---
title: LongSummaryStatistics.LongSummaryStatistics()
permalink: /Java/LongSummaryStatistics/LongSummaryStatistics/
date: 2021-01-11
key: Java.L.LongSummaryStatistics
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongSummaryStatistics.constructores valor="LongSummaryStatistics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LongSummaryStatistics()
public LongSummaryStatistics(long count, long min, long max, long sum) throws IllegalArgumentException
~~~

## Parámetros
* **long min**,  {% include w3api/param_description.html metodo=_dato parametro="long min" %}
* **long sum**,  {% include w3api/param_description.html metodo=_dato parametro="long sum" %}
* **long count**,  {% include w3api/param_description.html metodo=_dato parametro="long count" %}
* **long max**,  {% include w3api/param_description.html metodo=_dato parametro="long max" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LongSummaryStatistics](/Java/LongSummaryStatistics/)

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
