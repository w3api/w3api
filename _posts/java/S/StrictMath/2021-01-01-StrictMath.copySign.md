---
title: StrictMath.copySign()
permalink: /Java/StrictMath/copySign/
date: 2021-01-11
key: Java.S.StrictMath
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="copySign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static double copySign(double magnitude, double sign)
public static float copySign(float magnitude, float sign)
~~~

## Parámetros
* **float sign**,  {% include w3api/param_description.html metodo=_dato parametro="float sign" %}
* **float magnitude**,  {% include w3api/param_description.html metodo=_dato parametro="float magnitude" %}
* **double sign**,  {% include w3api/param_description.html metodo=_dato parametro="double sign" %}
* **double magnitude**,  {% include w3api/param_description.html metodo=_dato parametro="double magnitude" %}

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
