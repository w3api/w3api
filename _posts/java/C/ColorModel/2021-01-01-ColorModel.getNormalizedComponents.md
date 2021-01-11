---
title: ColorModel.getNormalizedComponents()
permalink: Java/ColorModel/getNormalizedComponents
date: 2021-01-11
key: JavaJava.C.ColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getNormalizedComponents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public float[] getNormalizedComponents(int[] components, int offset, float[] normComponents, int normOffset)
public float[] getNormalizedComponents(Object pixel, float[] normComponents, int normOffset)
~~~

## Parámetros
* **int[] components**,  {% include w3api/param_description.html metodo=_dato parametro="int[] components" %}
* **Object pixel**,  {% include w3api/param_description.html metodo=_dato parametro="Object pixel" %}
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_dato parametro="float[] normComponents" %}
* **int normOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int normOffset" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

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
