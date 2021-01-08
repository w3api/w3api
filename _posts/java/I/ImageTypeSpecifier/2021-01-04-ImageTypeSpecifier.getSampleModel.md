---
title: ImageTypeSpecifier.getSampleModel()
permalink: Java/ImageTypeSpecifier/getSampleModel
date: 2021-01-04
key: JavaJava.I.ImageTypeSpecifier
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageTypeSpecifier.metodos valor="getSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SampleModel getSampleModel()
public SampleModel getSampleModel(int width, int height)
~~~

## Parámetros
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

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
