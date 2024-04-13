---
title: ImageWriteParam.setTiling()
permalink: /Java/ImageWriteParam/setTiling/
date: 2021-01-11
key: Java.I.ImageWriteParam
category: Java
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
* **int tileHeight**,  {% include w3api/param_description.html metodo=_dato parametro="int tileHeight" %}
* **int tileWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int tileWidth" %}
* **int tileGridYOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int tileGridYOffset" %}
* **int tileGridXOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int tileGridXOffset" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ImageWriteParam](/Java/ImageWriteParam/)

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
