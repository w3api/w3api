---
title: DataBufferShort.DataBufferShort()
permalink: Java/DataBufferShort/DataBufferShort
date: 2021-01-11
key: JavaJava.D.DataBufferShort
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBufferShort.constructores valor="DataBufferShort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataBufferShort(int size)
public DataBufferShort(int size, int numBanks)
public DataBufferShort(short[][] dataArray, int size)
public DataBufferShort(short[][] dataArray, int size, int[] offsets)
public DataBufferShort(short[] dataArray, int size)
public DataBufferShort(short[] dataArray, int size, int offset)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_dato parametro="int numBanks" %}
* **short[][] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="short[][] dataArray" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] offsets" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **short[] dataArray**,  {% include w3api/param_description.html metodo=_dato parametro="short[] dataArray" %}

## Clase Padre
[DataBufferShort](/Java/DataBufferShort/)

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
