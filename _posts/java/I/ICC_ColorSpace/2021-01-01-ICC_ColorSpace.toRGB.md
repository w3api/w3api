---
title: ICC_ColorSpace.toRGB()
permalink: /Java/ICC_ColorSpace/toRGB/
date: 2021-01-11
key: Java.I.ICC_ColorSpace
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_ColorSpace.metodos valor="toRGB" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public float[] toRGB(float[] colorvalue)
~~~

## Parámetros
* **float[] colorvalue**,  {% include w3api/param_description.html metodo=_dato parametro="float[] colorvalue" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[ICC_ColorSpace](/Java/ICC_ColorSpace/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
