---
title: DefaultCellEditor.getTableCellEditorComponent()
permalink: Java/DefaultCellEditor/getTableCellEditorComponent
date: 2021-01-11
key: JavaJava.D.DefaultCellEditor
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultCellEditor.metodos valor="getTableCellEditorComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getTableCellEditorComponent(JTable table, Object value, boolean isSelected, int row, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **JTable table**,  {% include w3api/param_description.html metodo=_dato parametro="JTable table" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}

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
