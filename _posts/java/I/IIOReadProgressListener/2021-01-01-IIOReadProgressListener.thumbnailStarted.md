---
title: IIOReadProgressListener.thumbnailStarted()
permalink: Java/IIOReadProgressListener/thumbnailStarted
date: 2021-01-11
key: JavaJava.I.IIOReadProgressListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadProgressListener.metodos valor="thumbnailStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void thumbnailStarted(ImageReader source, int imageIndex, int thumbnailIndex)
~~~

## Parámetros
* **ImageReader source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReader source" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}
* **int thumbnailIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int thumbnailIndex" %}

## Clase Padre
[IIOReadProgressListener](/Java/IIOReadProgressListener/)

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
