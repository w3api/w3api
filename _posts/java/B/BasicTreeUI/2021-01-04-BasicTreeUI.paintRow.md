---
title: BasicTreeUI.paintRow()
permalink: Java/BasicTreeUI/paintRow
date: 2021-01-04
key: JavaJava.B.BasicTreeUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTreeUI.metodos valor="paintRow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintRow(Graphics g, Rectangle clipBounds, Insets insets, Rectangle bounds, TreePath path, int row, boolean isExpanded, boolean hasBeenExpanded, boolean isLeaf)
~~~

## Parámetros
* **TreePath path**,  {% include w3api/param_description.html metodo=_data parametro="TreePath path" %}
* **Rectangle bounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle bounds" %}
* **Insets insets**,  {% include w3api/param_description.html metodo=_data parametro="Insets insets" %}
* **boolean isExpanded**,  {% include w3api/param_description.html metodo=_data parametro="boolean isExpanded" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Rectangle clipBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle clipBounds" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **boolean isLeaf**,  {% include w3api/param_description.html metodo=_data parametro="boolean isLeaf" %}
* **boolean hasBeenExpanded**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasBeenExpanded" %}

## Clase Padre
[BasicTreeUI](/Java/BasicTreeUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicTreeUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
