---
title: ImageTypeSpecifier.createGrayscale()
permalink: Java/ImageTypeSpecifier/createGrayscale
date: 2021-01-04
key: JavaJava.I.ImageTypeSpecifier
category: java
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
* **boolean isSigned**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSigned" %}
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTypeSpecifier](/Java/ImageTypeSpecifier/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageTypeSpecifier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
