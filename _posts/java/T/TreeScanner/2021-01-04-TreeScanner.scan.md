---
title: TreeScanner.scan()
permalink: Java/TreeScanner/scan
date: 2021-01-04
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
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **Tree tree**,  {% include w3api/param_description.html metodo=_data parametro="Tree tree" %}
* **Iterable&lt;? extends Tree&gt; nodes**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<? extends Tree> nodes" %}

## Clase Padre
[TreeScanner](/Java/TreeScanner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
