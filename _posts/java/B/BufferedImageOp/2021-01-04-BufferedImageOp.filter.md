---
title: BufferedImageOp.filter()
permalink: Java/BufferedImageOp/filter
date: 2021-01-04
key: JavaJava.B.BufferedImageOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImageOp.metodos valor="filter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BufferedImage filter(BufferedImage src, BufferedImage dest)
~~~

## Parámetros
* **BufferedImage dest**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage dest" %}
* **BufferedImage src**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage src" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedImageOp](/Java/BufferedImageOp/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedImageOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
