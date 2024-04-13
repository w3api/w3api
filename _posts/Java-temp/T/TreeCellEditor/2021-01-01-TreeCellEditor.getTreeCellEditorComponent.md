---
title: TreeCellEditor.getTreeCellEditorComponent()
permalink: /Java/TreeCellEditor/getTreeCellEditorComponent/
date: 2021-01-11
key: Java.T.TreeCellEditor
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeCellEditor.metodos valor="getTreeCellEditorComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Component getTreeCellEditorComponent(JTree tree, Object value, boolean isSelected, boolean expanded, boolean leaf, int row)
~~~

## Parámetros
* **boolean leaf**,  {% include w3api/param_description.html metodo=_dato parametro="boolean leaf" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}
* **JTree tree**,  {% include w3api/param_description.html metodo=_dato parametro="JTree tree" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean expanded" %}

## Clase Padre
[TreeCellEditor](/Java/TreeCellEditor/)

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
