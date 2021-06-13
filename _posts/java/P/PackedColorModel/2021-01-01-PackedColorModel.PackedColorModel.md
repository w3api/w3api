---
title: PackedColorModel.PackedColorModel()
permalink: /Java/PackedColorModel/PackedColorModel/
date: 2021-01-11
key: Java.P.PackedColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PackedColorModel.constructores valor="PackedColorModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PackedColorModel(ColorSpace space, int bits, int[] colorMaskArray, int alphaMask, boolean isAlphaPremultiplied, int trans, int transferType)
public PackedColorModel(ColorSpace space, int bits, int rmask, int gmask, int bmask, int amask, boolean isAlphaPremultiplied, int trans, int transferType)
~~~

## Parámetros
* **int[] colorMaskArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] colorMaskArray" %}
* **int amask**,  {% include w3api/param_description.html metodo=_dato parametro="int amask" %}
* **int bmask**,  {% include w3api/param_description.html metodo=_dato parametro="int bmask" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_dato parametro="int transferType" %}
* **int rmask**,  {% include w3api/param_description.html metodo=_dato parametro="int rmask" %}
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **int alphaMask**,  {% include w3api/param_description.html metodo=_dato parametro="int alphaMask" %}
* **int trans**,  {% include w3api/param_description.html metodo=_dato parametro="int trans" %}
* **ColorSpace space**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace space" %}
* **int gmask**,  {% include w3api/param_description.html metodo=_dato parametro="int gmask" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PackedColorModel](/Java/PackedColorModel/)

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
