---
title: BufferedImage.getSubimage()
permalink: /Java/BufferedImage/getSubimage/
date: 2021-01-11
key: Java.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="getSubimage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage getSubimage(int x, int y, int w, int h)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[RasterFormatException](/Java/RasterFormatException/)

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

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
