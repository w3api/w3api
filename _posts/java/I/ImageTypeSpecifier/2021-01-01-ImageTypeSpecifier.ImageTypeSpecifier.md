---
title: ImageTypeSpecifier.ImageTypeSpecifier()
permalink: Java/ImageTypeSpecifier/ImageTypeSpecifier
date: 2021-01-11
key: JavaJava.I.ImageTypeSpecifier
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.constructores valor="ImageTypeSpecifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageTypeSpecifier(ColorModel colorModel, SampleModel sampleModel)
public ImageTypeSpecifier(RenderedImage image)
~~~

## Parámetros
* **RenderedImage image**,  {% include w3api/param_description.html metodo=_dato parametro="RenderedImage image" %}
* **ColorModel colorModel**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel colorModel" %}
* **SampleModel sampleModel**,  {% include w3api/param_description.html metodo=_dato parametro="SampleModel sampleModel" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTypeSpecifier](/Java/ImageTypeSpecifier/)

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
