---
title: DefaultTreeModel.nodesWereRemoved()
permalink: Java/DefaultTreeModel/nodesWereRemoved
date: 2021-01-04
key: JavaJava.D.DefaultTreeModel
category: java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeModel.metodos valor="nodesWereRemoved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void nodesWereRemoved(TreeNode node, int[] childIndices, Object[] removedChildren)
~~~

## Parámetros
* **Object[] removedChildren**,  {% include w3api/param_description.html metodo=_data parametro="Object[] removedChildren" %}
* **int[] childIndices**,  {% include w3api/param_description.html metodo=_data parametro="int[] childIndices" %}
* **TreeNode node**,  {% include w3api/param_description.html metodo=_data parametro="TreeNode node" %}

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
