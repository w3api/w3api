---
title: JavaCompiler.CompilationTask.addModules()
permalink: Java/JavaCompiler/CompilationTask/addModules
date: 2021-01-04
key: JavaJava.J.JavaCompiler.CompilationTask
category: java
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
* **Iterable&lt;String&gt; moduleNames**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<String> moduleNames" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JavaCompiler.CompilationTask](/Java/JavaCompiler/CompilationTask/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaCompiler.CompilationTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
