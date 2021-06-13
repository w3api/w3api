---
title: ImageWriterSpi.canEncodeImage()
permalink: /Java/ImageWriterSpi/canEncodeImage/
date: 2021-01-11
key: Java.I.ImageWriterSpi
category: Java
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
* **RenderedImage im**,  {% include w3api/param_description.html metodo=_dato parametro="RenderedImage im" %}
* **ImageTypeSpecifier type**,  {% include w3api/param_description.html metodo=_dato parametro="ImageTypeSpecifier type" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
