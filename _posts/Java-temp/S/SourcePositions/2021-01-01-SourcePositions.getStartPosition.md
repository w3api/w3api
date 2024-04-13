---
title: SourcePositions.getStartPosition()
permalink: /Java/SourcePositions/getStartPosition/
date: 2021-01-11
key: Java.S.SourcePositions
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourcePositions.metodos valor="getStartPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long getStartPosition(CompilationUnitTree file, Tree tree)
~~~

## Parámetros
* **Tree tree**,  {% include w3api/param_description.html metodo=_dato parametro="Tree tree" %}
* **CompilationUnitTree file**,  {% include w3api/param_description.html metodo=_dato parametro="CompilationUnitTree file" %}

## Clase Padre
[SourcePositions](/Java/SourcePositions/)

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
