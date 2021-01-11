---
title: DocTreeFactory.newDocCommentTree()
permalink: Java/DocTreeFactory/newDocCommentTree
date: 2021-01-11
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newDocCommentTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DocCommentTree newDocCommentTree(List<? extends DocTree> fullBody, List<? extends DocTree> tags)
DocCommentTree newDocCommentTree(List<? extends DocTree> fullBody, List<? extends DocTree> tags, List<? extends DocTree> preamble, List<? extends DocTree> postamble)
~~~

## Parámetros
* **List&lt;? extends DocTree&gt; fullBody**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> fullBody" %}
* **List&lt;? extends DocTree&gt; postamble**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> postamble" %}
* **List&lt;? extends DocTree&gt; preamble**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> preamble" %}
* **List&lt;? extends DocTree&gt; tags**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> tags" %}

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
