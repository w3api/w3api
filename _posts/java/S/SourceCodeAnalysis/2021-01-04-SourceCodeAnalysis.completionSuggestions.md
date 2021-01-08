---
title: SourceCodeAnalysis.completionSuggestions()
permalink: Java/SourceCodeAnalysis/completionSuggestions
date: 2021-01-04
key: JavaJava.S.SourceCodeAnalysis
category: java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceCodeAnalysis.metodos valor="completionSuggestions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract List<SourceCodeAnalysis.Suggestion> completionSuggestions(String input, int cursor, int[] anchor)
~~~

## Parámetros
* **int cursor**,  {% include w3api/param_description.html metodo=_data parametro="int cursor" %}
* **int[] anchor**,  {% include w3api/param_description.html metodo=_data parametro="int[] anchor" %}
* **String input**,  {% include w3api/param_description.html metodo=_data parametro="String input" %}

## Clase Padre
[SourceCodeAnalysis](/Java/SourceCodeAnalysis/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SourceCodeAnalysis.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
