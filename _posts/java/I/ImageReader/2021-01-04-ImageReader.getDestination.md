---
title: ImageReader.getDestination()
permalink: Java/ImageReader/getDestination
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
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
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageReadParam param" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **Iterator&lt;ImageTypeSpecifier&gt; imageTypes**,  {% include w3api/param_description.html metodo=_data parametro="Iterator<ImageTypeSpecifier> imageTypes" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

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
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
