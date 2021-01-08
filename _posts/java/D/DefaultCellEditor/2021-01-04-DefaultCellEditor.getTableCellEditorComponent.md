---
title: DefaultCellEditor.getTableCellEditorComponent()
permalink: Java/DefaultCellEditor/getTableCellEditorComponent
date: 2021-01-04
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
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSelected" %}
* **JTable table**,  {% include w3api/param_description.html metodo=_data parametro="JTable table" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[DefaultCellEditor](/Java/DefaultCellEditor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultCellEditor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
