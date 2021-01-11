---
title: DocTreeFactory.newAuthorTree()
permalink: Java/DocTreeFactory/newAuthorTree
date: 2021-01-11
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newAuthorTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AuthorTree newAuthorTree(List<? extends DocTree> name)
~~~

## Parámetros
* **List&lt;? extends DocTree&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> name" %}

## Clase Padre
[DocTreeFactory](/Java/DocTreeFactory/)

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