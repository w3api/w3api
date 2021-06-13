---
title: PixelFormat.getArgb()
permalink: /Java/PixelFormat/getArgb/
date: 2021-01-11
key: Java.P.PixelFormat
category: Java
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
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **T buf**,  {% include w3api/param_description.html metodo=_dato parametro="T buf" %}

## Clase Padre
[PixelFormat](/Java/PixelFormat/)

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
