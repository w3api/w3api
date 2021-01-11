---
title: DataBufferByte.DataBufferByte()
permalink: Java/DataBufferByte/DataBufferByte
date: 2021-01-11
key: JavaJava.D.DataBufferByte
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferByte.constructores valor="DataBufferByte" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferByte(byte[][] dataArray, int size)
public DataBufferByte(byte[][] dataArray, int size, int[] offsets)
public DataBufferByte(byte[] dataArray, int size)
public DataBufferByte(byte[] dataArray, int size, int offset)
public DataBufferByte(int size)
public DataBufferByte(int size, int numBanks)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **byte[] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] dataArray" %}
* **byte[][] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="byte[][] dataArray" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] offsets" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_dato parametro="int numBanks" %}

## Clase Padre
[DataBufferByte](/Java/DataBufferByte/)

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
