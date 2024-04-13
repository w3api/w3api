---
title: ImageReader.getSourceRegion()
permalink: /Java/ImageReader/getSourceRegion/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
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
* **int srcHeight**,  {% include w3api/param_description.html metodo=_dato parametro="int srcHeight" %}
* **int srcWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int srcWidth" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReadParam param" %}

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
