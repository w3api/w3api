---
title: SecureDirectoryStream.getFileAttributeView()
permalink: Java/SecureDirectoryStream/getFileAttributeView
date: 2021-01-04
key: JavaJava.S.SecureDirectoryStream
category: java
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
* **Class&lt;V&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<V> type" %}
* **T path**,  {% include w3api/param_description.html metodo=_data parametro="T path" %}
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_data parametro="LinkOption... options" %}

## Clase Padre
[SecureDirectoryStream](/Java/SecureDirectoryStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureDirectoryStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
