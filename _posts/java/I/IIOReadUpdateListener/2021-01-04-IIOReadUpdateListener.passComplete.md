---
title: IIOReadUpdateListener.passComplete()
permalink: Java/IIOReadUpdateListener/passComplete
date: 2021-01-04
key: JavaJava.I.IIOReadUpdateListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadUpdateListener.metodos valor="passComplete" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void passComplete(ImageReader source, BufferedImage theImage)
~~~

## Parámetros
* **ImageReader source**,  {% include w3api/param_description.html metodo=_data parametro="ImageReader source" %}
* **BufferedImage theImage**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage theImage" %}

## Clase Padre
[IIOReadUpdateListener](/Java/IIOReadUpdateListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOReadUpdateListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
