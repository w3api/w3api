---
title: ImageTypeSpecifier.createInterleaved()
permalink: /Java/ImageTypeSpecifier/createInterleaved/
date: 2021-01-11
key: Java.I.ImageTypeSpecifier
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="createInterleaved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ImageTypeSpecifier createInterleaved(ColorSpace colorSpace, int[] bandOffsets, int dataType, boolean hasAlpha, boolean isAlphaPremultiplied)
~~~

## Parámetros
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **ColorSpace colorSpace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace colorSpace" %}
* **boolean hasAlpha**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasAlpha" %}
* **int[] bandOffsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bandOffsets" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
