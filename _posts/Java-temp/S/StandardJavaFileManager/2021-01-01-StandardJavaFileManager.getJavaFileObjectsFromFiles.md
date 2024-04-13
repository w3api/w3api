---
title: StandardJavaFileManager.getJavaFileObjectsFromFiles()
permalink: /Java/StandardJavaFileManager/getJavaFileObjectsFromFiles/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="getJavaFileObjectsFromFiles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterable<? extends JavaFileObject> getJavaFileObjectsFromFiles(Iterable<? extends File> files)
~~~

## Parámetros
* **Iterable&lt;? extends File&gt; files**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends File> files" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

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
