---
title: ImageWriterSpi.canEncodeImage()
permalink: Java/ImageWriterSpi/canEncodeImage
date: 2021-01-04
key: JavaJava.I.ImageWriterSpi
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriterSpi.metodos valor="canEncodeImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean canEncodeImage(RenderedImage im)
public abstract boolean canEncodeImage(ImageTypeSpecifier type)
~~~

## Parámetros
* **ImageTypeSpecifier type**,  {% include w3api/param_description.html metodo=_data parametro="ImageTypeSpecifier type" %}
* **RenderedImage im**,  {% include w3api/param_description.html metodo=_data parametro="RenderedImage im" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageWriterSpi](/Java/ImageWriterSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageWriterSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
