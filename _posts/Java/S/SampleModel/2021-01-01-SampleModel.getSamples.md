---
title: SampleModel.getSamples()
permalink: /Java/SampleModel/getSamples/
date: 2021-01-11
key: Java.S.SampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.metodos valor="getSamples" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] getSamples(int x, int y, int w, int h, int b, double[] dArray, DataBuffer data)
public float[] getSamples(int x, int y, int w, int h, int b, float[] fArray, DataBuffer data)
public int[] getSamples(int x, int y, int w, int h, int b, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] iArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] iArray" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **double[] dArray**,  {% include w3api/param_description.html metodo=_dato parametro="double[] dArray" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **float[] fArray**,  {% include w3api/param_description.html metodo=_dato parametro="float[] fArray" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

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
