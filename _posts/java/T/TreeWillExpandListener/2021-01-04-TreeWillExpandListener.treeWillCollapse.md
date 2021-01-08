---
title: TreeWillExpandListener.treeWillCollapse()
permalink: Java/TreeWillExpandListener/treeWillCollapse
date: 2021-01-04
key: JavaJava.T.TreeWillExpandListener
category: java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeWillExpandListener.metodos valor="treeWillCollapse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void treeWillCollapse(TreeExpansionEvent event) throws ExpandVetoException
~~~

## Parámetros
* **TreeExpansionEvent event**,  {% include w3api/param_description.html metodo=_data parametro="TreeExpansionEvent event" %}

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
{%- for _ldc in site.data.Java.T.TreeWillExpandListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
