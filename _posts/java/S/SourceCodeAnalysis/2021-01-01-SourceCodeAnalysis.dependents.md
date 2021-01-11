---
title: SourceCodeAnalysis.dependents()
permalink: Java/SourceCodeAnalysis/dependents
date: 2021-01-11
key: JavaJava.S.SourceCodeAnalysis
category: java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceCodeAnalysis.metodos valor="dependents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Collection<Snippet> dependents(Snippet snippet)
~~~

## Parámetros
* **Snippet snippet**,  {% include w3api/param_description.html metodo=_dato parametro="Snippet snippet" %}

## Clase Padre
[SourceCodeAnalysis](/Java/SourceCodeAnalysis/)

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
