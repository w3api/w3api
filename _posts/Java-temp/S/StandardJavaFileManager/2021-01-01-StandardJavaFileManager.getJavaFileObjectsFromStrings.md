---
title: StandardJavaFileManager.getJavaFileObjectsFromStrings()
permalink: /Java/StandardJavaFileManager/getJavaFileObjectsFromStrings/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="getJavaFileObjectsFromStrings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterable<? extends JavaFileObject> getJavaFileObjectsFromStrings(Iterable<String> names)
~~~

## Parámetros
* **Iterable&lt;String&gt; names**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<String> names" %}

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
