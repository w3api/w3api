---
title: ColorSpace.toRGB()
permalink: /Java/ColorSpace/toRGB/
date: 2021-01-11
key: Java.C.ColorSpace
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorSpace.metodos valor="toRGB" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract float[] toRGB(float[] colorvalue)
~~~

## Parámetros
* **float[] colorvalue**,  {% include w3api/param_description.html metodo=_dato parametro="float[] colorvalue" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[ColorSpace](/Java/ColorSpace/)

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
