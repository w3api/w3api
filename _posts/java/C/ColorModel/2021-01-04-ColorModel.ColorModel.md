---
title: ColorModel.ColorModel()
permalink: Java/ColorModel/ColorModel
date: 2021-01-04
key: JavaJava.C.ColorModel
category: java
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
* **int pixel_bits**,  {% include w3api/param_description.html metodo=_data parametro="int pixel_bits" %}
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **int transparency**,  {% include w3api/param_description.html metodo=_data parametro="int transparency" %}
* **ColorSpace cspace**,  {% include w3api/param_description.html metodo=_data parametro="ColorSpace cspace" %}
* **boolean hasAlpha**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasAlpha" %}
* **int[] bits**,  {% include w3api/param_description.html metodo=_data parametro="int[] bits" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ColorModel](/Java/ColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
