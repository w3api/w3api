---
title: ValueRange.of()
permalink: Java/ValueRange/of
date: 2021-01-11
key: JavaJava.V.ValueRange
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueRange.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ValueRange of(long min, long max)
public static ValueRange of(long min, long maxSmallest, long maxLargest)
public static ValueRange of(long minSmallest, long minLargest, long maxSmallest, long maxLargest)
~~~

## Parámetros
* **long min**,  {% include w3api/param_description.html metodo=_dato parametro="long min" %}
* **long minSmallest**,  {% include w3api/param_description.html metodo=_dato parametro="long minSmallest" %}
* **long maxLargest**,  {% include w3api/param_description.html metodo=_dato parametro="long maxLargest" %}
* **long maxSmallest**,  {% include w3api/param_description.html metodo=_dato parametro="long maxSmallest" %}
* **long minLargest**,  {% include w3api/param_description.html metodo=_dato parametro="long minLargest" %}
* **long max**,  {% include w3api/param_description.html metodo=_dato parametro="long max" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ValueRange](/Java/ValueRange/)

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
