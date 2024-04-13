---
title: SecureDirectoryStream.getFileAttributeView()
permalink: /Java/SecureDirectoryStream/getFileAttributeView/
date: 2021-01-11
key: Java.S.SecureDirectoryStream
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureDirectoryStream.metodos valor="getFileAttributeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<V extends FileAttributeView>V getFileAttributeView(Class<V> type)
<V extends FileAttributeView>V getFileAttributeView(T path, Class<V> type, LinkOption... options)
~~~

## Parámetros
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="LinkOption... options" %}
* **T path**,  {% include w3api/param_description.html metodo=_dato parametro="T path" %}
* **Class&lt;V&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> type" %}

## Clase Padre
[SecureDirectoryStream](/Java/SecureDirectoryStream/)

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
