---
title: ImageTypeSpecifier.createGrayscale()
permalink: /Java/ImageTypeSpecifier/createGrayscale/
date: 2021-01-11
key: Java.I.ImageTypeSpecifier
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="createGrayscale" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ImageTypeSpecifier createGrayscale(int bits, int dataType, boolean isSigned)
public static ImageTypeSpecifier createGrayscale(int bits, int dataType, boolean isSigned, boolean isAlphaPremultiplied)
~~~

## Parámetros
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **boolean isSigned**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSigned" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTypeSpecifier](/Java/ImageTypeSpecifier/)

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
