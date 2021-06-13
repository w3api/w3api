---
title: DataBufferFloat.DataBufferFloat()
permalink: /Java/DataBufferFloat/DataBufferFloat/
date: 2021-01-11
key: Java.D.DataBufferFloat
category: Java
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
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **float[][] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="float[][] dataArray" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_dato parametro="int numBanks" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] offsets" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **float[] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="float[] dataArray" %}

## Clase Padre
[DataBufferFloat](/Java/DataBufferFloat/)

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
