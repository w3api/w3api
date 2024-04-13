---
title: DataBufferInt.DataBufferInt()
permalink: /Java/DataBufferInt/DataBufferInt/
date: 2021-01-11
key: Java.D.DataBufferInt
category: Java
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
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **int[][] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[][] dataArray" %}
* **int[] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] dataArray" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_dato parametro="int numBanks" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] offsets" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Clase Padre
[DataBufferInt](/Java/DataBufferInt/)

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
