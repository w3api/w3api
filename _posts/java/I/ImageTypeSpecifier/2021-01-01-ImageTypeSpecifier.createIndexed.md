---
title: ImageTypeSpecifier.createIndexed()
permalink: /Java/ImageTypeSpecifier/createIndexed/
date: 2021-01-11
key: Java.I.ImageTypeSpecifier
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="createIndexed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ImageTypeSpecifier createIndexed(byte[] redLUT, byte[] greenLUT, byte[] blueLUT, byte[] alphaLUT, int bits, int dataType)
~~~

## Parámetros
* **byte[] greenLUT**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] greenLUT" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **byte[] redLUT**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] redLUT" %}
* **byte[] blueLUT**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] blueLUT" %}
* **byte[] alphaLUT**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] alphaLUT" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageTypeSpecifier](/Java/ImageTypeSpecifier/)

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
