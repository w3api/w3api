---
title: DefaultTreeModel.getPathToRoot()
permalink: /Java/DefaultTreeModel/getPathToRoot/
date: 2021-01-11
key: Java.D.DefaultTreeModel
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeModel.metodos valor="getPathToRoot" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TreeNode[] getPathToRoot(TreeNode aNode)
protected TreeNode[] getPathToRoot(TreeNode aNode, int depth)
~~~

## Parámetros
* **int depth**,  {% include w3api/param_description.html metodo=_dato parametro="int depth" %}
* **TreeNode aNode**,  {% include w3api/param_description.html metodo=_dato parametro="TreeNode aNode" %}

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
