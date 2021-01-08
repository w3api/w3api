---
title: DirectColorModel.createCompatibleWritableRaster()
permalink: Java/DirectColorModel/createCompatibleWritableRaster
date: 2021-01-04
key: JavaJava.D.DirectColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.metodos valor="createCompatibleWritableRaster" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final WritableRaster createCompatibleWritableRaster(int w, int h)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DirectColorModel](/Java/DirectColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
