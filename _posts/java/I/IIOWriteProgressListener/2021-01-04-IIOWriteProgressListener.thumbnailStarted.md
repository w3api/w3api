---
title: IIOWriteProgressListener.thumbnailStarted()
permalink: Java/IIOWriteProgressListener/thumbnailStarted
date: 2021-01-04
key: JavaJava.I.IIOWriteProgressListener
category: java
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
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **ImageWriter source**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriter source" %}
* **int thumbnailIndex**,  {% include w3api/param_description.html metodo=_data parametro="int thumbnailIndex" %}

## Clase Padre
[IIOWriteProgressListener](/Java/IIOWriteProgressListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOWriteProgressListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
