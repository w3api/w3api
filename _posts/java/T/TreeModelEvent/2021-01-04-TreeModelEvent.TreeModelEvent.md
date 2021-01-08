---
title: TreeModelEvent.TreeModelEvent()
permalink: Java/TreeModelEvent/TreeModelEvent
date: 2021-01-04
key: JavaJava.T.TreeModelEvent
category: java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeModelEvent.constructores valor="TreeModelEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TreeModelEvent(Object source, Object[] path)
public TreeModelEvent(Object source, Object[] path, int[] childIndices, Object[] children)
public TreeModelEvent(Object source, TreePath path)
public TreeModelEvent(Object source, TreePath path, int[] childIndices, Object[] children)
~~~

## Parámetros
* **TreePath path**,  {% include w3api/param_description.html metodo=_data parametro="TreePath path" %}
* **Object[] path**,  {% include w3api/param_description.html metodo=_data parametro="Object[] path" %}
* **Object[] children**,  {% include w3api/param_description.html metodo=_data parametro="Object[] children" %}
* **int[] childIndices**,  {% include w3api/param_description.html metodo=_data parametro="int[] childIndices" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Clase Padre
[TreeModelEvent](/Java/TreeModelEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeModelEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
