---
title: DefaultTreeCellRenderer.getTreeCellRendererComponent()
permalink: /Java/DefaultTreeCellRenderer/getTreeCellRendererComponent/
date: 2021-01-11
key: Java.D.DefaultTreeCellRenderer
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeCellRenderer.metodos valor="getTreeCellRendererComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getTreeCellRendererComponent(JTree tree, Object value, boolean sel, boolean expanded, boolean leaf, int row, boolean hasFocus)
~~~

## Parámetros
* **boolean leaf**,  {% include w3api/param_description.html metodo=_dato parametro="boolean leaf" %}
* **boolean sel**,  {% include w3api/param_description.html metodo=_dato parametro="boolean sel" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **JTree tree**,  {% include w3api/param_description.html metodo=_dato parametro="JTree tree" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean expanded" %}
* **boolean hasFocus**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasFocus" %}

## Clase Padre
[DefaultTreeCellRenderer](/Java/DefaultTreeCellRenderer/)

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
