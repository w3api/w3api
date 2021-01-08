---
title: ImageReader.computeRegions()
permalink: Java/ImageReader/computeRegions
date: 2021-01-04
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
* **int srcHeight**,  {% include w3api/param_description.html metodo=_data parametro="int srcHeight" %}
* **Rectangle destRegion**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle destRegion" %}
* **Rectangle srcRegion**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle srcRegion" %}
* **BufferedImage image**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage image" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageReadParam param" %}
* **int srcWidth**,  {% include w3api/param_description.html metodo=_data parametro="int srcWidth" %}

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
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
