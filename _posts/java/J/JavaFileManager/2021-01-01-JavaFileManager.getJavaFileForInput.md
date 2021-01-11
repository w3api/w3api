---
title: JavaFileManager.getJavaFileForInput()
permalink: Java/JavaFileManager/getJavaFileForInput
date: 2021-01-11
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
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **JavaFileObject.Kind kind**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject.Kind kind" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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
