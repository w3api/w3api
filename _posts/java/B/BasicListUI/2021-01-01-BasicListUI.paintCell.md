---
title: BasicListUI.paintCell()
permalink: /Java/BasicListUI/paintCell/
date: 2021-01-11
key: JavaJava.B.BasicListUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicListUI.metodos valor="paintCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintCell(Graphics g, int row, Rectangle rowBounds, ListCellRenderer<Object> cellRenderer, ListModel<Object> dataModel, ListSelectionModel selModel, int leadIndex)
~~~

## Parámetros
* **ListModel&lt;Object&gt; dataModel**,  {% include w3api/param_description.html metodo=_dato parametro="ListModel<Object> dataModel" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **ListCellRenderer&lt;Object&gt; cellRenderer**,  {% include w3api/param_description.html metodo=_dato parametro="ListCellRenderer<Object> cellRenderer" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **Rectangle rowBounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle rowBounds" %}
* **int leadIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int leadIndex" %}
* **ListSelectionModel selModel**,  {% include w3api/param_description.html metodo=_dato parametro="ListSelectionModel selModel" %}

## Clase Padre
[BasicListUI](/Java/BasicListUI/)

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
