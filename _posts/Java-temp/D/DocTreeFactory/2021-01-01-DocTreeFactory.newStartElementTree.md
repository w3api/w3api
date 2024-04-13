---
title: DocTreeFactory.newStartElementTree()
permalink: /Java/DocTreeFactory/newStartElementTree/
date: 2021-01-11
key: Java.D.DocTreeFactory
category: Java
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
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **boolean selfClosing**,  {% include w3api/param_description.html metodo=_dato parametro="boolean selfClosing" %}
* **List&lt;? extends DocTree&gt; attrs**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> attrs" %}

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
