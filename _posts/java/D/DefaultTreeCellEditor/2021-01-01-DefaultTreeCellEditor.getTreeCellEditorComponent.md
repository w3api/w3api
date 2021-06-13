---
title: DefaultTreeCellEditor.getTreeCellEditorComponent()
permalink: /Java/DefaultTreeCellEditor/getTreeCellEditorComponent/
date: 2021-01-11
key: Java.D.DefaultTreeCellEditor
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeCellEditor.metodos valor="getTreeCellEditorComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getTreeCellEditorComponent(JTree tree, Object value, boolean isSelected, boolean expanded, boolean leaf, int row)
~~~

## Parámetros
* **boolean leaf**,  {% include w3api/param_description.html metodo=_dato parametro="boolean leaf" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}
* **JTree tree**,  {% include w3api/param_description.html metodo=_dato parametro="JTree tree" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_dato parametro="boolean expanded" %}

## Clase Padre
[DefaultTreeCellEditor](/Java/DefaultTreeCellEditor/)

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
