---
title: DefaultTreeModel.fireTreeNodesInserted()
permalink: /Java/DefaultTreeModel/fireTreeNodesInserted/
date: 2021-01-11
key: Java.D.DefaultTreeModel
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeModel.metodos valor="fireTreeNodesInserted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireTreeNodesInserted(Object source, Object[] path, int[] childIndices, Object[] children)
~~~

## Parámetros
* **Object[] children**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] children" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **Object[] path**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] path" %}
* **int[] childIndices**,  {% include w3api/param_description.html metodo=_dato parametro="int[] childIndices" %}

## Clase Padre
[DefaultTreeModel](/Java/DefaultTreeModel/)

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
