---
title: SourceCodeAnalysis.completionSuggestions()
permalink: /Java/SourceCodeAnalysis/completionSuggestions/
date: 2021-01-11
key: Java.S.SourceCodeAnalysis
category: Java
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
* **int[] anchor**,  {% include w3api/param_description.html metodo=_dato parametro="int[] anchor" %}
* **String input**,  {% include w3api/param_description.html metodo=_dato parametro="String input" %}
* **int cursor**,  {% include w3api/param_description.html metodo=_dato parametro="int cursor" %}

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
