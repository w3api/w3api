---
title: StrictMath.ulp()
permalink: /Java/StrictMath/ulp/
date: 2021-01-11
key: Java.S.StrictMath
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="ulp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static double ulp(double d)
public static float ulp(float f)
~~~

## Parámetros
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
