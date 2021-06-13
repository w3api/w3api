---
title: TreeWillExpandListener.treeWillExpand()
permalink: /Java/TreeWillExpandListener/treeWillExpand/
date: 2021-01-11
key: Java.T.TreeWillExpandListener
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeWillExpandListener.metodos valor="treeWillExpand" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void treeWillExpand(TreeExpansionEvent event) throws ExpandVetoException
~~~

## Parámetros
* **TreeExpansionEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="TreeExpansionEvent event" %}

## Excepciones
[ExpandVetoException](/Java/ExpandVetoException/)

## Clase Padre
[TreeWillExpandListener](/Java/TreeWillExpandListener/)

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
