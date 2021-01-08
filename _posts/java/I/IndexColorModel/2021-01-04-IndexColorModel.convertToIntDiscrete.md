---
title: IndexColorModel.convertToIntDiscrete()
permalink: Java/IndexColorModel/convertToIntDiscrete
date: 2021-01-04
key: JavaJava.I.IndexColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexColorModel.metodos valor="convertToIntDiscrete" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage convertToIntDiscrete(Raster raster, boolean forceARGB)
~~~

## Parámetros
* **Raster raster**,  {% include w3api/param_description.html metodo=_data parametro="Raster raster" %}
* **boolean forceARGB**,  {% include w3api/param_description.html metodo=_data parametro="boolean forceARGB" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IndexColorModel](/Java/IndexColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IndexColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
