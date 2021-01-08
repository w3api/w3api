---
title: TreeScanner.visitTypeParameter()
permalink: Java/TreeScanner/visitTypeParameter
date: 2021-01-04
key: JavaJava.T.TreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitTypeParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitTypeParameter(TypeParameterTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **TypeParameterTree node**,  {% include w3api/param_description.html metodo=_data parametro="TypeParameterTree node" %}

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
