---
title: DocTreeFactory.newUsesTree()
permalink: Java/DocTreeFactory/newUsesTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newUsesTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
UsesTree newUsesTree(ReferenceTree name, List<? extends DocTree> description)
~~~

## Parámetros
* **ReferenceTree name**,  {% include w3api/param_description.html metodo=_data parametro="ReferenceTree name" %}
* **List&lt;? extends DocTree&gt; description**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends DocTree> description" %}

## Clase Padre
[DocTreeFactory](/Java/DocTreeFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreeFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
