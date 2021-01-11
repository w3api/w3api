---
title: ImageReader.processThumbnailUpdate()
permalink: Java/ImageReader/processThumbnailUpdate
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="processThumbnailUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processThumbnailUpdate(BufferedImage theThumbnail, int minX, int minY, int width, int height, int periodX, int periodY, int[] bands)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int minX**,  {% include w3api/param_description.html metodo=_dato parametro="int minX" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage theThumbnail" %}
* **int minY**,  {% include w3api/param_description.html metodo=_dato parametro="int minY" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_dato parametro="int periodY" %}
* **int[] bands**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bands" %}
* **int periodX**,  {% include w3api/param_description.html metodo=_dato parametro="int periodX" %}

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