---
title: JavaCompiler.CompilationTask.setProcessors()
permalink: /Java/JavaCompiler/CompilationTask/setProcessors/
date: 2021-01-11
key: Java.J.JavaCompiler.CompilationTask
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaCompiler.CompilationTask.metodos valor="setProcessors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setProcessors(Iterable<? extends Processor> processors)
~~~

## Parámetros
* **Iterable&lt;? extends Processor&gt; processors**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends Processor> processors" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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
