---
title: ImageReader.computeRegions()
permalink: Java/ImageReader/computeRegions
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="computeRegions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static void computeRegions(ImageReadParam param, int srcWidth, int srcHeight, BufferedImage image, Rectangle srcRegion, Rectangle destRegion)
~~~

## Parámetros
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReadParam param" %}
* **int srcHeight**,  {% include w3api/param_description.html metodo=_dato parametro="int srcHeight" %}
* **BufferedImage image**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage image" %}
* **int srcWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int srcWidth" %}
* **Rectangle destRegion**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle destRegion" %}
* **Rectangle srcRegion**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle srcRegion" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
