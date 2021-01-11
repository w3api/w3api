---
title: SimpleDocTreeVisitor.visit()
permalink: Java/SimpleDocTreeVisitor/visit
date: 2021-01-11
key: JavaJava.S.SimpleDocTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleDocTreeVisitor.metodos valor="visit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final R visit(DocTree node, P p)
public final R visit(Iterable<? extends DocTree> nodes, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **DocTree node**,  {% include w3api/param_description.html metodo=_dato parametro="DocTree node" %}
* **Iterable&lt;? extends DocTree&gt; nodes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends DocTree> nodes" %}

## Clase Padre
[SimpleDocTreeVisitor](/Java/SimpleDocTreeVisitor/)

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
