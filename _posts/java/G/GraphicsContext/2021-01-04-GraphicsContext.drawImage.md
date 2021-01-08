---
title: GraphicsContext.drawImage()
permalink: Java/GraphicsContext/drawImage
date: 2021-01-04
key: JavaJava.G.GraphicsContext
category: java
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
* **double dh**,  {% include w3api/param_description.html metodo=_data parametro="double dh" %}
* **double w**,  {% include w3api/param_description.html metodo=_data parametro="double w" %}
* **double dw**,  {% include w3api/param_description.html metodo=_data parametro="double dw" %}
* **double h**,  {% include w3api/param_description.html metodo=_data parametro="double h" %}
* **double dy**,  {% include w3api/param_description.html metodo=_data parametro="double dy" %}
* **double dx**,  {% include w3api/param_description.html metodo=_data parametro="double dx" %}
* **Image img**,  {% include w3api/param_description.html metodo=_data parametro="Image img" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **double sx**,  {% include w3api/param_description.html metodo=_data parametro="double sx" %}
* **double sy**,  {% include w3api/param_description.html metodo=_data parametro="double sy" %}
* **double sw**,  {% include w3api/param_description.html metodo=_data parametro="double sw" %}
* **double sh**,  {% include w3api/param_description.html metodo=_data parametro="double sh" %}

## Clase Padre
[GraphicsContext](/Java/GraphicsContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GraphicsContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
