---
title: GraphicsConfiguration.createCompatibleImage()
permalink: /Java/GraphicsConfiguration/createCompatibleImage/
date: 2021-01-11
key: Java.G.GraphicsConfiguration
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GraphicsConfiguration.metodos valor="createCompatibleImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage createCompatibleImage(int width, int height)
public BufferedImage createCompatibleImage(int width, int height, int transparency)
~~~

## Parámetros
* **int transparency**,  {% include w3api/param_description.html metodo=_dato parametro="int transparency" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GraphicsConfiguration](/Java/GraphicsConfiguration/)

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
