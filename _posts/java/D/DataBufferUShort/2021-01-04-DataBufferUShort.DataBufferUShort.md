---
title: DataBufferUShort.DataBufferUShort()
permalink: Java/DataBufferUShort/DataBufferUShort
date: 2021-01-04
key: JavaJava.D.DataBufferUShort
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferUShort.constructores valor="DataBufferUShort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferUShort(int size)
public DataBufferUShort(int size, int numBanks)
public DataBufferUShort(short[][] dataArray, int size)
public DataBufferUShort(short[][] dataArray, int size, int[] offsets)
public DataBufferUShort(short[] dataArray, int size)
public DataBufferUShort(short[] dataArray, int size, int offset)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **short[] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="short[] dataArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **short[][] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="short[][] dataArray" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}

## Clase Padre
[DataBufferUShort](/Java/DataBufferUShort/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBufferUShort.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
