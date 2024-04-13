---
title: JavaCompiler.CompilationTask.addModules()
permalink: /Java/JavaCompiler/CompilationTask/addModules/
date: 2021-01-11
key: Java.J.JavaCompiler.CompilationTask
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaCompiler.CompilationTask.metodos valor="addModules" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addModules(Iterable<String> moduleNames)
~~~

## Parámetros
* **Iterable&lt;String&gt; moduleNames**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<String> moduleNames" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[JavaCompiler.CompilationTask](/Java/JavaCompiler/CompilationTask/)

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
