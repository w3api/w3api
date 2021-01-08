---
title: JavaFileManager.getJavaFileForInput()
permalink: Java/JavaFileManager/getJavaFileForInput
date: 2021-01-04
key: JavaJava.J.JavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="getJavaFileForInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaFileObject getJavaFileForInput(JavaFileManager.Location location, String className, JavaFileObject.Kind kind) throws IOException
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}
* **JavaFileObject.Kind kind**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileObject.Kind kind" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
