---
title: DataBufferInt.DataBufferInt()
permalink: Java/DataBufferInt/DataBufferInt
date: 2021-01-04
key: JavaJava.D.DataBufferInt
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferInt.constructores valor="DataBufferInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferInt(int size)
public DataBufferInt(int[][] dataArray, int size)
public DataBufferInt(int[][] dataArray, int size, int[] offsets)
public DataBufferInt(int[] dataArray, int size)
public DataBufferInt(int[] dataArray, int size, int offset)
public DataBufferInt(int size, int numBanks)
~~~

## Parámetros
* **int[] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] dataArray" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **int[][] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="int[][] dataArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}

## Clase Padre
[DataBufferInt](/Java/DataBufferInt/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBufferInt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
