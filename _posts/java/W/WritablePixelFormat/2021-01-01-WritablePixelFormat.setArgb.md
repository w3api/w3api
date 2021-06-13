---
title: WritablePixelFormat.setArgb()
permalink: /Java/WritablePixelFormat/setArgb/
date: 2021-01-11
key: Java.W.WritablePixelFormat
category: Java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritablePixelFormat.metodos valor="setArgb" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setArgb(T buf, int x, int y, int scanlineStride, int argb)
~~~

## Parámetros
* **int argb**,  {% include w3api/param_description.html metodo=_dato parametro="int argb" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **T buf**,  {% include w3api/param_description.html metodo=_dato parametro="T buf" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[WritablePixelFormat](/Java/WritablePixelFormat/)

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
