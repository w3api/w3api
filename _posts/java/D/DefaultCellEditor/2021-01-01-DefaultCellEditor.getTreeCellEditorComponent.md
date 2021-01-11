---
title: DefaultCellEditor.getTreeCellEditorComponent()
permalink: Java/DefaultCellEditor/getTreeCellEditorComponent
date: 2021-01-11
key: JavaJava.D.DefaultCellEditor
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultCellEditor.metodos valor="getTreeCellEditorComponent" %}

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
[DefaultCellEditor](/Java/DefaultCellEditor/)

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
