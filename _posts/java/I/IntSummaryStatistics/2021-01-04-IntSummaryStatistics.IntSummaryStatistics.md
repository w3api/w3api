---
title: IntSummaryStatistics.IntSummaryStatistics()
permalink: Java/IntSummaryStatistics/IntSummaryStatistics
date: 2021-01-04
key: JavaJava.I.IntSummaryStatistics
category: java
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
* **int min**,  {% include w3api/param_description.html metodo=_data parametro="int min" %}
* **int max**,  {% include w3api/param_description.html metodo=_data parametro="int max" %}
* **long count**,  {% include w3api/param_description.html metodo=_data parametro="long count" %}
* **long sum**,  {% include w3api/param_description.html metodo=_data parametro="long sum" %}

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
{%- for _ldc in site.data.Java.I.IntSummaryStatistics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
