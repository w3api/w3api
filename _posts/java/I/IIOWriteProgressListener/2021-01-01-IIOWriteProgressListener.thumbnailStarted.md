---
title: IIOWriteProgressListener.thumbnailStarted()
permalink: /Java/IIOWriteProgressListener/thumbnailStarted/
date: 2021-01-11
key: Java.I.IIOWriteProgressListener
category: Java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOWriteProgressListener.metodos valor="thumbnailStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void thumbnailStarted(ImageWriter source, int imageIndex, int thumbnailIndex)
~~~

## Parámetros
* **ImageWriter source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriter source" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}
* **int thumbnailIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int thumbnailIndex" %}

## Clase Padre
[IIOWriteProgressListener](/Java/IIOWriteProgressListener/)

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
