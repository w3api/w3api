---
title: StandardJavaFileManager.getJavaFileObjects()
permalink: /Java/StandardJavaFileManager/getJavaFileObjects/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="getJavaFileObjects" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterable<? extends JavaFileObject> getJavaFileObjects(File... files)
Iterable<? extends JavaFileObject> getJavaFileObjects(String... names)
default Iterable<? extends JavaFileObject> getJavaFileObjects(Path... paths)
~~~

## Parámetros
* **String... names**,  {% include w3api/param_description.html metodo=_dato parametro="String... names" %}
* **Path... paths**,  {% include w3api/param_description.html metodo=_dato parametro="Path... paths" %}
* **File... files**,  {% include w3api/param_description.html metodo=_dato parametro="File... files" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
