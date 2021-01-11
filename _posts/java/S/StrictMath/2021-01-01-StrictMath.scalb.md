---
title: StrictMath.scalb()
permalink: Java/StrictMath/scalb
date: 2021-01-11
key: JavaJava.S.StrictMath
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="scalb" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static double scalb(double d, int scaleFactor)
public static float scalb(float f, int scaleFactor)
~~~

## Parámetros
* **int scaleFactor**,  {% include w3api/param_description.html metodo=_dato parametro="int scaleFactor" %}
* **float f**,  {% include w3api/param_description.html metodo=_dato parametro="float f" %}
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}

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
