---
title: DocTreePath.DocTreePath()
permalink: /Java/DocTreePath/DocTreePath/
date: 2021-01-11
key: Java.D.DocTreePath
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreePath.constructores valor="DocTreePath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DocTreePath(DocTreePath p, DocTree t)
public DocTreePath(TreePath treePath, DocCommentTree t)
~~~

## Parámetros
* **DocTree t**,  {% include w3api/param_description.html metodo=_dato parametro="DocTree t" %}
* **DocTreePath p**,  {% include w3api/param_description.html metodo=_dato parametro="DocTreePath p" %}
* **DocCommentTree t**,  {% include w3api/param_description.html metodo=_dato parametro="DocCommentTree t" %}
* **TreePath treePath**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath treePath" %}

## Clase Padre
[DocTreePath](/Java/DocTreePath/)

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
