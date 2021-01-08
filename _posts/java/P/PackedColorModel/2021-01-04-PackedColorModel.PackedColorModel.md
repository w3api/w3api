---
title: PackedColorModel.PackedColorModel()
permalink: Java/PackedColorModel/PackedColorModel
date: 2021-01-04
key: JavaJava.P.PackedColorModel
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
* **int[] colorMaskArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] colorMaskArray" %}
* **ColorSpace space**,  {% include w3api/param_description.html metodo=_data parametro="ColorSpace space" %}
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **int rmask**,  {% include w3api/param_description.html metodo=_data parametro="int rmask" %}
* **int amask**,  {% include w3api/param_description.html metodo=_data parametro="int amask" %}
* **int gmask**,  {% include w3api/param_description.html metodo=_data parametro="int gmask" %}
* **int trans**,  {% include w3api/param_description.html metodo=_data parametro="int trans" %}
* **int bmask**,  {% include w3api/param_description.html metodo=_data parametro="int bmask" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}
* **int alphaMask**,  {% include w3api/param_description.html metodo=_data parametro="int alphaMask" %}

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
{%- for _ldc in site.data.Java.P.PackedColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
