---
title: BasicTabbedPaneUI.paintTab()
permalink: Java/BasicTabbedPaneUI/paintTab
date: 2021-01-11
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="paintTab" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintTab(Graphics g, int tabPlacement, Rectangle[] rects, int tabIndex, Rectangle iconRect, Rectangle textRect)
~~~

## Parámetros
* **Rectangle[] rects**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle[] rects" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconRect" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textRect" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int tabIndex" %}

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

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
