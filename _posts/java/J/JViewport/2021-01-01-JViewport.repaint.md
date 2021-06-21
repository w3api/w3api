---
title: JViewport.repaint()
permalink: /Java/JViewport/repaint/
date: 2021-01-11
key: Java.J.JViewport
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JViewport.metodos valor="repaint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void repaint(long tm, int x, int y, int w, int h)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **long tm**,  {% include w3api/param_description.html metodo=_dato parametro="long tm" %}

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
