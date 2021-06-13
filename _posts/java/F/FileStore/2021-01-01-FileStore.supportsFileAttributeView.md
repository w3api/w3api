---
title: FileStore.supportsFileAttributeView()
permalink: /Java/FileStore/supportsFileAttributeView/
date: 2021-01-11
key: Java.F.FileStore
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileStore.metodos valor="supportsFileAttributeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean supportsFileAttributeView(Class<? extends FileAttributeView> type)
public abstract boolean supportsFileAttributeView(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Class&lt;? extends FileAttributeView&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends FileAttributeView> type" %}

## Clase Padre
[FileStore](/Java/FileStore/)

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
