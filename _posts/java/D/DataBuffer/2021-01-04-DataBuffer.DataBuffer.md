---
title: DataBuffer.DataBuffer()
permalink: Java/DataBuffer/DataBuffer
date: 2021-01-04
key: JavaJava.D.DataBuffer
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBuffer.constructores valor="DataBuffer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected DataBuffer(int dataType, int size)
protected DataBuffer(int dataType, int size, int numBanks)
protected DataBuffer(int dataType, int size, int numBanks, int offset)
protected DataBuffer(int dataType, int size, int numBanks, int[] offsets)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int numBanks**,  {% include w3api/param_description.html metodo=_data parametro="int numBanks" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[DataBuffer](/Java/DataBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
