---
title: SwingUtilities.paintComponent()
permalink: Java/SwingUtilities/paintComponent
date: 2021-01-11
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="paintComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void paintComponent(Graphics g, Component c, Container p, int x, int y, int w, int h)
public static void paintComponent(Graphics g, Component c, Container p, Rectangle r)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Container p**,  {% include w3api/param_description.html metodo=_dato parametro="Container p" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle r" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

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
