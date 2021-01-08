---
title: ImageTranscoder.convertImageMetadata()
permalink: Java/ImageTranscoder/convertImageMetadata
date: 2021-01-04
key: JavaJava.I.ImageTranscoder
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTranscoder.metodos valor="convertImageMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
IIOMetadata convertImageMetadata(IIOMetadata inData, ImageTypeSpecifier imageType, ImageWriteParam param)
~~~

## Parámetros
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_data parametro="ImageTypeSpecifier imageType" %}
* **IIOMetadata inData**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata inData" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriteParam param" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTranscoder](/Java/ImageTranscoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageTranscoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
