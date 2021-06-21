---
title: ColorModel.ColorModel()
permalink: /Java/ColorModel/ColorModel/
date: 2021-01-11
key: Java.C.ColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorModel.constructores valor="ColorModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ColorModel(int bits)
protected ColorModel(int pixel_bits, int[] bits, ColorSpace cspace, boolean hasAlpha, boolean isAlphaPremultiplied, int transparency, int transferType)
~~~

## Parámetros
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_dato parametro="int transferType" %}
* **ColorSpace cspace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace cspace" %}
* **int pixel_bits**,  {% include w3api/param_description.html metodo=_dato parametro="int pixel_bits" %}
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **boolean hasAlpha**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasAlpha" %}
* **int transparency**,  {% include w3api/param_description.html metodo=_dato parametro="int transparency" %}
* **int[] bits**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
