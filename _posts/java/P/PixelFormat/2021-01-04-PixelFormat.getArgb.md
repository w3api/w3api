---
title: PixelFormat.getArgb()
permalink: Java/PixelFormat/getArgb
date: 2021-01-04
key: JavaJava.P.PixelFormat
category: java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelFormat.metodos valor="getArgb" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getArgb(T buf, int x, int y, int scanlineStride)
~~~

## Parámetros
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **T buf**,  {% include w3api/param_description.html metodo=_data parametro="T buf" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[PixelFormat](/Java/PixelFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PixelFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
