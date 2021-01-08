---
title: DocTreeFactory.newErroneousTree()
permalink: Java/DocTreeFactory/newErroneousTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newErroneousTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ErroneousTree newErroneousTree(String text, Diagnostic<JavaFileObject> diag)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **Diagnostic&lt;JavaFileObject&gt; diag**,  {% include w3api/param_description.html metodo=_data parametro="Diagnostic<JavaFileObject> diag" %}

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
