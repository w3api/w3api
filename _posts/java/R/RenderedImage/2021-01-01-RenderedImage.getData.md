---
title: RenderedImage.getData()
permalink: Java/RenderedImage/getData
date: 2021-01-11
key: Java.R.RenderedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RenderedImage.metodos valor="getData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Raster getData()
Raster getData(Rectangle rect)
~~~

## Parámetros
* **Rectangle rect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle rect" %}

## Clase Padre
[RenderedImage](/Java/RenderedImage/)

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
