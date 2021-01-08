---
title: ColorModel.getRed()
permalink: Java/ColorModel/getRed
date: 2021-01-04
key: JavaJava.C.ColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.metodos valor="getRed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getRed(int pixel)
public int getRed(Object inData)
~~~

## Parámetros
* **Object inData**,  {% include w3api/param_description.html metodo=_data parametro="Object inData" %}
* **int pixel**,  {% include w3api/param_description.html metodo=_data parametro="int pixel" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/)

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
