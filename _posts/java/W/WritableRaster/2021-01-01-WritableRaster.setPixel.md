---
title: WritableRaster.setPixel()
permalink: Java/WritableRaster/setPixel
date: 2021-01-11
key: JavaJava.W.WritableRaster
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableRaster.metodos valor="setPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPixel(int x, int y, double[] dArray)
public void setPixel(int x, int y, float[] fArray)
public void setPixel(int x, int y, int[] iArray)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] iArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] iArray" %}
* **double[] dArray**,  {% include w3api/param_description.html metodo=_dato parametro="double[] dArray" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **float[] fArray**,  {% include w3api/param_description.html metodo=_dato parametro="float[] fArray" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[WritableRaster](/Java/WritableRaster/)

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
