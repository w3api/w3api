---
title: JavaCompiler.getTask()
permalink: Java/JavaCompiler/getTask
date: 2021-01-04
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
* **DiagnosticListener&lt;? super JavaFileObject&gt; diagnosticListener**,  {% include w3api/param_description.html metodo=_data parametro="DiagnosticListener<? super JavaFileObject> diagnosticListener" %}
* **Iterable&lt;String&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<String> options" %}
* **Iterable&lt;String&gt; classes**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<String> classes" %}
* **JavaFileManager fileManager**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager fileManager" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_data parametro="Writer out" %}
* **Iterable&lt;? extends JavaFileObject&gt; compilationUnits**,  {% include w3api/param_description.html metodo=_data parametro="Iterable<? extends JavaFileObject> compilationUnits" %}

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
{%- for _ldc in site.data.Java.J.JavaCompiler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
