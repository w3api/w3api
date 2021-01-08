---
title: WritablePixelFormat.setArgb()
permalink: Java/WritablePixelFormat/setArgb
date: 2021-01-04
key: JavaJava.W.WritablePixelFormat
category: java
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
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **T buf**,  {% include w3api/param_description.html metodo=_data parametro="T buf" %}
* **int argb**,  {% include w3api/param_description.html metodo=_data parametro="int argb" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[WritablePixelFormat](/Java/WritablePixelFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WritablePixelFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
