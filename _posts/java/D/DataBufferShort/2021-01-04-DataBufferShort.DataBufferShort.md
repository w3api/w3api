---
title: DataBufferShort.DataBufferShort()
permalink: Java/DataBufferShort/DataBufferShort
date: 2021-01-04
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
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **short[] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="short[] dataArray" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **short[][] dataArray**,  {% include w3api/param_description.html metodo=_data parametro="short[][] dataArray" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}

## Clase Padre
[DataBufferShort](/Java/DataBufferShort/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBufferShort.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
