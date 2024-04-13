---
title: JavaCompiler.getStandardFileManager()
permalink: /Java/JavaCompiler/getStandardFileManager/
date: 2021-01-11
key: Java.J.JavaCompiler
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaCompiler.metodos valor="getStandardFileManager" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
StandardJavaFileManager getStandardFileManager(DiagnosticListener<? super JavaFileObject> diagnosticListener, Locale locale, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **DiagnosticListener&lt;? super JavaFileObject&gt; diagnosticListener**,  {% include w3api/param_description.html metodo=_dato parametro="DiagnosticListener<? super JavaFileObject> diagnosticListener" %}

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
