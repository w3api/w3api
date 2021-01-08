---
title: IndexColorModel.IndexColorModel()
permalink: Java/IndexColorModel/IndexColorModel
date: 2021-01-04
key: JavaJava.I.IndexColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexColorModel.constructores valor="IndexColorModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IndexColorModel(int bits, int size, byte[] r, byte[] g, byte[] b)
public IndexColorModel(int bits, int size, byte[] r, byte[] g, byte[] b, byte[] a)
public IndexColorModel(int bits, int size, byte[] r, byte[] g, byte[] b, int trans)
public IndexColorModel(int bits, int size, byte[] cmap, int start, boolean hasalpha)
public IndexColorModel(int bits, int size, byte[] cmap, int start, boolean hasalpha, int trans)
public IndexColorModel(int bits, int size, int[] cmap, int start, boolean hasalpha, int trans, int transferType)
public IndexColorModel(int bits, int size, int[] cmap, int start, int transferType, BigInteger validBits)
~~~

## Parámetros
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **byte[] cmap**,  {% include w3api/param_description.html metodo=_data parametro="byte[] cmap" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int[] cmap**,  {% include w3api/param_description.html metodo=_data parametro="int[] cmap" %}
* **byte[] r**,  {% include w3api/param_description.html metodo=_data parametro="byte[] r" %}
* **int trans**,  {% include w3api/param_description.html metodo=_data parametro="int trans" %}
* **BigInteger validBits**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger validBits" %}
* **boolean hasalpha**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasalpha" %}
* **byte[] a**,  {% include w3api/param_description.html metodo=_data parametro="byte[] a" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **byte[] g**,  {% include w3api/param_description.html metodo=_data parametro="byte[] g" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IndexColorModel](/Java/IndexColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IndexColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
