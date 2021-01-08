---
title: TaskEvent.TaskEvent()
permalink: Java/TaskEvent/TaskEvent
date: 2021-01-04
key: JavaJava.T.TaskEvent
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TaskEvent.constructores valor="TaskEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TaskEvent(TaskEvent.Kind kind)
public TaskEvent(TaskEvent.Kind kind, CompilationUnitTree unit)
public TaskEvent(TaskEvent.Kind kind, CompilationUnitTree unit, TypeElement clazz)
public TaskEvent(TaskEvent.Kind kind, JavaFileObject sourceFile)
~~~

## Parámetros
* **TaskEvent.Kind kind**,  {% include w3api/param_description.html metodo=_data parametro="TaskEvent.Kind kind" %}
* **TypeElement clazz**,  {% include w3api/param_description.html metodo=_data parametro="TypeElement clazz" %}
* **CompilationUnitTree unit**,  {% include w3api/param_description.html metodo=_data parametro="CompilationUnitTree unit" %}
* **JavaFileObject sourceFile**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileObject sourceFile" %}

## Clase Padre
[TaskEvent](/Java/TaskEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TaskEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
