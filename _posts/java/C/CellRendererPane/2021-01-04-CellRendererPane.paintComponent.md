---
title: CellRendererPane.paintComponent()
permalink: Java/CellRendererPane/paintComponent
date: 2021-01-04
key: JavaJava.C.CellRendererPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CellRendererPane.metodos valor="paintComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paintComponent(Graphics g, Component c, Container p, int x, int y, int w, int h)
public void paintComponent(Graphics g, Component c, Container p, int x, int y, int w, int h, boolean shouldValidate)
public void paintComponent(Graphics g, Component c, Container p, Rectangle r)
~~~

## Parámetros
* **boolean shouldValidate**,  {% include w3api/param_description.html metodo=_data parametro="boolean shouldValidate" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle r" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Container p**,  {% include w3api/param_description.html metodo=_data parametro="Container p" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[CellRendererPane](/Java/CellRendererPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CellRendererPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
