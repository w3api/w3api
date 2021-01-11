---
title: BasicTreeUI.paintHorizontalPartOfLeg()
permalink: Java/BasicTreeUI/paintHorizontalPartOfLeg
date: 2021-01-11
key: JavaJava.B.BasicTreeUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTreeUI.metodos valor="paintHorizontalPartOfLeg" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintHorizontalPartOfLeg(Graphics g, Rectangle clipBounds, Insets insets, Rectangle bounds, TreePath path, int row, boolean isExpanded, boolean hasBeenExpanded, boolean isLeaf)
~~~

## Parámetros
* **boolean hasBeenExpanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasBeenExpanded" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **boolean isExpanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isExpanded" %}
* **boolean isLeaf**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isLeaf" %}
* **TreePath path**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath path" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **Rectangle bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle bounds" %}
* **Rectangle clipBounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle clipBounds" %}
* **Insets insets**,  {% include w3api/param_description.html metodo=_dato parametro="Insets insets" %}

## Clase Padre
[BasicTreeUI](/Java/BasicTreeUI/)

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