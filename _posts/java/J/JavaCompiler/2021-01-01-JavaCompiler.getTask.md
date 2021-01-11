---
title: JavaCompiler.getTask()
permalink: Java/JavaCompiler/getTask
date: 2021-01-11
key: JavaJava.J.JavaCompiler
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaCompiler.metodos valor="getTask" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaCompiler.CompilationTask getTask(Writer out, JavaFileManager fileManager, DiagnosticListener<? super JavaFileObject> diagnosticListener, Iterable<String> options, Iterable<String> classes, Iterable<? extends JavaFileObject> compilationUnits)
~~~

## Parámetros
* **DiagnosticListener&lt;? super JavaFileObject&gt; diagnosticListener**,  {% include w3api/param_description.html metodo=_dato parametro="DiagnosticListener<? super JavaFileObject> diagnosticListener" %}
* **JavaFileManager fileManager**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager fileManager" %}
* **Iterable&lt;String&gt; classes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<String> classes" %}
* **Iterable&lt;? extends JavaFileObject&gt; compilationUnits**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends JavaFileObject> compilationUnits" %}
* **Iterable&lt;String&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<String> options" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_dato parametro="Writer out" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JavaCompiler](/Java/JavaCompiler/)

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
