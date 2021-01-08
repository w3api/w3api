---
title: FileStore.getAttribute()
permalink: Java/FileStore/getAttribute
date: 2021-01-04
key: JavaJava.F.FileStore
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileStore.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Object getAttribute(String attribute) throws IOException
~~~

## Parámetros
* **String attribute**,  {% include w3api/param_description.html metodo=_data parametro="String attribute" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[FileStore](/Java/FileStore/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileStore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
