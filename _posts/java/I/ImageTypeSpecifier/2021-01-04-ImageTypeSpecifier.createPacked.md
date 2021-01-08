---
title: ImageTypeSpecifier.createPacked()
permalink: Java/ImageTypeSpecifier/createPacked
date: 2021-01-04
key: JavaJava.I.ImageTypeSpecifier
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="createPacked" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ImageTypeSpecifier createPacked(ColorSpace colorSpace, int redMask, int greenMask, int blueMask, int alphaMask, int transferType, boolean isAlphaPremultiplied)
~~~

## Parámetros
* **ColorSpace colorSpace**,  {% include w3api/param_description.html metodo=_data parametro="ColorSpace colorSpace" %}
* **int blueMask**,  {% include w3api/param_description.html metodo=_data parametro="int blueMask" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}
* **int greenMask**,  {% include w3api/param_description.html metodo=_data parametro="int greenMask" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **int redMask**,  {% include w3api/param_description.html metodo=_data parametro="int redMask" %}
* **int alphaMask**,  {% include w3api/param_description.html metodo=_data parametro="int alphaMask" %}

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
{%- for _ldc in site.data.Java.I.ImageTypeSpecifier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
