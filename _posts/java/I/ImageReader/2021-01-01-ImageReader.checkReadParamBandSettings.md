---
title: ImageReader.checkReadParamBandSettings()
permalink: /Java/ImageReader/checkReadParamBandSettings/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="checkReadParamBandSettings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static void checkReadParamBandSettings(ImageReadParam param, int numSrcBands, int numDstBands)
~~~

## Parámetros
* **int numDstBands**,  {% include w3api/param_description.html metodo=_dato parametro="int numDstBands" %}
* **int numSrcBands**,  {% include w3api/param_description.html metodo=_dato parametro="int numSrcBands" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReadParam param" %}

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
