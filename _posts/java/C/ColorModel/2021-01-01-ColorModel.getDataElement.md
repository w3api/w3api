---
title: ColorModel.getDataElement()
permalink: /Java/ColorModel/getDataElement/
date: 2021-01-11
key: Java.C.ColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getDataElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getDataElement(float[] normComponents, int normOffset)
public int getDataElement(int[] components, int offset)
~~~

## Parámetros
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_dato parametro="float[] normComponents" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int normOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int normOffset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

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
