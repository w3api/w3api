---
title: TreeSelectionEvent.isAddedPath()
permalink: /Java/TreeSelectionEvent/isAddedPath/
date: 2021-01-11
key: Java.T.TreeSelectionEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeSelectionEvent.metodos valor="isAddedPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isAddedPath()
public boolean isAddedPath(int index)
public boolean isAddedPath(TreePath path)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **TreePath path**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath path" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TreeSelectionEvent](/Java/TreeSelectionEvent/)

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
