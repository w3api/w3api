---
title: DebugGraphics.drawImage()
permalink: Java/DebugGraphics/drawImage
date: 2021-01-04
key: JavaJava.D.DebugGraphics
category: java
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
* **Color bgcolor**,  {% include w3api/param_description.html metodo=_data parametro="Color bgcolor" %}
* **int sx1**,  {% include w3api/param_description.html metodo=_data parametro="int sx1" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int dy2**,  {% include w3api/param_description.html metodo=_data parametro="int dy2" %}
* **int sy1**,  {% include w3api/param_description.html metodo=_data parametro="int sy1" %}
* **int sx2**,  {% include w3api/param_description.html metodo=_data parametro="int sx2" %}
* **int dy1**,  {% include w3api/param_description.html metodo=_data parametro="int dy1" %}
* **int dx1**,  {% include w3api/param_description.html metodo=_data parametro="int dx1" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **int dx2**,  {% include w3api/param_description.html metodo=_data parametro="int dx2" %}
* **Image img**,  {% include w3api/param_description.html metodo=_data parametro="Image img" %}
* **int sy2**,  {% include w3api/param_description.html metodo=_data parametro="int sy2" %}
* **ImageObserver observer**,  {% include w3api/param_description.html metodo=_data parametro="ImageObserver observer" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[DebugGraphics](/Java/DebugGraphics/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DebugGraphics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
