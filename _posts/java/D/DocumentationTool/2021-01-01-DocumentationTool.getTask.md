---
title: DocumentationTool.getTask()
permalink: /Java/DocumentationTool/getTask/
date: 2021-01-11
key: Java.D.DocumentationTool
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentationTool.metodos valor="getTask" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DocumentationTool.DocumentationTask getTask(Writer out, JavaFileManager fileManager, DiagnosticListener<? super JavaFileObject> diagnosticListener, Class<?> docletClass, Iterable<String> options, Iterable<? extends JavaFileObject> compilationUnits)
~~~

## Parámetros
* **DiagnosticListener&lt;? super JavaFileObject&gt; diagnosticListener**,  {% include w3api/param_description.html metodo=_dato parametro="DiagnosticListener<? super JavaFileObject> diagnosticListener" %}
* **JavaFileManager fileManager**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager fileManager" %}
* **Class&lt;?&gt; docletClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> docletClass" %}
* **Iterable&lt;? extends JavaFileObject&gt; compilationUnits**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends JavaFileObject> compilationUnits" %}
* **Iterable&lt;String&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<String> options" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_dato parametro="Writer out" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DocumentationTool](/Java/DocumentationTool/)

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
