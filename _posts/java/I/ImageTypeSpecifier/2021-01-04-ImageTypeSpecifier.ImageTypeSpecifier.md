---
title: ImageTypeSpecifier.ImageTypeSpecifier()
permalink: Java/ImageTypeSpecifier/ImageTypeSpecifier
date: 2021-01-04
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
* **SampleModel sampleModel**,  {% include w3api/param_description.html metodo=_data parametro="SampleModel sampleModel" %}
* **ColorModel colorModel**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel colorModel" %}
* **RenderedImage image**,  {% include w3api/param_description.html metodo=_data parametro="RenderedImage image" %}

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
{%- for _ldc in site.data.Java.I.ImageTypeSpecifier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
