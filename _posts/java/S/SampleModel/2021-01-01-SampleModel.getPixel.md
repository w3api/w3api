---
title: SampleModel.getPixel()
permalink: Java/SampleModel/getPixel
date: 2021-01-11
key: JavaJava.S.SampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.metodos valor="getPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] getPixel(int x, int y, double[] dArray, DataBuffer data)
public float[] getPixel(int x, int y, float[] fArray, DataBuffer data)
public int[] getPixel(int x, int y, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] iArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] iArray" %}
* **double[] dArray**,  {% include w3api/param_description.html metodo=_dato parametro="double[] dArray" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **float[] fArray**,  {% include w3api/param_description.html metodo=_dato parametro="float[] fArray" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SampleModel](/Java/SampleModel/)

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
