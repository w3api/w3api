---
title: TableCellRenderer.getTableCellRendererComponent()
permalink: Java/TableCellRenderer/getTableCellRendererComponent
date: 2021-01-04
key: JavaJava.T.TableCellRenderer
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableCellRenderer.metodos valor="getTableCellRendererComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column)
~~~

## Parámetros
* **boolean hasFocus**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasFocus" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSelected" %}
* **JTable table**,  {% include w3api/param_description.html metodo=_data parametro="JTable table" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[TableCellRenderer](/Java/TableCellRenderer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableCellRenderer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
