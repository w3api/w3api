---
title: StrictMath.nextAfter()
permalink: /Java/StrictMath/nextAfter/
date: 2021-01-11
key: Java.S.StrictMath
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="nextAfter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static double nextAfter(double start, double direction)
public static float nextAfter(float start, double direction)
~~~

## Parámetros
* **double direction**,  {% include w3api/param_description.html metodo=_dato parametro="double direction" %}
* **double start**,  {% include w3api/param_description.html metodo=_dato parametro="double start" %}
* **float start**,  {% include w3api/param_description.html metodo=_dato parametro="float start" %}

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
