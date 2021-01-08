---
title: DataBufferFloat.DataBufferFloat()
permalink: Java/DataBufferFloat/DataBufferFloat
date: 2021-01-04
key: JavaJava.D.DataBufferFloat
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferFloat.constructores valor="DataBufferFloat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferFloat(float[][] dataArray, int size)
public DataBufferFloat(float[][] dataArray, int size, int[] offsets)
public DataBufferFloat(float[] dataArray, int size)
public DataBufferFloat(float[] dataArray, int size, int offset)
public DataBufferFloat(int size)
public DataBufferFloat(int size, int numBanks)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **float[][] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="float[][] dataArray" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **float[] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="float[] dataArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}

## Clase Padre
[DataBufferFloat](/Java/DataBufferFloat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBufferFloat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
