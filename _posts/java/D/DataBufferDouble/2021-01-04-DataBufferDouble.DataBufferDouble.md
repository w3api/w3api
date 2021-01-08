---
title: DataBufferDouble.DataBufferDouble()
permalink: Java/DataBufferDouble/DataBufferDouble
date: 2021-01-04
key: JavaJava.D.DataBufferDouble
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferDouble.constructores valor="DataBufferDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferDouble(double[][] dataArray, int size)
public DataBufferDouble(double[][] dataArray, int size, int[] offsets)
public DataBufferDouble(double[] dataArray, int size)
public DataBufferDouble(double[] dataArray, int size, int offset)
public DataBufferDouble(int size)
public DataBufferDouble(int size, int numBanks)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **double[] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="double[] dataArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}
* **double[][] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="double[][] dataArray" %}

## Clase Padre
[DataBufferDouble](/Java/DataBufferDouble/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBufferDouble.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
