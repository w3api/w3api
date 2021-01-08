---
title: DefaultTreeCellRenderer.getTreeCellRendererComponent()
permalink: Java/DefaultTreeCellRenderer/getTreeCellRendererComponent
date: 2021-01-04
key: JavaJava.D.DefaultTreeCellRenderer
category: java
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
* **boolean leaf**,  {% include w3api/param_description.html metodo=_data parametro="boolean leaf" %}
* **boolean hasFocus**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasFocus" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **boolean expanded**,  {% include w3api/param_description.html metodo=_data parametro="boolean expanded" %}
* **boolean sel**,  {% include w3api/param_description.html metodo=_data parametro="boolean sel" %}
* **JTree tree**,  {% include w3api/param_description.html metodo=_data parametro="JTree tree" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[DefaultTreeCellRenderer](/Java/DefaultTreeCellRenderer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTreeCellRenderer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
