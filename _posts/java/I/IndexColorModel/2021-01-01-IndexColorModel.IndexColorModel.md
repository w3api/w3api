---
title: IndexColorModel.IndexColorModel()
permalink: /Java/IndexColorModel/IndexColorModel/
date: 2021-01-11
key: Java.I.IndexColorModel
category: Java
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
* **byte[] r**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] r" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_dato parametro="int transferType" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **BigInteger validBits**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger validBits" %}
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **int[] cmap**,  {% include w3api/param_description.html metodo=_dato parametro="int[] cmap" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}
* **byte[] a**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] a" %}
* **boolean hasalpha**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasalpha" %}
* **byte[] g**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] g" %}
* **int trans**,  {% include w3api/param_description.html metodo=_dato parametro="int trans" %}
* **byte[] cmap**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] cmap" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
