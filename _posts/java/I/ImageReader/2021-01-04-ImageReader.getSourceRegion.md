---
title: ImageReader.getSourceRegion()
permalink: Java/ImageReader/getSourceRegion
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getSourceRegion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static Rectangle getSourceRegion(ImageReadParam param, int srcWidth, int srcHeight)
~~~

## Parámetros
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageReadParam param" %}
* **int srcHeight**,  {% include w3api/param_description.html metodo=_data parametro="int srcHeight" %}
* **int srcWidth**,  {% include w3api/param_description.html metodo=_data parametro="int srcWidth" %}

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
