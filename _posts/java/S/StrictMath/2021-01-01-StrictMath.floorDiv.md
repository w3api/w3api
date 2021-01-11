---
title: StrictMath.floorDiv()
permalink: Java/StrictMath/floorDiv
date: 2021-01-11
key: JavaJava.S.StrictMath
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="floorDiv" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int floorDiv(int x, int y)
public static long floorDiv(long x, int y)
public static long floorDiv(long x, long y)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **long x**,  {% include w3api/param_description.html metodo=_dato parametro="long x" %}
* **long y**,  {% include w3api/param_description.html metodo=_dato parametro="long y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[StrictMath](/Java/StrictMath/)

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
