---
title: IIOReadUpdateListener.thumbnailPassComplete()
permalink: /Java/IIOReadUpdateListener/thumbnailPassComplete/
date: 2021-01-11
key: Java.I.IIOReadUpdateListener
category: Java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadUpdateListener.metodos valor="thumbnailPassComplete" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void thumbnailPassComplete(ImageReader source, BufferedImage theThumbnail)
~~~

## Parámetros
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage theThumbnail" %}
* **ImageReader source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReader source" %}

## Clase Padre
[IIOReadUpdateListener](/Java/IIOReadUpdateListener/)

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
