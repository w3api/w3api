---
title: ImageReader.getDestination()
permalink: /Java/ImageReader/getDestination/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getDestination" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static BufferedImage getDestination(ImageReadParam param, Iterator<ImageTypeSpecifier> imageTypes, int width, int height) throws IIOException
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReadParam param" %}
* **Iterator&lt;ImageTypeSpecifier&gt; imageTypes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<ImageTypeSpecifier> imageTypes" %}

## Excepciones
[IIOException](/Java/IIOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReader](/Java/ImageReader/)

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
