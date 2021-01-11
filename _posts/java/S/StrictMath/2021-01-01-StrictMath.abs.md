---
title: StrictMath.abs()
permalink: Java/StrictMath/abs
date: 2021-01-11
key: JavaJava.S.StrictMath
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="abs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static double abs(double a)
public static float abs(float a)
public static int abs(int a)
public static long abs(long a)
~~~

## Parámetros
* **float a**,  {% include w3api/param_description.html metodo=_dato parametro="float a" %}
* **double a**,  {% include w3api/param_description.html metodo=_dato parametro="double a" %}
* **long a**,  {% include w3api/param_description.html metodo=_dato parametro="long a" %}
* **int a**,  {% include w3api/param_description.html metodo=_dato parametro="int a" %}

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
