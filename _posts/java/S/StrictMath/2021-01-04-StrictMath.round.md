---
title: StrictMath.round()
permalink: Java/StrictMath/round
date: 2021-01-04
key: JavaJava.S.StrictMath
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrictMath.metodos valor="round" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static long round(double a)
public static int round(float a)
~~~

## Parámetros
* **float a**,  {% include w3api/param_description.html metodo=_data parametro="float a" %}
* **double a**,  {% include w3api/param_description.html metodo=_data parametro="double a" %}

## Clase Padre
[StrictMath](/Java/StrictMath/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StrictMath.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
