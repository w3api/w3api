---
title: ColorModel.getNormalizedComponents()
permalink: Java/ColorModel/getNormalizedComponents
date: 2021-01-04
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
* **Object pixel**,  {% include w3api/param_description.html metodo=_data parametro="Object pixel" %}
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_data parametro="float[] normComponents" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_data parametro="int[] components" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int normOffset**,  {% include w3api/param_description.html metodo=_data parametro="int normOffset" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
