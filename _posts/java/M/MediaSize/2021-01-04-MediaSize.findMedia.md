---
title: MediaSize.findMedia()
permalink: Java/MediaSize/findMedia
date: 2021-01-04
key: JavaJava.M.MediaSize
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaSize.metodos valor="findMedia" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MediaSizeName findMedia(float x, float y, int units)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **int units**,  {% include w3api/param_description.html metodo=_data parametro="int units" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MediaSize](/Java/MediaSize/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MediaSize.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
