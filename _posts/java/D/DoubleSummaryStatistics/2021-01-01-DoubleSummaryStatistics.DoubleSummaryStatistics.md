---
title: DoubleSummaryStatistics.DoubleSummaryStatistics()
permalink: /Java/DoubleSummaryStatistics/DoubleSummaryStatistics/
date: 2021-01-11
key: Java.D.DoubleSummaryStatistics
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleSummaryStatistics.constructores valor="DoubleSummaryStatistics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DoubleSummaryStatistics()
public DoubleSummaryStatistics(long count, double min, double max, double sum) throws IllegalArgumentException
~~~

## Parámetros
* **double min**,  {% include w3api/param_description.html metodo=_dato parametro="double min" %}
* **double sum**,  {% include w3api/param_description.html metodo=_dato parametro="double sum" %}
* **double max**,  {% include w3api/param_description.html metodo=_dato parametro="double max" %}
* **long count**,  {% include w3api/param_description.html metodo=_dato parametro="long count" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DoubleSummaryStatistics](/Java/DoubleSummaryStatistics/)

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
