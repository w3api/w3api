---
title: DebugGraphics.drawImage()
permalink: /Java/DebugGraphics/drawImage/
date: 2021-01-11
key: Java.D.DebugGraphics
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DebugGraphics.metodos valor="drawImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean drawImage(Image img, int dx1, int dy1, int dx2, int dy2, int sx1, int sy1, int sx2, int sy2, Color bgcolor, ImageObserver observer)
public boolean drawImage(Image img, int dx1, int dy1, int dx2, int dy2, int sx1, int sy1, int sx2, int sy2, ImageObserver observer)
public boolean drawImage(Image img, int x, int y, int width, int height, Color bgcolor, ImageObserver observer)
public boolean drawImage(Image img, int x, int y, int width, int height, ImageObserver observer)
public boolean drawImage(Image img, int x, int y, Color bgcolor, ImageObserver observer)
public boolean drawImage(Image img, int x, int y, ImageObserver observer)
~~~

## Parámetros
* **int sy2**,  {% include w3api/param_description.html metodo=_dato parametro="int sy2" %}
* **int dy2**,  {% include w3api/param_description.html metodo=_dato parametro="int dy2" %}
* **int dy1**,  {% include w3api/param_description.html metodo=_dato parametro="int dy1" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int dx2**,  {% include w3api/param_description.html metodo=_dato parametro="int dx2" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int dx1**,  {% include w3api/param_description.html metodo=_dato parametro="int dx1" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int sy1**,  {% include w3api/param_description.html metodo=_dato parametro="int sy1" %}
* **Color bgcolor**,  {% include w3api/param_description.html metodo=_dato parametro="Color bgcolor" %}
* **Image img**,  {% include w3api/param_description.html metodo=_dato parametro="Image img" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int sx2**,  {% include w3api/param_description.html metodo=_dato parametro="int sx2" %}
* **ImageObserver observer**,  {% include w3api/param_description.html metodo=_dato parametro="ImageObserver observer" %}
* **int sx1**,  {% include w3api/param_description.html metodo=_dato parametro="int sx1" %}

## Clase Padre
[DebugGraphics](/Java/DebugGraphics/)

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
