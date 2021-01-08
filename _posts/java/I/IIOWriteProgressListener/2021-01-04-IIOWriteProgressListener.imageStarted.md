---
title: IIOWriteProgressListener.imageStarted()
permalink: Java/IIOWriteProgressListener/imageStarted
date: 2021-01-04
key: JavaJava.I.IIOWriteProgressListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOWriteProgressListener.metodos valor="imageStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void imageStarted(ImageWriter source, int imageIndex)
~~~

## Parámetros
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **ImageWriter source**,  {% include w3api/param_description.html metodo=_data parametro="ImageWriter source" %}

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
