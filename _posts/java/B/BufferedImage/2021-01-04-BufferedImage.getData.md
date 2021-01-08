---
title: BufferedImage.getData()
permalink: Java/BufferedImage/getData
date: 2021-01-04
key: JavaJava.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="getData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Raster getData()
public Raster getData(Rectangle rect)
~~~

## Parámetros
* **Rectangle rect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle rect" %}

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
