---
title: BasicTabbedPaneUI.paintFocusIndicator()
permalink: Java/BasicTabbedPaneUI/paintFocusIndicator
date: 2021-01-04
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="paintFocusIndicator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintFocusIndicator(Graphics g, int tabPlacement, Rectangle[] rects, int tabIndex, Rectangle iconRect, Rectangle textRect, boolean isSelected)
~~~

## Parámetros
* **int tabIndex**,  {% include w3api/param_description.html metodo=_data parametro="int tabIndex" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle iconRect" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_data parametro="int tabPlacement" %}
* **Rectangle[] rects**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle[] rects" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textRect" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSelected" %}

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicTabbedPaneUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
