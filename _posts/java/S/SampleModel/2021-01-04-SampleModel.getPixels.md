---
title: SampleModel.getPixels()
permalink: Java/SampleModel/getPixels
date: 2021-01-04
key: JavaJava.S.SampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.metodos valor="getPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] getPixels(int x, int y, int w, int h, double[] dArray, DataBuffer data)
public float[] getPixels(int x, int y, int w, int h, float[] fArray, DataBuffer data)
public int[] getPixels(int x, int y, int w, int h, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **int[] iArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] iArray" %}
* **float[] fArray**,  {% include w3api/param_description.html metodo=_data parametro="float[] fArray" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_data parametro="DataBuffer data" %}
* **double[] dArray**,  {% include w3api/param_description.html metodo=_data parametro="double[] dArray" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.S.SampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
