---
title: DocTreePath.getPath()
permalink: Java/DocTreePath/getPath
date: 2021-01-04
key: JavaJava.D.DocTreePath
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreePath.metodos valor="getPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DocTreePath getPath(DocTreePath path, DocTree target)
public static DocTreePath getPath(TreePath treePath, DocCommentTree doc, DocTree target)
~~~

## Parámetros
* **DocCommentTree doc**,  {% include w3api/param_description.html metodo=_data parametro="DocCommentTree doc" %}
* **DocTreePath path**,  {% include w3api/param_description.html metodo=_data parametro="DocTreePath path" %}
* **TreePath treePath**,  {% include w3api/param_description.html metodo=_data parametro="TreePath treePath" %}
* **DocTree target**,  {% include w3api/param_description.html metodo=_data parametro="DocTree target" %}

## Clase Padre
[DocTreePath](/Java/DocTreePath/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreePath.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
