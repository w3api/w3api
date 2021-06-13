---
title: FileStore.getFileStoreAttributeView()
permalink: /Java/FileStore/getFileStoreAttributeView/
date: 2021-01-11
key: Java.F.FileStore
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileStore.metodos valor="getFileStoreAttributeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <V extends FileStoreAttributeView>V getFileStoreAttributeView(Class<V> type)
~~~

## Parámetros
* **Class&lt;V&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> type" %}

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
