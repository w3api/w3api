---
title: StandardJavaFileManager.setLocationForModule()
permalink: Java/StandardJavaFileManager/setLocationForModule
date: 2021-01-11
key: JavaJava.S.StandardJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="setLocationForModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void setLocationForModule(JavaFileManager.Location location, String moduleName, Collection<? extends Path> paths) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **String moduleName**,  {% include w3api/param_description.html metodo=_dato parametro="String moduleName" %}
* **Collection&lt;? extends Path&gt; paths**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends Path> paths" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
