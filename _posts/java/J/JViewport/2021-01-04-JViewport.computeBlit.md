---
title: JViewport.computeBlit()
permalink: Java/JViewport/computeBlit
date: 2021-01-04
key: JavaJava.J.JViewport
category: java
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
* **Point blitTo**,  {% include w3api/param_description.html metodo=_data parametro="Point blitTo" %}
* **Point blitFrom**,  {% include w3api/param_description.html metodo=_data parametro="Point blitFrom" %}
* **int dy**,  {% include w3api/param_description.html metodo=_data parametro="int dy" %}
* **Rectangle blitPaint**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle blitPaint" %}
* **int dx**,  {% include w3api/param_description.html metodo=_data parametro="int dx" %}
* **Dimension blitSize**,  {% include w3api/param_description.html metodo=_data parametro="Dimension blitSize" %}

## Clase Padre
[JViewport](/Java/JViewport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JViewport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
