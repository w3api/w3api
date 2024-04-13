---
title: StandardJavaFileManager.getJavaFileObjectsFromPaths()
permalink: /Java/StandardJavaFileManager/getJavaFileObjectsFromPaths/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="getJavaFileObjectsFromPaths" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Iterable<? extends JavaFileObject> getJavaFileObjectsFromPaths(Iterable<? extends Path> paths)
~~~

## Parámetros
* **Iterable&lt;? extends Path&gt; paths**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends Path> paths" %}

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
