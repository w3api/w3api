---
title: SourceCodeAnalysis.analyzeCompletion()
permalink: Java/SourceCodeAnalysis/analyzeCompletion
date: 2021-01-11
key: JavaJava.S.SourceCodeAnalysis
category: java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceCodeAnalysis.metodos valor="analyzeCompletion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SourceCodeAnalysis.CompletionInfo analyzeCompletion(String input)
~~~

## Parámetros
* **String input**,  {% include w3api/param_description.html metodo=_dato parametro="String input" %}

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
