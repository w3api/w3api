---
title: ImageTranscoder.convertStreamMetadata()
permalink: /Java/ImageTranscoder/convertStreamMetadata/
date: 2021-01-11
key: Java.I.ImageTranscoder
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTranscoder.metodos valor="convertStreamMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
IIOMetadata convertStreamMetadata(IIOMetadata inData, ImageWriteParam param)
~~~

## Parámetros
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **IIOMetadata inData**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata inData" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTranscoder](/Java/ImageTranscoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
