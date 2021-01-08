---
title: ColorConvertOp.createCompatibleDestImage()
permalink: Java/ColorConvertOp/createCompatibleDestImage
date: 2021-01-04
key: JavaJava.C.ColorConvertOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorConvertOp.metodos valor="createCompatibleDestImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage createCompatibleDestImage(BufferedImage src, ColorModel destCM)
~~~

## Parámetros
* **ColorModel destCM**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel destCM" %}
* **BufferedImage src**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage src" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ColorConvertOp](/Java/ColorConvertOp/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ColorConvertOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
