---
title: TreeCellRenderer.getTreeCellRendererComponent()
permalink: Java/TreeCellRenderer/getTreeCellRendererComponent
date: 2021-01-04
key: JavaJava.T.TreeCellRenderer
category: java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeCellRenderer.metodos valor="getTreeCellRendererComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Component getTreeCellRendererComponent(JTree tree, Object value, boolean selected, boolean expanded, boolean leaf, int row, boolean hasFocus)
~~~

## Parámetros
* **boolean leaf**,  {% include w3api/param_description.html metodo=_data parametro="boolean leaf" %}
* **boolean hasFocus**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasFocus" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **boolean selected**,  {% include w3api/param_description.html metodo=_data parametro="boolean selected" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_data parametro="boolean expanded" %}
* **JTree tree**,  {% include w3api/param_description.html metodo=_data parametro="JTree tree" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[TreeCellRenderer](/Java/TreeCellRenderer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeCellRenderer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
