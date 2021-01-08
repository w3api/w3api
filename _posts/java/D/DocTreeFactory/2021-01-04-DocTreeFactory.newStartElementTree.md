---
title: DocTreeFactory.newStartElementTree()
permalink: Java/DocTreeFactory/newStartElementTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newStartElementTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
StartElementTree newStartElementTree(Name name, List<? extends DocTree> attrs, boolean selfClosing)
~~~

## Parámetros
* **boolean selfClosing**,  {% include w3api/param_description.html metodo=_data parametro="boolean selfClosing" %}
* **List&lt;? extends DocTree&gt; attrs**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends DocTree> attrs" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

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
