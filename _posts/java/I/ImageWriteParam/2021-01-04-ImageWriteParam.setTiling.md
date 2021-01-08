---
title: ImageWriteParam.setTiling()
permalink: Java/ImageWriteParam/setTiling
date: 2021-01-04
key: JavaJava.I.ImageWriteParam
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriteParam.metodos valor="setTiling" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTiling(int tileWidth, int tileHeight, int tileGridXOffset, int tileGridYOffset)
~~~

## Parámetros
* **int tileGridYOffset**,  {% include w3api/param_description.html metodo=_data parametro="int tileGridYOffset" %}
* **int tileWidth**,  {% include w3api/param_description.html metodo=_data parametro="int tileWidth" %}
* **int tileGridXOffset**,  {% include w3api/param_description.html metodo=_data parametro="int tileGridXOffset" %}
* **int tileHeight**,  {% include w3api/param_description.html metodo=_data parametro="int tileHeight" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageWriteParam](/Java/ImageWriteParam/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageWriteParam.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
