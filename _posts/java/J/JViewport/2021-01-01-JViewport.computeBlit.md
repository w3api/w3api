---
title: JViewport.computeBlit()
permalink: /Java/JViewport/computeBlit/
date: 2021-01-11
key: Java.J.JViewport
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JViewport.metodos valor="computeBlit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean computeBlit(int dx, int dy, Point blitFrom, Point blitTo, Dimension blitSize, Rectangle blitPaint)
~~~

## Parámetros
* **Point blitTo**,  {% include w3api/param_description.html metodo=_dato parametro="Point blitTo" %}
* **Dimension blitSize**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension blitSize" %}
* **Point blitFrom**,  {% include w3api/param_description.html metodo=_dato parametro="Point blitFrom" %}
* **int dx**,  {% include w3api/param_description.html metodo=_dato parametro="int dx" %}
* **Rectangle blitPaint**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle blitPaint" %}
* **int dy**,  {% include w3api/param_description.html metodo=_dato parametro="int dy" %}

## Clase Padre
[JViewport](/Java/JViewport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
