---
title: IIOReadProgressListener.sequenceStarted()
permalink: Java/IIOReadProgressListener/sequenceStarted
date: 2021-01-11
key: JavaJava.I.IIOReadProgressListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadProgressListener.metodos valor="sequenceStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sequenceStarted(ImageReader source, int minIndex)
~~~

## Parámetros
* **ImageReader source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReader source" %}
* **int minIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int minIndex" %}

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
