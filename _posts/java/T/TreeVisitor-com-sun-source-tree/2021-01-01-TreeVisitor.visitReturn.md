---
title: TreeVisitor.visitReturn()
permalink: Java/TreeVisitor-com-sun-source-tree/visitReturn
date: 2021-01-11
key: JavaJava.T.TreeVisitor-com-sun-source-tree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeVisitor-com-sun-source-tree.metodos valor="visitReturn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitReturn(ReturnTree node, P p)
~~~

## Parámetros
* **ReturnTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ReturnTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[TreeVisitor](/Java/TreeVisitor-com-sun-source-tree/)

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