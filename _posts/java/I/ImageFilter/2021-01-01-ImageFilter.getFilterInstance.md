---
title: ImageFilter.getFilterInstance()
permalink: /Java/ImageFilter/getFilterInstance/
date: 2021-01-11
key: Java.I.ImageFilter
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageFilter.metodos valor="getFilterInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageFilter getFilterInstance(ImageConsumer ic)
~~~

## Parámetros
* **ImageConsumer ic**,  {% include w3api/param_description.html metodo=_dato parametro="ImageConsumer ic" %}

## Clase Padre
[ImageFilter](/Java/ImageFilter/)

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
