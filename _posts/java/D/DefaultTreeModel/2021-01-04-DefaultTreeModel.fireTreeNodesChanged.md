---
title: DefaultTreeModel.fireTreeNodesChanged()
permalink: Java/DefaultTreeModel/fireTreeNodesChanged
date: 2021-01-04
key: JavaJava.D.DefaultTreeModel
category: java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeModel.metodos valor="fireTreeNodesChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireTreeNodesChanged(Object source, Object[] path, int[] childIndices, Object[] children)
~~~

## Parámetros
* **Object[] path**,  {% include w3api/param_description.html metodo=_data parametro="Object[] path" %}
* **int[] childIndices**,  {% include w3api/param_description.html metodo=_data parametro="int[] childIndices" %}
* **Object[] children**,  {% include w3api/param_description.html metodo=_data parametro="Object[] children" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Clase Padre
[DefaultTreeModel](/Java/DefaultTreeModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTreeModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
