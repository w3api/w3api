---
title: ImageTypeSpecifier.createIndexed()
permalink: Java/ImageTypeSpecifier/createIndexed
date: 2021-01-04
key: JavaJava.I.ImageTypeSpecifier
category: java
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
* **byte[] blueLUT**,  {% include w3api/param_description.html metodo=_data parametro="byte[] blueLUT" %}
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **byte[] greenLUT**,  {% include w3api/param_description.html metodo=_data parametro="byte[] greenLUT" %}
* **byte[] redLUT**,  {% include w3api/param_description.html metodo=_data parametro="byte[] redLUT" %}
* **byte[] alphaLUT**,  {% include w3api/param_description.html metodo=_data parametro="byte[] alphaLUT" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

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
