---
title: GraphicsContext.drawImage()
permalink: /Java/GraphicsContext/drawImage/
date: 2021-01-11
key: Java.G.GraphicsContext
category: Java
tags: ['java se', 'javafx.scene.canvas', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GraphicsContext.metodos valor="drawImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void drawImage(Image img, double x, double y)
public void drawImage(Image img, double x, double y, double w, double h)
public void drawImage(Image img, double sx, double sy, double sw, double sh, double dx, double dy, double dw, double dh)
~~~

## Parámetros
* **double dx**,  {% include w3api/param_description.html metodo=_dato parametro="double dx" %}
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}
* **double sh**,  {% include w3api/param_description.html metodo=_dato parametro="double sh" %}
* **double dw**,  {% include w3api/param_description.html metodo=_dato parametro="double dw" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double dh**,  {% include w3api/param_description.html metodo=_dato parametro="double dh" %}
* **Image img**,  {% include w3api/param_description.html metodo=_dato parametro="Image img" %}
* **double sx**,  {% include w3api/param_description.html metodo=_dato parametro="double sx" %}
* **double sw**,  {% include w3api/param_description.html metodo=_dato parametro="double sw" %}
* **double dy**,  {% include w3api/param_description.html metodo=_dato parametro="double dy" %}
* **double sy**,  {% include w3api/param_description.html metodo=_dato parametro="double sy" %}

## Clase Padre
[GraphicsContext](/Java/GraphicsContext/)

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
