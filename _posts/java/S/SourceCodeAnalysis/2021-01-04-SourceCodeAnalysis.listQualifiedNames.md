---
title: SourceCodeAnalysis.listQualifiedNames()
permalink: Java/SourceCodeAnalysis/listQualifiedNames
date: 2021-01-04
key: JavaJava.S.SourceCodeAnalysis
category: java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceCodeAnalysis.metodos valor="listQualifiedNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SourceCodeAnalysis.QualifiedNames listQualifiedNames(String code, int cursor)
~~~

## Parámetros
* **int cursor**,  {% include w3api/param_description.html metodo=_data parametro="int cursor" %}
* **String code**,  {% include w3api/param_description.html metodo=_data parametro="String code" %}

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
