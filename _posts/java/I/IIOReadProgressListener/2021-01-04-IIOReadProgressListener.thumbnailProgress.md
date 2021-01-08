---
title: IIOReadProgressListener.thumbnailProgress()
permalink: Java/IIOReadProgressListener/thumbnailProgress
date: 2021-01-04
key: JavaJava.I.IIOReadProgressListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadProgressListener.metodos valor="thumbnailProgress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void thumbnailProgress(ImageReader source, float percentageDone)
~~~

## Parámetros
* **float percentageDone**,  {% include w3api/param_description.html metodo=_data parametro="float percentageDone" %}
* **ImageReader source**,  {% include w3api/param_description.html metodo=_data parametro="ImageReader source" %}

## Clase Padre
[IIOReadProgressListener](/Java/IIOReadProgressListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOReadProgressListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
