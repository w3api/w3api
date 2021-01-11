---
title: TreeScanner.scan()
permalink: Java/TreeScanner/scan
date: 2021-01-11
key: JavaJava.T.TreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="scan" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R scan(Tree tree, P p)
public R scan(Iterable<? extends Tree> nodes, P p)
~~~

## Parámetros
* **Iterable&lt;? extends Tree&gt; nodes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends Tree> nodes" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **Tree tree**,  {% include w3api/param_description.html metodo=_dato parametro="Tree tree" %}

## Clase Padre
[TreeScanner](/Java/TreeScanner/)

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
